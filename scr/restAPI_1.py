import requests
import mysql.connector as conn

def get_data():
    ship_api_url = "https://app.uhds.oregonstate.edu/api/webcam/ship"
    request_data = requests.get(ship_api_url)
    return request_data.json()

def writeSQL(SQL,*fields):
    con = conn.connect(host='localhost',database='sakila',user='root',password='root')
    cur=con.cursor()
    cur.execute(SQL)
    return cur.fetchall()

data = get_data()

for s in data:
    print(s['air_temp'] )