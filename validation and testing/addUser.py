import mysql.connector
import sys
import cfgconnection

#pip install mysql-connector
cnx = mysql.connector.connect(host=cfgconnection.configh(),
                              user=cfgconnection.configu(),
                              #password=cfgconnection.configpass,
                              database=cfgconnection.configdb(),
                              port=cfgconnection.configp())
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