import os
import json
import urllib
import config
import facebook



host = "https://graph.facebook.com"
path = "/me"

def printMe():
    #1
    params = urllib.urlencode({"access_token": config.ACCESS_TOKEN_FB})
    #2
    url = "{host}{path}?{params}".format(host=host, path=path, params=params)
    #3
    resp = urllib.urlopen(url).read()
    #4
    me = json.loads(resp)
    #print(me)

def main():
  # Fill in the values noted in previous steps here
  cfg = {
    "page_id"      : config.APP_ID_FB,  # Step 1
    "access_token" : config.ACCESS_TOKEN_FB   # Step 3
    }

  api = get_api(cfg)
  msg = "Hello, world!"
  status = api.put_wall_post(msg)

def get_api(cfg):
  graph = facebook.GraphAPI(cfg['access_token'])
  # Get page token to post as the page. You can skip
  # the following if you want to post as yourself.
  resp = graph.get_object('me/accounts')
  page_access_token = None
  for page in resp['data']:
    if page['id'] == cfg['page_id']:
      page_access_token = page['access_token']
  graph = facebook.GraphAPI(page_access_token)
  return graph
  # You can also skip the above if you get a page token:
  # http://stackoverflow.com/questions/8231877/facebook-access-token-for-pages
  # and make that long-lived token as in Step 3

if __name__ == "__main__":
  main()
#    assert self.access_token, "Write operations require an access token"
#AssertionError: Write operations require an access token
