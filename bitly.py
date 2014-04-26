import urllib
import urllib2
import json
import re

access_token = ''

def search(args):
    
    data = {}

    data['access_token'] = access_token
    data['query'] = args['query']
    data['cities'] = args['location']
    data['fields'] = 'title,description,aggregate_link'
    data['limit'] = 10
    
    get_params = urllib.urlencode(data)

    endpoint = 'https://api-ssl.bitly.com/v3/search' + '?' + get_params
    response = urllib2.urlopen(endpoint)
    data = json.load(response)
    
    #for result in  data['data']['results']:
    #    if 'description' in result.keys() and result['description'] != "":
    #        sentences = re.split('\. |: |;', result['description'])         
    #        if len(sentences) > 3:
    #            result['description']  = sentences[0]
            
    return data
