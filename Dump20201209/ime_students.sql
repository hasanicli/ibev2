-- MySQL dump 10.13  Distrib 8.0.15, for Win64 (x86_64)
--
-- Host: localhost    Database: ime
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
-- Table structure for table `students`
--

DROP TABLE IF EXISTS `students`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `students` (
  `id_number` varchar(11) NOT NULL,
  `name` varchar(45) NOT NULL,
  `surname` varchar(45) NOT NULL,
  `school_number` varchar(45) NOT NULL,
  `branchID` int(11) NOT NULL,
  `classID` int(11) DEFAULT NULL,
  `record_date` datetime NOT NULL,
  `father_name` varchar(45) DEFAULT NULL,
  `mother_name` varchar(45) DEFAULT NULL,
  `birthdate` datetime DEFAULT NULL,
  `birth_place` varchar(45) DEFAULT NULL,
  `is_going` char(1) NOT NULL,
  `self_phone` varchar(11) DEFAULT NULL,
  `parent_phone1` varchar(11) DEFAULT NULL,
  `parent_phone2` varchar(11) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `photo_address` varchar(255) DEFAULT NULL,
  `is_active` char(1) NOT NULL,
  `gender` char(1) NOT NULL,
  PRIMARY KEY (`id_number`),
  UNIQUE KEY `idnumber_UNIQUE` (`id_number`),
  KEY `fk_student_class` (`classID`),
  KEY `fk_student_branch` (`branchID`),
  CONSTRAINT `fk_student_branch` FOREIGN KEY (`branchID`) REFERENCES `branches` (`id`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `fk_student_class` FOREIGN KEY (`classID`) REFERENCES `classes` (`id`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `students`
--

LOCK TABLES `students` WRITE;
/*!40000 ALTER TABLE `students` DISABLE KEYS */;
INSERT INTO `students` VALUES ('11111111111','Mehmet','Erhan','1',15,106,'2020-12-04 00:00:00','','','2007-01-01 00:00:00','','E','','','','','','E','E'),('22222222222','Fadime','Zehra','2',15,106,'2020-12-04 00:00:00','','','2007-01-01 00:00:00','','E','','','','','','E','E'),('33333333333','Ayşe','Şule','3',15,105,'2020-12-04 00:00:00','','','2007-01-01 00:00:00','','E','','','','','','E','E'),('44444444444','Burak','Göllü','4',15,105,'2020-12-04 00:00:00','','','2007-01-01 00:00:00','','E','','','','','','E','E'),('55555555555','A. Rıza','Göllü','5',15,NULL,'2020-12-04 00:00:00','','','2007-01-01 00:00:00','','E','','','','','','E','E'),('66666666666','Bekir','Göllü','6',15,105,'2020-12-04 00:00:00','','','2007-01-01 00:00:00','','E','','','','','','E','E');
/*!40000 ALTER TABLE `students` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-12-09 11:11:32
