import time
import urllib2
from bs4 import BeautifulSoup
from lxml import html
import requests
import time

def getURLbs4(url):
    pg = urllib2.urlopen(url)
    return pg

def getURL(url):
    return requests.get(url)

def getFile(path,mode):
    return open(path, mode=mode)

url="https://www.analyticsvidhya.com/blog/2015/10/beginner-guide-web-scraping-beautiful-soup-python/"
path=r'C:\VIVEK\testWEB_'+time.strftime('%d%m%Y_%H%M%S')+ '.txt'
#1
#data = getURLbs4(url)
#soup = BeautifulSoup(data)
#print("RESULT : " + '/n' + soup.prettify())

data1=getURL(url)
#print (data1.text)
f=getFile(path,'w')
f.writelines(data1.text)


