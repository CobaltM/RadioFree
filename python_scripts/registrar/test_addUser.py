import unittest
import mysql.connector
import cfgconnection
import string
import subprocess
#this tes
cnx = mysql.connector.connect(host=cfgconnection.configh(),
                              user=cfgconnection.configu(),
                              password=cfgconnection.configpass(),
                              database=cfgconnection.configdb(),
                              port=cfgconnection.configp())
cursor = cnx.cursor(buffered=True)
auxcursor = cnx.cursor(buffered=True)

class test_Registration(unittest.TestCase):
    def setUp(self):
        subprocess.call(["python","./addUser.py","RegTest","RegTest","127.0.0.1"],shell=True)
    def test_user_exists(self):
        result = False
        cursor.execute("select username from member where username = 'RegTest'")
        if(cursor.fetchone() is not None):
            result = True
        self.assertTrue(result)
    def test_followerCount_created(self):
        result = False
        cursor.execute("select followercount from member where username = 'RegTest' && followerCount = 0")
        if(cursor.fetchone() is not None):
            result = True
        self.assertTrue(result)
    def test_isBroadcasting_created(self):
        result = False
        cursor.execute("select followercount from member where username = 'RegTest' && isBroadcasting = 0")
        if (cursor.fetchone() is not None):
            result = True
        self.assertTrue(result)
    def test_ip_added(self):
        result = False
        cursor.execute("select followercount from member where username = 'RegTest' && ip is not Null")
        if (cursor.fetchone() is not None):
            result = True
        self.assertTrue(result)
    def test_password_exists(self):
        result = False
        cursor.execute("select username from member where password is not null && username = 'RegTest'")
        if (cursor.fetchone() is not None):
            result = True
        self.assertTrue(result)
    def test_password_is_correct(self):
        result = False
        cursor.execute("select username from member where password = 'RegTest' && username = 'RegTest'")
        if (cursor.fetchone() is not None):
            result = True
        self.assertTrue(result)
    def test_user_room_created(self):
        query = ("SELECT room_id FROM member")
        cursor.execute(query)
        cur=cursor.fetchone()
        if(cur is not None):
            result = True
        else:
            result = False
        self.assertTrue(result)
    def test_room_created(self):
        query1 = ("SELECT room_id FROM room WHERE room_id = %d")
        query2 = ("SELECT room_id FROM member WHERE member.username = 'RegTest'")
        cursor.execute(query2)
        cur = cursor.fetchone()
        if (cur is not None):
            rid = cur;
        else:
            result = False
        cursor.execute(query1 % rid)
        cur = cursor.fetchone()
        if (cur is not None):
            result = True
        else:
            result = False
        self.assertTrue(result)
    def test_room_unique(self):
        query = ("SELECT room_id FROM room where broadcaster = 'RegTest'")
        cursor.execute(query)
        cur = cursor.fetchone()
        result = 0
        if(cur is not None):
            while (cur is not None):
                print(cur)
                result += 1
                self.assertEqual(result,1)
                cur = cursor.fetchone()
        else:
            self.assertTrue(False)
    def test_member_room_id_linked(self):
        n=1
        query1=("SELECT username FROM member WHERE member.room_id = '%d'")

        query2=("SELECT broadcaster FROM room WHERE room.room_id = '%d'")

        while(n!=0):
            cursor.execute(query1 % n)
            cur1 = cursor.fetchone()
            cursor.execute(query2 % n)
            cur2 = cursor.fetchone()
            fetch1=cur1 is None
            fetch2=cur2 is None
            if(fetch1 ^ fetch2):
                self.assertTrue(False)
            if(fetch1 & fetch2):
                result=True
                break
            if(cur1 == cur2):
                result = True
            else:
                result = False
            self.assertTrue(result)
            n+=1
        self.assertTrue(result)
    def tearDown(self):
        query = ("DELETE FROM member WHERE `username`='RegTest';")
        cursor.execute(query)
        cnx.commit()
if __name__=="__main__":
    unittest.main()
