

import mysql.connector as myConn

def runQuery(sql):
    con = myConn.connect(host='localhost',
                       database='sakila',
                       user='root',
                       password='root')
    cur=con.cursor()
    cur.execute(sql)
    res=cur.fetchall()
    return res

#conn =  myConn.connect(host='localhost',
#                       database='sakila',
#                       user='root',
#                       password='root')
#assert ( conn.is_connected()),"connection failed"

#cursor = conn.cursor()
#cursor.execute("select * from actor limit 5")
#row=cursor.fetchall()
#print row

print runQuery("select * from actor limit 5")


