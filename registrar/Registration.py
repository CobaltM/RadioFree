import mysql.connector
import sys
import json
import cfgconnection

#pip install mysql-connector
if (cfgconnection.hasPass()):
    cnx = mysql.connector.connect(host=cfgconnection.configh(),
                                  user=cfgconnection.configu(),
                                  password=cfgconnection.configpass(),
                                  database=cfgconnection.configdb(),
                                  port=cfgconnection.configp())
else:
    cnx = mysql.connector.connect(host=cfgconnection.configh(),
                                  user=cfgconnection.configu(),
                                  database=cfgconnection.configdb(),
                                  port=cfgconnection.configp())
#you can add password etc to the fields above
cursor=cnx.cursor(buffered=True)
def Registration(un,pw):
    test1=ValidateUsername(un)
    test2=ValidatePassword(pw)*2
    print(test1+test2)

def ValidateUsername(username):
    query=("SELECT username FROM member WHERE username = '{!s}'").format(username)
    #testuserbase is my personal name for the database
    cursor.execute(query)
    if cursor.fetchone() is not None:
        return False
    if(len(username)<5):
        return False
    if (len(username)>20):
        return False
    ln=list(username)
    i=0
    while(i<len(username)):
        nl=ord(ln[i])
        i+=1
        if(45<=nl&nl<=57):
            continue
        if(65<=nl&nl<=90):
            continue
        if(97<=nl&nl<=122):
            continue
        else:
            return False
    return True
def ValidatePassword(password):
    if(len(password)<10):
        return False
    if(len(password)>30):
        return False
    lp=list(password)
    i=0
    satisfyCap=False
    satisfyLow=False
    satisfySym=False
    satisfyNum=False
    while(i<len(password)):
        np=ord(lp[i])
        i+=1
        if(48<=np&np<=57):
            satisfyNum=True
            continue
        if(65<=np&np<=90):
            satisfyCap=True
            continue
        if(97<=np&np<=122):
            satisfyLow=True
            continue
        if(33<=np&np<=126):
            satisfySym=True
            continue
        else:
            return False
    if(satisfyCap&satisfyLow&satisfyNum&satisfySym):
        return True
    else:
        return False
cursor.close
cnx.close
if __name__=='__main__':
    Registration(sys.argv[1],sys.argv[2])