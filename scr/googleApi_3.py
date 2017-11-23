from googleapiclient.discovery import build
import config

service = build("customsearch","v1",developerKey=config.developerKey_google)
result = service.cse().list(q="papa",cx='001132580745589424302:jbscnf14_dw',lr='lang_pt',start=4).execute()
print result
for res in result:
    print res

