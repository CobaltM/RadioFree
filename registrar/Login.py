import mysql.connector

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
            return True
        else:
            return False
    else:
        return False