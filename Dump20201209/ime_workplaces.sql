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
-- Table structure for table `workplaces`
--

DROP TABLE IF EXISTS `workplaces`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `workplaces` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `boss` varchar(45) NOT NULL,
  `departmentID` int(11) NOT NULL,
  `master_instructive` varchar(45) NOT NULL,
  `neighborhoodID` int(11) NOT NULL,
  `street` varchar(45) DEFAULT NULL,
  `address_number` varchar(45) DEFAULT NULL,
  `phone_number1` varchar(11) DEFAULT NULL,
  `phone_number2` varchar(11) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `government_contribution` char(1) NOT NULL,
  `dayID` int(11) DEFAULT NULL,
  `staffID` varchar(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  UNIQUE KEY `name_UNIQUE` (`name`),
  KEY `fk_workplace_department` (`departmentID`),
  KEY `fk_workplace_neighborhood` (`neighborhoodID`),
  KEY `fk_dayID_dayss` (`dayID`),
  KEY `fk_staffID_staffs` (`staffID`),
  CONSTRAINT `fk_dayID_dayss` FOREIGN KEY (`dayID`) REFERENCES `days` (`id`) ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT `fk_staffID_staffs` FOREIGN KEY (`staffID`) REFERENCES `staffs` (`id_number`) ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT `fk_workplace_department` FOREIGN KEY (`departmentID`) REFERENCES `departments` (`id`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `fk_workplace_neighborhood` FOREIGN KEY (`neighborhoodID`) REFERENCES `neighborhoods` (`id`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=69 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `workplaces`
--

LOCK TABLES `workplaces` WRITE;
/*!40000 ALTER TABLE `workplaces` DISABLE KEYS */;
INSERT INTO `workplaces` VALUES (66,'Pense Tic','Asd',49,'Asd',2,'','','','','','E',NULL,NULL),(67,'Yankeski Tic','Asd',49,'Asd',2,'','','','','','E',NULL,NULL),(68,'Tornavida Tic','Asd',49,'Asd',2,'','','','','','E',NULL,NULL);
/*!40000 ALTER TABLE `workplaces` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-12-09 11:11:33
