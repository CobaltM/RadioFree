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

# Example Python Query 
query="SELECT 2 + 4 as Solution"

cursor = cnx.cursor(buffered=True)
cursor.execute(query)

ct=cursor.fetchone()
ct=ct[0]

# Columns for room
# Don't include the room_id because it is generated AUTO INCREMET on mysql 
# Make sure broadcaster is a valid existing username 

broadcaster = 'white'
spotifyLink = ct
url = 'https://badbitchesofatlanta.com'
description = 'reymond'
numberOfListeners = 666
chatId = 999
listenersId = 888


addRoom=("insert into room"
	    "(broadcaster, spotifyLink,"
	    " url, description, numberOfListeners,"
	    " chat_id, listeners_id)"
        "values ('%s','%d','%s','%s','%d','%d','%d')")

cursor.execute(addRoom %( 
	broadcaster , 
	spotifyLink , 
	url,
	description,
	numberOfListeners,
	chatId,
	listenersId))

cnx.commit()