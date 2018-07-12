import unittest
import mysql.connector
import Registration
import cfgconnection
import string

#this tests inputting a new member by checking if a user has the correct length username and password, and meets the
#extra requirements of a password and username


cnx = mysql.connector.connect(host=cfgconnection.configh(),
                              user=cfgconnection.configu(),
                              password=cfgconnection.configpass(),
                              database=cfgconnection.configdb(),
                              port=cfgconnection.configp())
cursor = cnx.cursor(buffered=True)

class test_Registration(unittest.TestCase):

    def test_unique_entry(self):
    #fails if the registration will allow you to input a username that is already in the database
        query = ("SELECT username FROM member")
        cursor.execute(query)
        cur = cursor.fetchone()
        while(cur is not None):
            result = Registration.ValidateUsername("%s" %cur)
            self.assertFalse(result)
            cur = cursor.fetchone()
    def test_length_true(self):
    #passes if a username is allowed a valid length (5-20 chars)
        name = "aaaaa";
        while (len(name)<21):
            result= Registration.ValidateUsername(name)
            self.assertTrue(result)
            name=name+("a")
    def test_length_less_than_valid(self):
    #fails if a username is allowed an invalid length less than 5 chars
        name=""
        while(len(name)<5):
            result = Registration.ValidateUsername(name)
            self.assertFalse(result)
            name=name+("a")
    def test_length_greater_than_valid(self):
    #fails if a username is allowed an invalid length greater than 20 chars (but only up to 100 chars)
        name=""
        while(len(name)<100):
            name=name+("a")
        while(len(name)>20):
            result = Registration.ValidateUsername(name)
            self.assertFalse(result)
            name = name[:-1]
    def test_invalid_chars(self):
    #fails if invalid characters are allowed in the username (anything not a letter or number)
        invalidlist = list(string.printable)
        invalidlist=invalidlist[62:]
        i=0
        name=invalidlist[i]+invalidlist[i]+invalidlist[i]+invalidlist[i]+invalidlist[i]
        while(i<len(invalidlist)):
            cur=''.join(name)
            result = Registration.ValidateUsername(cur)
            self.assertFalse(result)
            i+=1
    def test_valid_chars(self):
    #passes if valid characters are allowed in the username
        validlist = list(string.printable)
        validlist = validlist[:62]
        i = 0
        name = validlist[i] + validlist[i] + validlist[i] + validlist[i] + validlist[i]
        while (i < len(validlist)):
            cur = ''.join(name)
            result = Registration.ValidateUsername(cur)
            self.assertTrue(result)
            i += 1
    def test_password_too_small(self):
    #fails if a password is allowed to be less than 10 chars
        pw='aA1!'
        while(len(pw)<10):
            result = Registration.ValidatePassword(pw)
            self.assertFalse(result)
            pw=pw+'a'
    def test_password_too_big(self):
    #fails if a password is allowed to be greater than 30 chars
        pw = "aA1!"
        while (len(pw) < 100):
            pw = pw + ("a")
        while (len(pw) > 30):
            result = Registration.ValidatePassword(pw)
            self.assertFalse(result)
            pw = pw[:-1]
    def test_password_no_capital(self):
    #fails if a password is allowed to not have capital letters
        pw="aa1!aaaaaa"
        result = Registration.ValidatePassword(pw)
        self.assertFalse(result)
    def test_password_no_symbol(self):
    #fails if a password is allowed to have no symbols
        pw = "aa1Aaaaaaa"
        result = Registration.ValidatePassword(pw)
        self.assertFalse(result)
    def test_password_no_number(self):
    #fails if a password has no number
        pw = "aaA!aaaaaa"
        result = Registration.ValidatePassword(pw)
        self.assertFalse(result)
    def test_password_no_lower(self):
    #fails if a password has no lowercase letters
        pw = "AA1!AAAAAA"
        result = Registration.ValidatePassword(pw)
        self.assertFalse(result)
    def test_valid_password(self):
    #passes if a password is valid
        pw='aA1!aB**caa'
        result = Registration.ValidatePassword(pw)
        self.assertTrue(result)
if __name__=='__main__':
    unittest.main()