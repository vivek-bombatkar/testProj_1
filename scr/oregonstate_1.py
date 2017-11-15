import requests
import mysql.connector as conn
import time
from decimal import *
URL = "https://app.uhds.oregonstate.edu/api/webcam/ship"

def get_data(URL):
    request_data = requests.get(URL)
    return request_data.json()

def writeSQL(SQL,*fields):
    con = conn.connect(host='localhost',database='sakila',user='root',password='root')
    cur=con.cursor()
    cur.execute(SQL,fields)
    con.commit()
    return True

def main():
    data = get_data(URL)
    for s in data:
        ID=time.strftime('%d%m%Y%H%M%S')
        print(Decimal(s['air_temp']))
        writeSQL('insert into oregonstate_2 (ID,air_temp,water_temp,lng,lat) '
                 'values (%s,%s,%s,%s,%s)',ID, Decimal(s['air_temp']),Decimal(s['water_temp']),Decimal(s['lng']),Decimal(s['lat']))
        #writeSQL('insert into oregonstate_1 (col1)  values (%s)', str(s) )


if __name__ == '__main__':
    main()