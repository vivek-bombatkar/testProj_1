import mysql.connector as myConn
import requests

URL="http://api.openweathermap.org/data/2.5/forecast?id=524901&APPID=48a10244f0b2ed7fb4962396eee67c62"

def getURL(URL):
    data = requests.get(URL).json()
    return data
#print(data['list'][1]['clouds'])
#print(data['list'][1]['snow'])
def getDB():
    con = myConn.connect(host='localhost',database='sakila',user='root',password='root')
    cur=con.cursor()
    return cur

def executeSQL(SQL,value):
    #cur = getDB()
    con = myConn.connect(host='localhost',database='sakila',user='root',password='root')
    cur=con.cursor()
    cur.execute(SQL,value)
    result = cur.fetchall()
    return result

def main():
    urlData  = getURL(URL)
    #print(urlData['list'][1]['weather'])
    for val in urlData['list']:
        executeSQL("insert into openweathermap_1 (col1) values (%s)",str(val['weather']))
        print(str(val['weather']))


if __name__ == '__main__':
    main()
