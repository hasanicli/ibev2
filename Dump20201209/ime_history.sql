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
-- Table structure for table `history`
--

DROP TABLE IF EXISTS `history`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `history` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `studentID` varchar(11) NOT NULL,
  `workplaceID` int(11) NOT NULL,
  `starting_date` datetime NOT NULL,
  `leaving_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  KEY `fk_history_student` (`studentID`),
  KEY `fk_history_workplace` (`workplaceID`),
  CONSTRAINT `fk_history_student` FOREIGN KEY (`studentID`) REFERENCES `students` (`id_number`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `fk_history_workplace` FOREIGN KEY (`workplaceID`) REFERENCES `workplaces` (`id`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=199 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `history`
--

LOCK TABLES `history` WRITE;
/*!40000 ALTER TABLE `history` DISABLE KEYS */;
INSERT INTO `history` VALUES (167,'55555555555',66,'2020-12-03 00:00:00','2020-12-03 00:00:00'),(168,'33333333333',68,'2020-12-03 00:00:00','2020-12-03 00:00:00'),(169,'66666666666',67,'2020-12-03 00:00:00','2020-12-03 00:00:00'),(170,'44444444444',66,'2020-12-03 00:00:00','2020-12-03 00:00:00'),(171,'22222222222',68,'2020-12-03 00:00:00','2020-12-03 00:00:00'),(172,'11111111111',67,'2020-12-03 00:00:00','2020-12-03 00:00:00'),(173,'55555555555',66,'2020-12-03 00:00:00','2020-12-03 00:00:00'),(174,'44444444444',66,'2020-12-03 00:00:00','2020-12-03 00:00:00'),(175,'55555555555',66,'2020-12-03 00:00:00','2020-12-03 00:00:00'),(176,'44444444444',66,'2020-12-03 00:00:00','2020-12-03 00:00:00'),(177,'55555555555',66,'2020-12-03 00:00:00','2020-12-03 00:00:00'),(178,'55555555555',66,'2020-12-03 00:00:00','2020-12-03 00:00:00'),(179,'44444444444',66,'2020-12-03 00:00:00','2020-12-03 00:00:00'),(181,'22222222222',66,'2020-12-04 00:00:00','2020-12-04 00:00:00'),(182,'11111111111',66,'2020-12-04 00:00:00','2020-12-04 00:00:00'),(183,'11111111111',66,'2020-12-04 00:00:00','2020-12-04 00:00:00'),(184,'11111111111',66,'2020-12-04 00:00:00','2020-12-04 00:00:00'),(185,'11111111111',66,'2020-12-04 00:00:00','2020-12-04 00:00:00'),(186,'11111111111',66,'2020-12-04 00:00:00','2020-12-04 00:00:00'),(187,'55555555555',66,'2020-12-04 00:00:00','2020-12-04 00:00:00'),(188,'33333333333',66,'2020-12-04 00:00:00','2020-12-04 00:00:00'),(189,'66666666666',66,'2020-12-04 00:00:00','2020-12-04 00:00:00'),(190,'44444444444',68,'2020-12-04 00:00:00','2020-12-04 00:00:00'),(191,'55555555555',66,'2020-12-04 00:00:00','2020-12-04 00:00:00'),(192,'33333333333',66,'2020-12-04 00:00:00','2020-12-04 00:00:00'),(193,'66666666666',66,'2020-12-04 00:00:00',NULL),(194,'44444444444',68,'2020-12-04 00:00:00',NULL),(195,'22222222222',68,'2020-12-04 00:00:00',NULL),(196,'11111111111',68,'2020-12-04 00:00:00',NULL),(197,'55555555555',66,'2020-12-04 00:00:00',NULL),(198,'33333333333',66,'2020-12-04 00:00:00',NULL);
/*!40000 ALTER TABLE `history` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-12-09 11:11:35
