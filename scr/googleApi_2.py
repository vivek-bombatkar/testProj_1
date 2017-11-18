from googleapiclient.discovery import build
import config

def getGooglService(key):
    return build("customsearch","v1",developerKey=key)

def googleSearch(str,service):
    return service.cse().list(q=str,cx='001132580745589424302:jbscnf14_dw').execute()
#cx='cx',
#cx='001132580745589424302:jbscnf14_dw',
#cx='017576662512468239146:omuauf_lfve'
def main():
    service = getGooglService(config.developerKey_google)
    res = googleSearch('vidhi vivek',service)
    for s in res['items']:
        print s['snippet']


if __name__ == '__main__':
    main()
