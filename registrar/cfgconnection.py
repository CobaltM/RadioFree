def configu():
    user = 'root'
    return(user)
def configh():
    host = '127.0.0.1'
    return(host)
def configdb():
    database = 'testuserbase'
    return(database)
def configpass():
    if(hasPass()):
        password='root'
    else:
        password=False
    return(password)
def hasPass():
    macOS=False
    #Change this to "True" if running on mamp
    return(macOS)
def configp():
    if(hasPass()):
        post='3306'
    else:
        post='3306'
    return (post)