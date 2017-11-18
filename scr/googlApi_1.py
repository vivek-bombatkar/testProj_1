import config
import pprint
import json
from googleapiclient.discovery import build

def main():
  service = build("customsearch", "v1",developerKey=config.developerKey_google)

  result = service.cse().list(
      q='bombatkar',
      cx='017576662512468239146:omuauf_lfve',
    ).execute()
  #json.dumps(
  res = json.dumps(result)
  print json.dumps(result["items"])
  #for res1 in res:
  #  res = json.dumps(res1)
  #  pprint.pprint(res1[0])

if __name__ == '__main__':
  main()

