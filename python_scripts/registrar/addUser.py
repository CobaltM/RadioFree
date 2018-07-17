import mysql.connector
import sys

#pip install mysql-connector
import cfgconnection


cnx = mysql.connector.connect(host=cfgconnection.configh(),
                              user=cfgconnection.configu(),
                              password=cfgconnection.configpass(),
                              database=cfgconnection.configdb(),
                              port=cfgconnection.configp())


# Generate room_id usin'g the number of memebers 
query="SELECT COUNT(*) FROM member"
cursor = cnx.cursor(buffered=True)
cursor.execute(query)
ct=cursor.fetchone()
ct=ct[0]

print(sys.argv)

# Set SQL Query values 

username =sys.argv[1]
password = sys.argv[2]
ip = sys.argv[3]
room_id = ct

# Default values
followerCount = 0
follower_id = ''
isBroadcasting = 0  

addUser=("insert into member"
	    "(username, "
	    " password, "
	    " room_id, "
	    " ip, "
        " followerCount, "
	    " follower_id,"
	    " isBroadcasting) "
        "values ('%s','%s','%d','%s','%d','%s','%d')")

# Execute SQL Query
cursor.execute(addUser %(
	username, 
	password, 
	room_id, 
	ip, 
	followerCount, 
	follower_id, 
	isBroadcasting))
cnx.commit()
