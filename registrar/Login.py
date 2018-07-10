import mysql.connector
import sys
#pip install mysql-connector

cnx = mysql.connector.connect(host='127.0.0.1',
                              user='root',
                              database='testuserbase')
#you can add password etc to the fields above
cursor=cnx.cursor(buffered=True)
def login(username, password):
    query = ("SELECT username FROM member WHERE username = '%s'" %username)
    cursor.execute(query)
    cur=cursor.fetchone()
    if cur is not None:
        query = ("SELECT username FROM member WHERE password = '%s'" %password)
        cursor.execute(query)
        curp = cursor.fetchone()
        if(cur == curp):
            print(1)
            return True
        else:
            print(2)
            return False
    else:
        print(2)
        return False
if __name__=='__main__':
    login(sys.argv[1],sys.argv[2])