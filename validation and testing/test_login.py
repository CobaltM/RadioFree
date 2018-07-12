import unittest
import mysql.connector
import Login
import string
import cfgconnection

#this tests the limits of registering a user by


cnx = mysql.connector.connect(host=cfgconnection.configh(),
                              user=cfgconnection.configu(),
                              password=cfgconnection.configpass(),
                              database=cfgconnection.configdb(),
                              port=cfgconnection.configp())
cursor = cnx.cursor(buffered=True)
cursor2 = cnx.cursor(buffered=True)

class test_login(unittest.TestCase):

    def test_login_success(self):
        query = ("SELECT username FROM member")
        cursor.execute(query)
        un = cursor.fetchone()
        while(un is not None):
            query = ("SELECT password FROM member WHERE username = '%s'" % un)
            cursor2.execute(query)
            pw = cursor2.fetchone()
            result = Login.login("%s" %un,"%s" %pw)
            self.assertTrue(result)
            un = cursor.fetchone()
    def test_login_invalid_password(self):
        query = ("SELECT username FROM member")
        cursor.execute(query)
        un = cursor.fetchone()
        un="%s" %un
        pw="INVALID"
        result = Login.login("%s" % un, "%s" % pw)
        self.assertFalse(result)
    def test_login_other_passwords(self):
        query = ("SELECT username FROM member")
        cursor.execute(query)
        un = cursor.fetchone()
        un = "%s" % un
        query = ("SELECT password FROM member WHERE username = '%s'"%un)
        cursor.execute(query)
        pw=cursor.fetchone()
        query = ("SELECT password FROM member WHERE username!='%s' AND password!='%s'" %(''.join(un),''.join(pw)))
        cursor.execute(query)
        pw = cursor.fetchone()
        while (pw is not None ):
            result = Login.login("%s" % un, "%s" % pw)
            self.assertFalse(result)
            pw = cursor.fetchone()
    def test_login_invalid_username(self):
        un="INV"
        query = ("SELECT password FROM member")
        cursor.execute(query)
        pw = cursor.fetchone()
        pw = "%s" % pw
        result = Login.login("%s" % un, "%s" % pw)
        self.assertFalse(result)
if __name__=='__main__':
    unittest.main()