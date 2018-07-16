import mysql.connector
import sys

#pip install mysql-connector
import cfgconnection
def addU(follower=sys.argv[1],followed=sys.argv[2]):
    cnx = mysql.connector.connect(host=cfgconnection.configh(),
                                  user=cfgconnection.configu(),
                                  password=cfgconnection.configpass(),
                                  database=cfgconnection.configdb(),
                                  port=cfgconnection.configp())
    #follower_id is to be set up as follows:
    #"[username]_____,[username2]_____"
    #such that "_" makes the number of characters between each comma equal to 16
    #for instance
    #"white___________,red_____________,black___________"
    cnx.commit()
if __name__ == '__main__':
    addU()