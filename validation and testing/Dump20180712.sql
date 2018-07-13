CREATE DATABASE  IF NOT EXISTS `RadioFreeDatabase` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `RadioFreeDatabase`;
-- MySQL dump 10.13  Distrib 5.7.17, for Win64 (x86_64)
--
-- Host: localhost    Database: testuserbase
-- ------------------------------------------------------
-- Server version	5.7.21

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `member`
--

DROP TABLE IF EXISTS `member`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `member` (
  `username` varchar(16) NOT NULL,
  `password` varchar(32) NOT NULL,
  `room_id` int(11) DEFAULT NULL,
  `ip` varchar(45) DEFAULT NULL,
  `followerCount` int(11) DEFAULT NULL,
  `follower_id` varchar(169) DEFAULT NULL,
  `isBroadcasting` tinyint(4) DEFAULT NULL,
  PRIMARY KEY (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `member`
--

LOCK TABLES `member` WRITE;
/*!40000 ALTER TABLE `member` DISABLE KEYS */;
INSERT INTO `member` VALUES ('black','thunder',1,NULL,NULL,NULL,NULL),('joe','aruba',2,NULL,NULL,NULL,NULL),('kev','sev',3,NULL,NULL,NULL,NULL),('litany','violence',4,NULL,NULL,NULL,NULL),('pale','wind',5,NULL,NULL,NULL,NULL),('password1','aruba1',6,NULL,NULL,NULL,NULL),('red','napalm',7,NULL,NULL,NULL,NULL),('testa','testb',8,NULL,NULL,NULL,NULL),('white','steel',9,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `member` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `message`
--

DROP TABLE IF EXISTS `message`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `message` (
  `message_id` int(11) NOT NULL,
  `content` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`message_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `message`
--

LOCK TABLES `message` WRITE;
/*!40000 ALTER TABLE `message` DISABLE KEYS */;
/*!40000 ALTER TABLE `message` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `message_board`
--

DROP TABLE IF EXISTS `message_board`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `message_board` (
  `username` varchar(16) NOT NULL,
  `follower_notification1` varchar(50) DEFAULT NULL,
  `follower_notification2` varchar(45) DEFAULT NULL,
  `follower_notification3` varchar(45) DEFAULT NULL,
  `follower_notification4` varchar(45) DEFAULT NULL,
  `follower_notification5` varchar(45) DEFAULT NULL,
  `follower_notification6` varchar(45) DEFAULT NULL,
  `follower_notification7` varchar(45) DEFAULT NULL,
  `follower_notification8` varchar(45) DEFAULT NULL,
  `follower_notification9` varchar(50) DEFAULT NULL,
  `follower_notification` varchar(50) DEFAULT NULL,
  `message_id` int(11) DEFAULT NULL,
  `global_message` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`username`),
  KEY `messageboardtoglobal_idx` (`message_id`),
  CONSTRAINT `messageboardtoglobal` FOREIGN KEY (`message_id`) REFERENCES `message` (`message_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `messageboardtousername` FOREIGN KEY (`username`) REFERENCES `member` (`username`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `message_board`
--

LOCK TABLES `message_board` WRITE;
/*!40000 ALTER TABLE `message_board` DISABLE KEYS */;
/*!40000 ALTER TABLE `message_board` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `room`
--

DROP TABLE IF EXISTS `room`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `room` (
  `room_id` int(11) NOT NULL,
  `broadcaster` varchar(16) DEFAULT NULL,
  `spotifyLink` tinyint(4) DEFAULT NULL,
  `url` varchar(16) DEFAULT NULL,
  `description` varchar(200) DEFAULT NULL,
  `numberOfListeners` int(11) DEFAULT NULL,
  `chat_id` int(11) DEFAULT NULL,
  `listeners_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`room_id`),
  KEY `broadcastuser_idx` (`broadcaster`),
  CONSTRAINT `broadcastuser` FOREIGN KEY (`broadcaster`) REFERENCES `member` (`username`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `room`
--

LOCK TABLES `room` WRITE;
/*!40000 ALTER TABLE `room` DISABLE KEYS */;
INSERT INTO `room` VALUES (1,'black',1,'aaaaaX','listen to music!',NULL,NULL,NULL);
/*!40000 ALTER TABLE `room` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `room_public`
--

DROP TABLE IF EXISTS `room_public`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `room_public` (
  `room_id` int(11) NOT NULL,
  `isBroadcasting` tinyint(4) DEFAULT NULL,
  `broadcaster` varchar(16) DEFAULT NULL,
  `numberOfListeners` int(11) DEFAULT NULL,
  `description` varchar(200) DEFAULT NULL,
  `url` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`room_id`),
  CONSTRAINT `publictoid` FOREIGN KEY (`room_id`) REFERENCES `room` (`room_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `room_public`
--

LOCK TABLES `room_public` WRITE;
/*!40000 ALTER TABLE `room_public` DISABLE KEYS */;
/*!40000 ALTER TABLE `room_public` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `visitor`
--

DROP TABLE IF EXISTS `visitor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `visitor` (
  `ip` varchar(45) NOT NULL,
  `canChat` tinyint(4) DEFAULT NULL,
  PRIMARY KEY (`ip`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `visitor`
--

LOCK TABLES `visitor` WRITE;
/*!40000 ALTER TABLE `visitor` DISABLE KEYS */;
/*!40000 ALTER TABLE `visitor` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-07-12 20:37:37
