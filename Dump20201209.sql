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
-- Table structure for table `archive`
--

DROP TABLE IF EXISTS `archive`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `archive` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `studentID` varchar(11) NOT NULL,
  `starting_date` datetime NOT NULL,
  `disconnection_date` datetime NOT NULL,
  `disconnection_causeID` int(11) NOT NULL,
  `document_number` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  KEY `fk_cause_archieve` (`disconnection_causeID`),
  KEY `fk_archieve_student` (`studentID`),
  CONSTRAINT `fk_archieve_cause` FOREIGN KEY (`disconnection_causeID`) REFERENCES `causes` (`id`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `fk_archieve_student` FOREIGN KEY (`studentID`) REFERENCES `students` (`id_number`) ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=83 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `archive`
--

LOCK TABLES `archive` WRITE;
/*!40000 ALTER TABLE `archive` DISABLE KEYS */;
INSERT INTO `archive` VALUES (59,'55555555555','2020-12-03 00:00:00','2020-12-03 00:00:00',28,'z'),(60,'33333333333','2020-12-03 00:00:00','2020-12-03 00:00:00',28,'z'),(61,'66666666666','2020-12-03 00:00:00','2020-12-03 00:00:00',28,'z'),(62,'44444444444','2020-12-03 00:00:00','2020-12-03 00:00:00',28,'z'),(63,'22222222222','2020-12-03 00:00:00','2020-12-03 00:00:00',28,'z'),(64,'11111111111','2020-12-03 00:00:00','2020-12-03 00:00:00',28,'z'),(65,'11111111111','2020-12-04 00:00:00','2020-12-04 00:00:00',28,'1'),(66,'11111111111','2020-12-04 00:00:00','2020-12-04 00:00:00',28,'2'),(67,'11111111111','2020-12-04 00:00:00','2020-12-04 00:00:00',28,'2'),(68,'11111111111','2020-12-04 00:00:00','2020-12-04 00:00:00',28,'3'),(69,'55555555555','2020-12-04 00:00:00','2020-12-04 00:00:00',28,'2'),(70,'33333333333','2020-12-04 00:00:00','2020-12-04 00:00:00',28,'1'),(71,'66666666666','2020-12-04 00:00:00','2020-12-04 00:00:00',28,'1'),(72,'44444444444','2020-12-04 00:00:00','2020-12-04 00:00:00',28,'1'),(73,'22222222222','2020-12-04 00:00:00','2020-12-04 00:00:00',28,'1'),(74,'11111111111','2020-12-04 00:00:00','2020-12-04 00:00:00',28,'1'),(75,'55555555555','2020-12-04 00:00:00','2020-12-04 00:00:00',28,'1'),(76,'33333333333','2020-12-04 00:00:00','2020-12-04 00:00:00',28,'1'),(77,'66666666666','2020-12-04 00:00:00','2020-12-04 00:00:00',28,'1'),(78,'44444444444','2020-12-04 00:00:00','2020-12-04 00:00:00',28,'1'),(79,'22222222222','2020-12-04 00:00:00','2020-12-04 00:00:00',28,'1'),(80,'11111111111','2020-12-04 00:00:00','2020-12-04 00:00:00',28,'1'),(81,'55555555555','2020-12-04 00:00:00','2020-12-04 00:00:00',28,'1'),(82,'33333333333','2020-12-04 00:00:00','2020-12-04 00:00:00',28,'1');
/*!40000 ALTER TABLE `archive` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `branches`
--

DROP TABLE IF EXISTS `branches`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `branches` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `departmentID` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  UNIQUE KEY `name_UNIQUE` (`name`),
  KEY `fk_branches_departments` (`departmentID`),
  CONSTRAINT `fk_branches_departments` FOREIGN KEY (`departmentID`) REFERENCES `departments` (`id`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=610 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `branches`
--

LOCK TABLES `branches` WRITE;
/*!40000 ALTER TABLE `branches` DISABLE KEYS */;
INSERT INTO `branches` VALUES (15,'Bobinaj',49),(17,'Lastikçilik',50),(18,'Pompacılık',50),(21,'Pano Tasarımı',49),(22,'İç Mekan',52),(23,'Döşeme',52),(113,'Cnc',51);
/*!40000 ALTER TABLE `branches` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `causes`
--

DROP TABLE IF EXISTS `causes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `causes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  UNIQUE KEY `name_UNIQUE` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=62 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `causes`
--

LOCK TABLES `causes` WRITE;
/*!40000 ALTER TABLE `causes` DISABLE KEYS */;
INSERT INTO `causes` VALUES (28,'Mezun'),(2,'Nakil'),(55,'Veli İstek');
/*!40000 ALTER TABLE `causes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `classes`
--

DROP TABLE IF EXISTS `classes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `classes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `parentID` int(11) DEFAULT NULL,
  `departmentID` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  UNIQUE KEY `name_UNIQUE` (`name`),
  KEY `fk_classes_parent_classes` (`parentID`),
  KEY `fk_classes_departments` (`departmentID`),
  CONSTRAINT `fk_classes_departments` FOREIGN KEY (`departmentID`) REFERENCES `departments` (`id`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `fk_classes_parent_classes` FOREIGN KEY (`parentID`) REFERENCES `parent_classes` (`id`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=108 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `classes`
--

LOCK TABLES `classes` WRITE;
/*!40000 ALTER TABLE `classes` DISABLE KEYS */;
INSERT INTO `classes` VALUES (105,'9A ELK',NULL,49),(106,'9B ELK',NULL,49);
/*!40000 ALTER TABLE `classes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `classes_days`
--

DROP TABLE IF EXISTS `classes_days`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `classes_days` (
  `classID` int(11) NOT NULL,
  `dayID` int(11) NOT NULL,
  PRIMARY KEY (`classID`,`dayID`),
  KEY `fk_classes_days2` (`dayID`),
  CONSTRAINT `fk_classes_days` FOREIGN KEY (`classID`) REFERENCES `classes` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_classes_days2` FOREIGN KEY (`dayID`) REFERENCES `days` (`id`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `classes_days`
--

LOCK TABLES `classes_days` WRITE;
/*!40000 ALTER TABLE `classes_days` DISABLE KEYS */;
INSERT INTO `classes_days` VALUES (106,1),(105,2),(105,3),(106,3),(105,4),(106,4),(105,5),(106,5);
/*!40000 ALTER TABLE `classes_days` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `days`
--

DROP TABLE IF EXISTS `days`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `days` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  UNIQUE KEY `name_UNIQUE` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `days`
--

LOCK TABLES `days` WRITE;
/*!40000 ALTER TABLE `days` DISABLE KEYS */;
INSERT INTO `days` VALUES (3,'Çarşamba'),(5,'Cuma'),(6,'Cumartesi'),(7,'Pazar'),(1,'Pazartesi'),(4,'Perşembe'),(2,'Salı');
/*!40000 ALTER TABLE `days` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `departments`
--

DROP TABLE IF EXISTS `departments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `departments` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  UNIQUE KEY `name_UNIQUE` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=66 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `departments`
--

LOCK TABLES `departments` WRITE;
/*!40000 ALTER TABLE `departments` DISABLE KEYS */;
INSERT INTO `departments` VALUES (49,'Elektrik'),(51,'Makine'),(52,'Mobilya'),(50,'Motor');
/*!40000 ALTER TABLE `departments` ENABLE KEYS */;
UNLOCK TABLES;

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

--
-- Table structure for table `neighborhoods`
--

DROP TABLE IF EXISTS `neighborhoods`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `neighborhoods` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  UNIQUE KEY `name_UNIQUE` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `neighborhoods`
--

LOCK TABLES `neighborhoods` WRITE;
/*!40000 ALTER TABLE `neighborhoods` DISABLE KEYS */;
INSERT INTO `neighborhoods` VALUES (2,'Cumhuriyet Mah'),(1,'Karaboyunlu'),(5,'Selimiye Mah.');
/*!40000 ALTER TABLE `neighborhoods` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `parent_classes`
--

DROP TABLE IF EXISTS `parent_classes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `parent_classes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  UNIQUE KEY `name_UNIQUE` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `parent_classes`
--

LOCK TABLES `parent_classes` WRITE;
/*!40000 ALTER TABLE `parent_classes` DISABLE KEYS */;
INSERT INTO `parent_classes` VALUES (14,'10A'),(15,'10B'),(16,'10C'),(17,'10D'),(18,'11A'),(19,'11B'),(21,'11D'),(22,'12A'),(23,'12B'),(24,'12C'),(25,'12D'),(10,'9A'),(11,'9B'),(12,'9C'),(13,'9D');
/*!40000 ALTER TABLE `parent_classes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `school_info`
--

DROP TABLE IF EXISTS `school_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `school_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `city` varchar(45) NOT NULL,
  `county` varchar(45) NOT NULL,
  `name` varchar(45) NOT NULL,
  `managerID` varchar(11) DEFAULT NULL,
  `coordinator_managerID` varchar(11) DEFAULT NULL,
  `phone_number1` varchar(11) DEFAULT NULL,
  `phone_number2` varchar(11) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  UNIQUE KEY `name_UNIQUE` (`name`),
  UNIQUE KEY `manager_UNIQUE` (`managerID`),
  UNIQUE KEY `coordinator_managerID_UNIQUE` (`coordinator_managerID`),
  CONSTRAINT `fk_school_coordinator` FOREIGN KEY (`coordinator_managerID`) REFERENCES `staffs` (`id_number`) ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT `fk_school_manager` FOREIGN KEY (`managerID`) REFERENCES `staffs` (`id_number`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `school_info`
--

LOCK TABLES `school_info` WRITE;
/*!40000 ALTER TABLE `school_info` DISABLE KEYS */;
INSERT INTO `school_info` VALUES (1,'OSMANİYE','Merkez','Şehit Onur Deniz Mesleki Eğitim Merkezi',NULL,NULL,'05056756565','03281165989','okul@okul.meb.gov.tr');
/*!40000 ALTER TABLE `school_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `staff_branches`
--

DROP TABLE IF EXISTS `staff_branches`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `staff_branches` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  UNIQUE KEY `name_UNIQUE` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `staff_branches`
--

LOCK TABLES `staff_branches` WRITE;
/*!40000 ALTER TABLE `staff_branches` DISABLE KEYS */;
INSERT INTO `staff_branches` VALUES (13,'Bilişim Teknolojileri'),(4,'Elektrik Elektronik Teknolojisi'),(14,'Güzellik Ve Saç Bakım Hizmetleri'),(12,'Makine Teknolojisi'),(9,'Metal Teknolojisi');
/*!40000 ALTER TABLE `staff_branches` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `staff_degrees`
--

DROP TABLE IF EXISTS `staff_degrees`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `staff_degrees` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  UNIQUE KEY `name_UNIQUE` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `staff_degrees`
--

LOCK TABLES `staff_degrees` WRITE;
/*!40000 ALTER TABLE `staff_degrees` DISABLE KEYS */;
INSERT INTO `staff_degrees` VALUES (11,'Koor Md Yrd'),(9,'Md. Yrd.'),(2,'Müdür'),(3,'Müdür Yardımcısı'),(10,'Öğretmen'),(12,'Okul Müdürü');
/*!40000 ALTER TABLE `staff_degrees` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `staffs`
--

DROP TABLE IF EXISTS `staffs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `staffs` (
  `id_number` varchar(11) NOT NULL,
  `name` varchar(45) NOT NULL,
  `surname` varchar(45) NOT NULL,
  `staff_branchID` int(11) NOT NULL,
  `staff_degreeID` int(11) NOT NULL,
  `phone_number` varchar(11) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id_number`),
  UNIQUE KEY `id_number_UNIQUE` (`id_number`),
  KEY `fk_staffs_branches` (`staff_branchID`),
  KEY `fk_staffs_degrees` (`staff_degreeID`),
  CONSTRAINT `fk_staffs_branches` FOREIGN KEY (`staff_branchID`) REFERENCES `staff_branches` (`id`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `fk_staffs_degrees` FOREIGN KEY (`staff_degreeID`) REFERENCES `staff_degrees` (`id`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `staffs`
--

LOCK TABLES `staffs` WRITE;
/*!40000 ALTER TABLE `staffs` DISABLE KEYS */;
/*!40000 ALTER TABLE `staffs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `staffs_days`
--

DROP TABLE IF EXISTS `staffs_days`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `staffs_days` (
  `dayID` int(11) NOT NULL,
  `staffID` varchar(11) NOT NULL,
  PRIMARY KEY (`dayID`,`staffID`),
  KEY `fk_staff_days_staff` (`staffID`),
  CONSTRAINT `fk_staff_days_day` FOREIGN KEY (`dayID`) REFERENCES `days` (`id`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `fk_staff_days_staff` FOREIGN KEY (`staffID`) REFERENCES `staffs` (`id_number`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `staffs_days`
--

LOCK TABLES `staffs_days` WRITE;
/*!40000 ALTER TABLE `staffs_days` DISABLE KEYS */;
/*!40000 ALTER TABLE `staffs_days` ENABLE KEYS */;
UNLOCK TABLES;

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

--
-- Table structure for table `temp_workplace`
--

DROP TABLE IF EXISTS `temp_workplace`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `temp_workplace` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `studentID` varchar(11) NOT NULL,
  `staffID` varchar(11) DEFAULT NULL,
  `starting_date` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  KEY `fk_temp_student` (`studentID`),
  KEY `fk_temp_staff` (`staffID`),
  CONSTRAINT `fk_temp_staff` FOREIGN KEY (`staffID`) REFERENCES `staffs` (`id_number`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_temp_student` FOREIGN KEY (`studentID`) REFERENCES `students` (`id_number`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=62 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `temp_workplace`
--

LOCK TABLES `temp_workplace` WRITE;
/*!40000 ALTER TABLE `temp_workplace` DISABLE KEYS */;
/*!40000 ALTER TABLE `temp_workplace` ENABLE KEYS */;
UNLOCK TABLES;

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

-- Dump completed on 2020-12-09 10:59:19
