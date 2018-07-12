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
    password='root'
    return(password)
def hasPass():
    macOS=False
    return(macOS)
def configp():
    if(hasPass()):
        post='8889'
    else:
        post='3306'
    return (post)