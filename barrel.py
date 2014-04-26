import os
import urllib
import bitly

import webapp2
import jinja2

from google.appengine.api import users
from google.appengine.ext import ndb


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class MainPage(webapp2.RequestHandler):

    def get(self):

        response = {}

        template_values = {
            'show_response': False
        }

        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))


class SearchPage(webapp2.RequestHandler):

    def post(self):
        user_input = {}
        user_input['query'] = self.request.get('query')
        user_input['location'] = self.request.get('location')

        response = bitly.search(user_input)

        template_values = {
            'response': response,
            'show_response': True,
            'response_found': response['data'] is not None and len(response['data']['results']) > 0
        }

        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))


application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/search.*', SearchPage),
], debug=True)
