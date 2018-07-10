import mysql.connector
import sys

#pip install mysql-connector

cnx = mysql.connector.connect(host='127.0.0.1',
                              user='root',
                              database='testuserbase')
addUser=("insert into member"
	    "(username, password) "
        "values ('%s','%s')")
cursor = cnx.cursor(buffered=True)
a=sys.argv[1]
b=sys.argv[2]
#addUser, %(a,b)
#print(addUser %(a,b))
cursor.execute(addUser %(a,b))
cnx.commit()
print("success!");