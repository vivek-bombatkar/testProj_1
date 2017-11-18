import facebook
import config

def getFacebookGraph(token):
    return facebook.GraphAPI(access_token=token, version="2.1")

def getSiteDesc(URL,fbGraph):
    return fbGraph.get_object(URL,fields="og_object")

def searchFB(type,string,fbGraph):
    return fbGraph.search(type=type,q=string)

def main():
    fbGraph = getFacebookGraph(config.ACCESS_TOKEN_FB)
    msg = fbGraph.get_object(id='161997914535776',fields='name')
    print msg

    msg = getSiteDesc('https%3A//stackoverflow.com/questions/11510850/python-facebook-api-need-a-working-example',fbGraph)
    print msg['og_object']['description']
    '''searchResult = searchFB('user','india',fbGraph)
    for res in searchResult:
        print res
    '''

if __name__ == '__main__':
    main()