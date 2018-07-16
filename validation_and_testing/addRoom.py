import mysql.connector
import sys

#pip install mysql-connector
import cfgconnection
def addU(username=sys.argv[1],roomname=sys.argv[2],maxListeners = sys.argv[3],spotifyURI=sys.argv[4],description=sys.argv[5]):
    cnx = mysql.connector.connect(host=cfgconnection.configh(),
                                  user=cfgconnection.configu(),
                                  password=cfgconnection.configpass(),
                                  database=cfgconnection.configdb(),
                                  port=cfgconnection.configp())

if __name__ == '__main__':
    addU()