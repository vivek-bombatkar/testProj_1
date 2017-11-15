import os
import json
import urllib
import pprint
#import facebook

ACCESS_TOKEN = 'XXX'

host = "https://graph.facebook.com"
path = "/me"
params = urllib.urlencode({"access_token": ACCESS_TOKEN})

url = "{host}{path}?{params}".format(host=host, path=path, params=params)

resp = urllib.urlopen(url).read()

me = json.loads(resp)

pprint.pprint(me)