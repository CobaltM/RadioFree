import mysql.connector
import sys

#pip install mysql-connector
import cfgconnection


cnx = mysql.connector.connect(host=cfgconnection.configh(),
                              user=cfgconnection.configu(),
                              password=cfgconnection.configpass(),
                              database=cfgconnection.configdb(),
                              port=cfgconnection.configp())
query="SELECT COUNT(*) FROM member"
cursor = cnx.cursor(buffered=True)
cursor.execute(query)
ct=cursor.fetchone()
ct=ct[0]

addUser=("insert into member"
	    "(username, password, room_id,"
	    " ip, followerCount, follower_id,"
	    " isBroadcasting) "
        "values ('%s','%s','%d','%d')")

a=sys.argv[1]
b=sys.argv[2]
#addUser, %(a,b)
#print(addUser %(a,b))
cursor.execute(addUser %(a,b,ct,0))
cnx.commit()