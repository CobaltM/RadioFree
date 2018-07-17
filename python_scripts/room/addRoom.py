import mysql.connector
import sys

#pip install mysql-connector
import cfgconnection

#

cnx = mysql.connector.connect(host=cfgconnection.configh(),
                              user=cfgconnection.configu(),
                              password=cfgconnection.configpass(),
                              database=cfgconnection.configdb(),
                              port=cfgconnection.configp())

cursor = cnx.cursor(buffered=True)
	
# SET Sql query
username=sys.argv[1]
roomname=sys.argv[2]
maxListeners = sys.argv[3]
spotifyURI=sys.argv[4]
description=sys.argv[5]

addRoom=("insert into room"
	    "(username, roomname,"
	    " maxNumberOfListeners, spotifyURI,"
	    " description)" 
        "values ('%s','%s','%d','%s','%s')")

# Execute SQL query

cursor.execute(addRoom %( 
	username,
	roomname,
	maxListeners,
	spotifyURI,
	description))
cnx.commit()