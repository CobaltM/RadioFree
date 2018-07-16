import unittest
import mysql.connector
import cfgconnection
import string
import subprocess
import re
#this tes
#6247
cnx = mysql.connector.connect(host=cfgconnection.configh(),
                              user=cfgconnection.configu(),
                              password=cfgconnection.configpass(),
                              database=cfgconnection.configdb(),
                              port=cfgconnection.configp())
cursor = cnx.cursor(buffered=True)
auxcursor = cnx.cursor(buffered=True)

class test_Registration(unittest.TestCase):
    def setUp(self):
        subprocess.call(["python", "./addUser.py", "RegTest", "RegTest", "127.0.0.1"], shell=True)
        subprocess.call(["python","./addRoom.py","RegTest","RegTestRoomName","10","https://open.spotify.com/album/4AZpJ7WG1RFcimSggc05ZC","RegTestDescriptionHere"],shell=True)
        subprocess.call(["python", "./addUser.py", "RegTest2", "RegTest2", "127.0.0.1"], shell=True)
        subprocess.call(["python", "./follow.py", "RegTest2", "RegTest"], shell=True)
    def test_followerCount_increased(self):
        result = False
        cursor.execute("SELECT followerCount from member where username = 'RegTest'")
        fcountfinal = cursor.fetchone()
        if(fcountfinal == 1):
            result = True
        self.assertTrue(result)
    def test_followerid_updated(self):
        result = False
        cursor.execute("SELECT follower_id from member where username = 'RegTest'")
        cur = cursor.fetchone()
        curtest = re.findall('^.*RegTest2________,',cur)
        if(curtest != []):
            result = True
        self.assertTrue(result)
    def tearDown(self):
        query = ("DELETE FROM member WHERE `username`='RegTest';")
        cursor.execute(query)
        query= ("DELETE FROM room where broadcaster = 'RegTest'")
        cursor.execute(query)
        query = ("DELETE FROM room_public where broadcaster = 'RegTest'")
        cursor.execute(query)
        query = ("DELETE FROM member WHERE `username`='RegTest2';")
        cursor.execute(query)
        query = ("DELETE FROM room where broadcaster = 'RegTest2'")
        cursor.execute(query)
        cnx.commit()

if __name__=="__main__":
    unittest.main()
