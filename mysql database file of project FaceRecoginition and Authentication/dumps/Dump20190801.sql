-- MySQL dump 10.13  Distrib 8.0.15, for Win64 (x86_64)
--
-- Host: localhost    Database: testdb
-- ------------------------------------------------------
-- Server version	8.0.15

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `stud`
--

DROP TABLE IF EXISTS `stud`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `stud` (
  `name` varchar(20) DEFAULT NULL,
  `pass` varchar(20) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `college` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stud`
--

LOCK TABLES `stud` WRITE;
/*!40000 ALTER TABLE `stud` DISABLE KEYS */;
INSERT INTO `stud` VALUES ('Atiksha','hello',21,'GEHU'),('Ram','abcd',22,'Doon');
/*!40000 ALTER TABLE `stud` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `studentdata`
--

DROP TABLE IF EXISTS `studentdata`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `studentdata` (
  `regNO` int(11) NOT NULL AUTO_INCREMENT,
  `fName` varchar(50) DEFAULT NULL,
  `lName` varchar(50) DEFAULT NULL,
  `dob` varchar(20) DEFAULT NULL,
  `gender` varchar(2) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `pNo` varchar(15) DEFAULT NULL,
  `course` varchar(20) DEFAULT NULL,
  `batch` varchar(20) DEFAULT NULL,
  `bGroup` varchar(5) DEFAULT NULL,
  `addess` varchar(500) DEFAULT NULL,
  `ftName` varchar(50) DEFAULT NULL,
  `mtName` varchar(50) DEFAULT NULL,
  `oInfo` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`regNO`)
) ENGINE=InnoDB AUTO_INCREMENT=92 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `studentdata`
--

LOCK TABLES `studentdata` WRITE;
/*!40000 ALTER TABLE `studentdata` DISABLE KEYS */;
INSERT INTO `studentdata` VALUES (78,'Atiksha','Pundir','1998-11-13','F','atikshapundir1311@gmail.com','9874565478','Btech CS','2018-2022','A+','lane No-3, Meera Nagar Bapugram Rishikesh\n','Sukhpal singh Pundir','Sushila Pundir','Pass out of B.M.S.S.S\n\n'),(79,'Somika','Mishra','1998-02-13','F','Somkia123@gmail.com','9874646555','BCA','2018-2021','B+','Houseno-23,lane No-2, Subhash Nagar ,Dehradun\r\n','M Mishra','Ml Mishra','no\n'),(80,'Neeta','Rawat','1999-05-29','F','neetarawat123@gmail.com','9876544562','Btech CS','2018-2022','A+','lane No -11 , Shakantula Viwas ,shivkutti Clemen town ,Dehradun\n','Jaipal S Rawat','Punam Rawat','Student from paurdi\n'),(81,'Atiksha','Pundir','2000-12-03','F','atiksha123@gmail.com','8745684842','BCA','2018-2021','AB','lane no-9 Society Area near,  Graphic era hill University\n','Hardeep singh','Lila Rawat','localite\n');
/*!40000 ALTER TABLE `studentdata` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `students`
--

DROP TABLE IF EXISTS `students`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `students` (
  `name` varchar(255) DEFAULT NULL,
  `age` int(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `students`
--

LOCK TABLES `students` WRITE;
/*!40000 ALTER TABLE `students` DISABLE KEYS */;
INSERT INTO `students` VALUES ('Rachel',22),('Rachel',22),('Amanda',32),('Avi',13),('Michelle',17);
/*!40000 ALTER TABLE `students` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `subscribers`
--

DROP TABLE IF EXISTS `subscribers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `subscribers` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(50) NOT NULL,
  `fName` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `subscribers`
--

LOCK TABLES `subscribers` WRITE;
/*!40000 ALTER TABLE `subscribers` DISABLE KEYS */;
/*!40000 ALTER TABLE `subscribers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb2`
--

DROP TABLE IF EXISTS `tb2`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `tb2` (
  `name` varchar(255) DEFAULT NULL,
  `age` int(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb2`
--

LOCK TABLES `tb2` WRITE;
/*!40000 ALTER TABLE `tb2` DISABLE KEYS */;
/*!40000 ALTER TABLE `tb2` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb3`
--

DROP TABLE IF EXISTS `tb3`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `tb3` (
  `name` varchar(255) DEFAULT NULL,
  `age` int(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb3`
--

LOCK TABLES `tb3` WRITE;
/*!40000 ALTER TABLE `tb3` DISABLE KEYS */;
/*!40000 ALTER TABLE `tb3` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-08-01  7:47:33
