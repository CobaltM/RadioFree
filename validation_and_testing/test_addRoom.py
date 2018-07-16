import unittest
import mysql.connector
import cfgconnection
import string
import subprocess
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
    def test_member_isBroadcasting_is_one(self):
        result = False
        cursor.execute("select isBroadcasting from member where username = 'RegTest' && isBroadcasting = 1")
        if (cursor.fetchone() is not None):
            result = True
        self.assertTrue(result)
    def test_room_url_created(self):
        result = False
        cursor.execute("select url from room where broadcaster = 'RegTest' && url is not Null")
        if (cursor.fetchone() is not None):
            result = True
        self.assertTrue(result)
    def test_room_maxlistenersupdated(self):
        result = False
        cursor.execute("select maxNumberOfListeners from room where broadcaster = 'RegTest' && maxNumberOfListeners = 10")
        if (cursor.fetchone() is not None):
            result = True
        self.assertTrue(result)
    def test_spotify_uri_added(self):
        result = False
        cursor.execute("select room_id from room where broadcaster = 'RegTest' && spotifyURI = 'https://open.spotify.com/album/4AZpJ7WG1RFcimSggc05ZC'")
        if (cursor.fetchone() is not None):
            result = True
        self.assertTrue(result)
    def test_chat_id_generated(self):
        result = False
        cursor.execute("select room_id from room where broadcaster = 'RegTest' && chat_id is not Null")
        if (cursor.fetchone() is not None):
            result = True
        self.assertTrue(result)
    def test_roomName_added(self):
        result = False
        cursor.execute("select room_id from room where broadcaster = 'RegTest' && roomName = 'RegTestRoomName'")
        if (cursor.fetchone() is not None):
            result = True
        self.assertTrue(result)
    def test_room_url_unique(self):
        cursor.execute("SELECT url FROM room where broadcaster = 'RegTest'")
        cur = cursor.fetchone()
        result = 0
        if (cur is not None):
            while (cur is not None):
                result += 1
                self.assertEqual(result, 1)
                cur = cursor.fetchone()
        else:
            self.assertTrue(False)
    def test_description_added(self):
        result = False
        cursor.execute("select room_id from room where broadcaster = 'RegTest' && description='RegTestDescriptionHere'")
        if (cursor.fetchone() is not None):
            result = True
        self.assertTrue(result)
    def test_public_room_url_unique(self):
        cursor.execute("SELECT url FROM room_public where broadcaster = 'RegTest'")
        cur = cursor.fetchone()
        result = 0
        if (cur is not None):
            while (cur is not None):
                result += 1
                self.assertEqual(result, 1)
                cur = cursor.fetchone()
        else:
            self.assertTrue(False)
    def test_public_description_added(self):
        result = False
        cursor.execute("select room_id from room_public where broadcaster = 'RegTest' && description='RegTestDescriptionHere'")
        if (cursor.fetchone() is not None):
            result = True
        self.assertTrue(result)
    def test_roomName_public_added(self):
        result = False
        cursor.execute("select room_id from room_public where broadcaster = 'RegTest' && roomName = 'RegTestRoomName'")
        if (cursor.fetchone() is not None):
            result = True
        self.assertTrue(result)
    def test_room_url_public_created(self):
        result = False
        cursor.execute("select url from room_public where broadcaster = 'RegTest' && url is not Null")
        if (cursor.fetchone() is not None):
            result = True
        self.assertTrue(result)
    def test_room_id_created(self):
        result = False
        cursor.execute("select room_id from room where broadcaster = 'RegTest'")
        curroom =  cursor.fetchone()
        cursor.execute("select room_id from member where username = 'RegTest'")
        curmember = cursor.fetchone()
        if(curroom is not None):
            if(curmember is not None):
                if(curroom == curmember):
                    reuslt=True
        self.assertTrue(result)
    def test_room_id_public_created(self):
        result = False
        cursor.execute("select room_id from room_public where broadcaster = 'RegTest'")
        curroom =  cursor.fetchone()
        cursor.execute("select room_id from member where username = 'RegTest'")
        curmember = cursor.fetchone()
        if(curroom is not None):
            if(curmember is not None):
                if(curroom == curmember):
                    reuslt=True
        self.assertTrue(result)
    def test_member_isBroadcasting_public_is_one(self):
        result = False
        cursor.execute("select isBroadcasting from room_public where broadcaster = 'RegTest' && isBroadcasting = 1")
        if (cursor.fetchone() is not None):
            result = True
        self.assertTrue(result)
    def tearDown(self):
        query = ("DELETE FROM member WHERE `username`='RegTest';")
        cursor.execute(query)
        query= ("DELETE FROM room where broadcaster = 'RegTest'")
        cursor.execute(query)
        query = ("DELETE FROM room_public where broadcaster = 'RegTest'")
        cursor.execute(query)
        cnx.commit()

if __name__=="__main__":
    unittest.main()
