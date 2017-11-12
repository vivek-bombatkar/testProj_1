
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

PATH= r'C:\VIVEK\PROJECTS\practice_1\working'
PATH= PATH + "\data_" + time.strftime('%d%m%Y_%H%M%S') + ".txt"
URL = "https://www.udemy.com/gcp-data-engineer-and-cloud-architect/"
if len(sys.argv) == 2:
    URL=sys.argv[1]
    print("URL : " + URL)

def getRequests(URL):
    lgr.info("calling page : " + URL)
    result=rq.get(URL)
    lgr.info("call finish : " + URL)
    return result

def getUrllib2(URL):
    return ur2.urlopen(URL)

def getFile(path):
    return open(path,mode='w')

def exeSQL(sql,v1,v2):
    lgr.info(sql)
    con=cntr.connect(host='localhost',database='sakila',user='root',password='root')
    cur=con.cursor()
    cur.execute(sql,(v1,v2))
    con.commit()
    return ""

def main():
    #print("getRequests " + getRequests(URL).text)
    getFile(PATH).write(getRequests(URL).text)
    #"insert into batch_test (id,URL) values ('{0}','{1}')".format(time.strftime('%H%M%S'),"YYY"
    print exeSQL("insert into batch_test (id,URL) values (%s,%s)",time.strftime('%H%M%S'),URL)
    #print("getUrllib2 " + getUrllib2(URL))

if __name__ == '__main__':
    main()