
import requests as rq
import urllib2 as ur2
import sys
import time
import logging as lg
import mysql.connector as cntr
reload(sys)
sys.setdefaultencoding('utf-8')

lg.basicConfig(level=lg.INFO)
lgr=lg.getLogger(__name__)
hdlr=lg.FileHandler(r"logs\logFile.txt")
hdlr.setLevel(level=lg.INFO)
frmt=lg.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
hdlr.setFormatter(frmt)
lgr.addHandler(hdlr)

def getRequests(URL):
    try:
        lgr.info("calling page : " + URL)
        result=rq.get(URL).text
        lgr.info("call finish : " + URL)
    except:
        lgr.error(sys.exc_info()[0])
        return ""
    return result

def getUrllib2(URL):
    return ur2.urlopen(URL)

def getFile(path):
    return open(path,mode='a')

def exeSQL(sql,*values):
    try:
        #lgr.info(sql,values)
        con=cntr.connect(host='localhost',database='sakila',user='root',password='root')
        cur=con.cursor()
        cur.execute(sql,values)
        con.commit()
    except:
        lgr.error(sys.exc_info()[0])
        return "FAIL"
    return "DONE"

def getURLS(data):
    links=data.find("a href")
    if links == -1:
        return None,0
    startQ=data.find('"',links)
    endQ=data.find('"',startQ+1)
    url=data[startQ+1:endQ]
    return url,endQ

def processURL(timestampID,URL,PATH):
    #timestampID=time.strftime('%d%m%Y%H%M%S')
    urlText=getRequests(URL)
    #getFile(PATH).write(urlText)
    if urlText <> "":
        while True:
            nextURL,n  = getURLS(urlText)
            urlText = urlText[n:]
            if nextURL:
                if "https://" in nextURL:
                    nextURL=nextURL.replace("/url?q=","")+'\n'
                    getFile(PATH).write(nextURL)
                    lgr.info(exeSQL(
                        "insert into parent_child_urls (idparent_child_urls,parent_url,child_url) "
                        "values (%s,%s,%s)", timestampID, URL,nextURL))
                    #processURL(timestampID, nextURL, PATH)
            else:
                break
            #"insert into batch_test (id,URL) values ('{0}','{1}')".format(time.strftime('%H%M%S'),"YYY"
        lgr.info(exeSQL("insert into batch_test (id,URL) values (%s,%s)",timestampID,URL))
    else:
        lgr.info("NOTHING HAPPENED")
    return None

def main():
    PATH = r'C:\VIVEK\PROJECTS\practice_1\working'
    URL = "https://www.digitalocean.com/community/tutorials/an-introduction-to-string-functions-in-python-3"
    if len(sys.argv) == 3:
        URL = sys.argv[1]
        PATH = sys.argv[2]
        lgr.info("URL : " + URL)
        lgr.info("PATH : " + PATH)
    PATH = PATH + "\data_" + time.strftime('%d%m%Y_%H%M%S') + ".txt"

    timestampID = time.strftime('%d%m%Y%H%M%S')
    processURL(timestampID,URL,PATH)

if __name__ == '__main__':
    main()