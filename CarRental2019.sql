CREATE DATABASE  IF NOT EXISTS `project_3330_part2` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `project_3330_part2`;
-- MySQL dump 10.13  Distrib 8.0.29, for Win64 (x86_64)
--
-- Host: localhost    Database: project_3330_part2
-- ------------------------------------------------------
-- Server version	8.0.29

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer` (
  `CustID` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(255) DEFAULT NULL,
  `Phone` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`CustID`)
) ENGINE=InnoDB AUTO_INCREMENT=233 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES (201,'A. Parks','(214) 555-0127'),(202,'S. Patel','(849) 811-6298'),(203,'A. Hernandez','(355) 572-5385'),(204,'G. Carver','(753) 763-8656'),(205,'Sh. Byers','(912) 925-5332'),(206,'L. Lutz','(931) 966-1775'),(207,'L. Bernal','(884) 727-0591'),(208,'I. Whyte','(811) 979-7345'),(209,'L. Lott','(954) 706-2219'),(210,'G. Clarkson','(309) 625-1838'),(211,'Sh. Dunlap','(604) 581-6642'),(212,'H. Gallegos','(961) 265-8638'),(213,'L. Perkins','(317) 996-3104'),(214,'M. Beach','(481) 422-0282'),(215,'C. Pearce','(599) 881-5189'),(216,'A. Hess','(516) 570-6411'),(217,'M. Lee','(369) 898-6162'),(218,'R. Booker','(730) 784-6303'),(219,'A. Crowther','(325) 783-4081'),(220,'H. Mahoney','(212) 262-8829'),(221,'J. Brown','(644) 756-0110'),(222,'H. Stokes','(931) 969-7317'),(223,'J. Reeves','(940) 981-5113'),(224,'A. Mcghee','(838) 610-5802'),(225,'L. Mullen','(798) 331-7777'),(226,'R. Armstrong','(325) 783-4081'),(227,'J. Greenaway','(212) 262-8829'),(228,'K. Kaiser Acosta','(228) 576-1557'),(229,'D. Kirkpatrick','(773) 696-8009'),(230,'A. Odonnell','(439) 536-8929'),(231,'K. Kay','(368) 336-5403'),(232,'Khanh Le','(837) 721-8965');
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `question_9`
--

DROP TABLE IF EXISTS `question_9`;
/*!50001 DROP VIEW IF EXISTS `question_9`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `question_9` AS SELECT 
 1 AS `Description`,
 1 AS `Year`,
 1 AS `Type`,
 1 AS `Category`,
 1 AS `Total Duration`,
 1 AS `Type of Duration`,
 1 AS `Price Per Unit`,
 1 AS `Total Amount`,
 1 AS `Paid`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `rate`
--

DROP TABLE IF EXISTS `rate`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rate` (
  `Type` int NOT NULL,
  `Category` int NOT NULL,
  `Weekly` int DEFAULT NULL,
  `Daily` int DEFAULT NULL,
  PRIMARY KEY (`Type`,`Category`),
  KEY `Category_idx` (`Category`),
  KEY `type_idx` (`Type`) /*!80000 INVISIBLE */,
  CONSTRAINT `categpry` FOREIGN KEY (`Category`) REFERENCES `vehicle` (`Category`),
  CONSTRAINT `type` FOREIGN KEY (`Type`) REFERENCES `vehicle` (`Type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rate`
--

LOCK TABLES `rate` WRITE;
/*!40000 ALTER TABLE `rate` DISABLE KEYS */;
INSERT INTO `rate` VALUES (1,0,480,80),(1,1,600,105),(2,0,530,90),(2,1,660,116),(3,0,600,100),(3,1,710,126),(4,0,685,115),(4,1,800,142),(5,0,780,130),(5,1,900,150),(6,0,685,115),(6,1,800,135);
/*!40000 ALTER TABLE `rate` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rental`
--

DROP TABLE IF EXISTS `rental`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rental` (
  `CustID` int NOT NULL,
  `VehicleID` varchar(20) NOT NULL,
  `StartDate` date NOT NULL,
  `OrderDate` date DEFAULT NULL,
  `RentalType` int DEFAULT NULL,
  `Qty` int DEFAULT NULL,
  `ReturnDate` date DEFAULT NULL,
  `TotalAmount` int DEFAULT NULL,
  `PaymentDate` date DEFAULT NULL,
  `Returned` int NOT NULL,
  PRIMARY KEY (`CustID`,`VehicleID`,`StartDate`),
  KEY `VehicleID_idx` (`VehicleID`) /*!80000 INVISIBLE */,
  CONSTRAINT `CustID` FOREIGN KEY (`CustID`) REFERENCES `customer` (`CustID`),
  CONSTRAINT `VehicleID` FOREIGN KEY (`VehicleID`) REFERENCES `vehicle` (`VehicleID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rental`
--

LOCK TABLES `rental` WRITE;
/*!40000 ALTER TABLE `rental` DISABLE KEYS */;
INSERT INTO `rental` VALUES (203,'JM3KE4DY4F0441471','2019-09-09','2019-05-22',1,4,'2019-09-13',460,'2019-09-09',1),(210,'19VDE1F3XEE414842','2019-11-01','2019-10-28',7,2,'2019-11-15',1200,NULL,0),(210,'JTHFF2C26F135BX45','2019-05-01','2019-04-15',7,1,'2019-05-08',600,'2019-05-08',1),(210,'JTHFF2C26F135BX45','2019-11-01','2019-10-28',7,2,'2019-11-15',1200,NULL,0),(210,'WAUTFAFH0E0010613','2019-11-01','2019-10-28',7,2,'2019-11-15',1200,NULL,0),(210,'WBA3A9G51ENN73366','2019-11-01','2019-10-28',7,2,'2019-11-15',1200,NULL,0),(210,'WBA3B9C59EP458859','2019-11-01','2019-10-28',7,2,'2019-11-15',1200,NULL,0),(210,'WDCGG0EB0EG188709','2019-11-01','2019-10-28',7,2,'2019-11-15',1200,NULL,0),(212,'19VDE1F3XEE414842','2019-06-10','2019-04-15',7,3,'2019-07-01',1800,'2019-06-10',1),(216,'1N6BF0KM0EN101134','2019-08-02','2019-03-15',7,4,'2019-08-30',2740,'2019-08-02',1),(216,'1N6BF0KM0EN101134','2019-08-30','2019-03-15',1,2,'2019-09-01',230,'2019-08-02',1),(221,'19VDE1F3XEE414842','2019-07-01','2019-06-12',7,1,'2019-07-08',600,'2019-07-01',1),(221,'19VDE1F3XEE414842','2019-07-09','2019-06-12',1,2,'2019-07-11',200,'2019-07-01',1),(221,'19VDE1F3XEE414842','2020-01-01','2019-12-15',7,4,'2020-01-29',2400,NULL,0),(221,'JTHFF2C26F135BX45','2020-01-01','2019-12-15',7,4,'2020-01-29',2400,NULL,0),(221,'WAUTFAFH0E0010613','2019-07-01','2019-06-12',7,1,'2019-07-08',600,'2019-07-01',1),(221,'WAUTFAFH0E0010613','2019-07-09','2019-06-12',1,2,'2019-07-11',200,'2019-07-01',1),(221,'WAUTFAFH0E0010613','2020-01-01','2019-12-15',7,4,'2020-01-29',2400,NULL,0),(221,'WBA3A9G51ENN73366','2020-01-01','2019-12-15',7,4,'2020-01-29',2400,NULL,0),(221,'WBA3B9C59EP458859','2020-01-01','2019-12-15',7,4,'2020-01-29',2400,NULL,0),(221,'WDCGG0EB0EG188709','2020-01-01','2019-12-15',7,4,'2020-01-29',2400,NULL,0),(229,'19VDE1F3XEE414842','2019-05-06','2019-04-12',1,4,'2019-05-10',400,'2019-05-06',1),(229,'WAUTFAFH0E0010613','2019-05-06','2019-04-12',1,4,'2019-05-10',400,'2019-05-06',1);
/*!40000 ALTER TABLE `rental` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vehicle`
--

DROP TABLE IF EXISTS `vehicle`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vehicle` (
  `VehicleID` varchar(20) NOT NULL,
  `Description` varchar(100) DEFAULT NULL,
  `Year` year DEFAULT NULL,
  `Type` int NOT NULL,
  `Category` int NOT NULL,
  PRIMARY KEY (`VehicleID`),
  KEY `type` (`Type`),
  KEY `category` (`Category`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vehicle`
--

LOCK TABLES `vehicle` WRITE;
/*!40000 ALTER TABLE `vehicle` DISABLE KEYS */;
INSERT INTO `vehicle` VALUES ('19VDE1F3XEE414842','Acura ILX',2014,1,1),('1FDEE3FL6EDA29122','Ford E 350',2014,6,0),('1FDRF3B61FEA87469','Ford Super Duty Pickup',2015,5,0),('1FTNF1CF2EKE54305','Ford F Series Pickup',2014,5,0),('1G1JD5SB3E4240835','Chevrolet Optra',2014,1,0),('1GB3KZCG1EF117132','Chevrolet Silverado',2014,5,0),('1HGCR2E3XEA305302','Honda Accord',2014,2,0),('1N4AB7AP2EN855026','Nissan Sentra',2014,1,0),('1N6BA0EJ9EN516565','Nissan Titan',2014,5,0),('1N6BF0KM0EN101134','Nissan NV',2014,6,0),('1VWCH7A3XEC037969','Volkswagen Passat',2014,2,1),('2HGFB2F94FH501940','Honda Civic',2015,1,0),('2T3DFREV0FW317743','Toyota RAV4',2015,4,0),('3MZBM1L74EM109736','Mazda 3',2014,1,0),('3N1CE2CP0FL409472','Nissan Versa Note',2015,1,0),('3N1CN7APXEK444458','Nissan Versa',2014,1,0),('3VW2A7AU1FM012211','Volkswagen Golf',2015,1,0),('4S4BRCFC1E3203823','Subaru Outback',2014,4,0),('4S4BSBF39F3261064','Subaru Outback',2015,4,0),('4S4BSELC0F3325370','Subaru Outback',2015,4,0),('5FNRL6H58KB133711','Honda Odyssey',2019,6,1),('5J6RM4H90FL028629','Honda CR-V',2015,4,0),('5N1AL0MM8EL549388','Infiniti JX35',2014,4,1),('5NPDH4AE2FH565275','Hyundai Elantra',2015,1,0),('5TDBKRFH4ES26D590','Toyota Highlander',2014,4,0),('5XYKT4A75FG610224','Kia Sorento',2015,4,0),('5XYKU4A7XFG622415','Kia Sorento',2015,4,0),('5XYKUDA77EG449709','Kia Sorento',2014,4,0),('JF1GPAA61F8314971','Subaru Impreza',2015,1,0),('JH4KC1F50EC800004','Acura RLX',2014,3,1),('JH4KC1F56EC000095','Acura RLX',2014,3,1),('JM1BM1V35E1210570','Mazda 3',2014,1,0),('JM3KE4DY4F0441471','Mazda CX5',2015,4,0),('JM3TB3DV0E0015742','Mazda CX9',2014,4,0),('JN8AS5MV0FW760408','Nissan Rogue Select',2015,4,0),('JTEZUEJR7E5081641','Toyota 4Runner',2014,4,0),('JTHBW1GG1F120DU53','Lexus ES 300h',2015,2,1),('JTHCE1BL3F151DE04','Lexus GS 350',2015,2,1),('JTHDL5EF9F5007221','Lexus LS 460',2015,3,1),('JTHFF2C26F135BX45','Lexus IS 250C',2015,1,1),('JTJHY7AX2F120EA11','Lexus LX 570',2015,4,1),('JTJJM7FX2E152CD75','Lexus GX460',2014,4,1),('JTMBFREV1FJ019885','Toyota RAV4',2015,4,0),('KM8SN4HF0FU107203','Hyundai Santa Fe',2015,4,0),('KMHJT3AF1FU028211','Hyundai Tucson',2015,4,0),('KMHTC6AD8EU998631','Hyundai Veloster',2014,1,0),('KNAFZ4A86E5195865','KIA Sportage',2014,4,0),('KNAFZ4A86E5195895','KIA Forte',2014,1,0),('KNAGN4AD2F5084324','Kia Optima Hybrid',2015,2,0),('KNALN4D75E5A57351','Kia Cadenza',2014,3,0),('KNALU4D42F6025717','Kia K900',2015,3,0),('KNDPCCA65F7791085','KIA Sportage',2015,4,0),('WA1LGAFE8ED001506','Audi Q7',2014,4,1),('WAU32AFD8FN005740','Audi A8',2015,3,1),('WAUTFAFH0E0010613','Audi A5',2014,1,1),('WBA3A9G51ENN73366','BMW 3 Series',2014,1,1),('WBA3B9C59EP458859','BMW 3 Series',2014,1,1),('WBAVL1C57EVR93286','BMW X1',2014,4,1),('WDCGG0EB0EG188709','Mercedes_Benz GLK',2014,1,1),('YV440MDD6F2617077','Volvo XC60',2015,4,1),('YV4940NB5F1191453','Volvo XC70',2015,4,1);
/*!40000 ALTER TABLE `vehicle` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `vrentalinfo`
--

DROP TABLE IF EXISTS `vrentalinfo`;
/*!50001 DROP VIEW IF EXISTS `vrentalinfo`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `vrentalinfo` AS SELECT 
 1 AS `OrderDate`,
 1 AS `StartDate`,
 1 AS `ReturnDate`,
 1 AS `TotalDays`,
 1 AS `VIN`,
 1 AS `Vehicle`,
 1 AS `Type`,
 1 AS `Category`,
 1 AS `CustomerID`,
 1 AS `CustomerName`,
 1 AS `OrderAmount`,
 1 AS `RentalBalance`*/;
SET character_set_client = @saved_cs_client;

--
-- Final view structure for view `question_9`
--

/*!50001 DROP VIEW IF EXISTS `question_9`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `question_9` AS select `t`.`Description` AS `Description`,`t`.`Year` AS `Year`,`t`.`Type` AS `Type`,`t`.`Category` AS `Category`,`t`.`TotalDuration` AS `Total Duration`,`t`.`TypeofDuration` AS `Type of Duration`,`t`.`PricePerUnit` AS `Price Per Unit`,(`t`.`TotalDuration` * `t`.`PricePerUnit`) AS `Total Amount`,`t`.`Paid` AS `Paid` from (select `v`.`Description` AS `Description`,`v`.`Year` AS `Year`,(case when (`v`.`Type` = 1) then 'Compact' when (`v`.`Type` = 2) then 'Medium' when (`v`.`Type` = 3) then 'Large' when (`v`.`Type` = 4) then 'SUV' when (`v`.`Type` = 5) then 'Truck' when (`v`.`Type` = 6) then 'VAN' else 'ERROR' end) AS `Type`,(case when (`v`.`Category` = 0) then 'Basic' when (`v`.`Category` = 1) then 'Luxury' else 'ERROR' end) AS `Category`,(case when (((to_days(`r`.`ReturnDate`) - to_days(`r`.`StartDate`)) % 7) = 0) then round(((to_days(`r`.`ReturnDate`) - to_days(`r`.`StartDate`)) / 7),0) when (((to_days(`r`.`ReturnDate`) - to_days(`r`.`StartDate`)) % 7) <> 0) then (to_days(`r`.`ReturnDate`) - to_days(`r`.`StartDate`)) else 'ERROR' end) AS `TotalDuration`,(case when (`r`.`RentalType` = 1) then 'Days' when (`r`.`RentalType` = 7) then 'Weeks' else 'ERROR' end) AS `TypeofDuration`,(case when (`r`.`RentalType` = 1) then `rt`.`Daily` when (`r`.`RentalType` = 7) then `rt`.`Weekly` else 'ERROR' end) AS `PricePerUnit`,(case when (`r`.`PaymentDate` is not null) then 'PAID' else 'NOT PAY YET' end) AS `Paid` from (((`customer` `c` join `vehicle` `v`) join `rental` `r`) join `rate` `rt`) where ((`r`.`CustID` = `c`.`CustID`) and (`r`.`VehicleID` = `v`.`VehicleID`) and (`c`.`Name` = 'J. Brown') and (`rt`.`Type` = `v`.`Type`) and (`rt`.`Category` = `v`.`Category`)) order by `r`.`StartDate`) `t` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `vrentalinfo`
--

/*!50001 DROP VIEW IF EXISTS `vrentalinfo`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `vrentalinfo` AS select `t`.`OrderDate` AS `OrderDate`,`t`.`StartDate` AS `StartDate`,`t`.`ReturnDate` AS `ReturnDate`,`t`.`TotalDays` AS `TotalDays`,`t`.`VehicleID` AS `VIN`,`t`.`Description` AS `Vehicle`,`t`.`Type` AS `Type`,`t`.`Category` AS `Category`,`t`.`CustID` AS `CustomerID`,`t`.`Name` AS `CustomerName`,`t`.`TotalAmount` AS `OrderAmount`,`t`.`RentalBalance` AS `RentalBalance` from (select `r`.`OrderDate` AS `OrderDate`,`r`.`StartDate` AS `StartDate`,`r`.`ReturnDate` AS `ReturnDate`,(to_days(`r`.`ReturnDate`) - to_days(`r`.`StartDate`)) AS `TotalDays`,`r`.`VehicleID` AS `VehicleID`,`v`.`Description` AS `Description`,(case when (`v`.`Type` = 1) then 'Compact' when (`v`.`Type` = 2) then 'Medium' when (`v`.`Type` = 3) then 'Large' when (`v`.`Type` = 4) then 'SUV' when (`v`.`Type` = 5) then 'Truck' when (`v`.`Type` = 6) then 'VAN' else 'ERROR' end) AS `Type`,(case when (`v`.`Category` = 0) then 'Basic' when (`v`.`Category` = 1) then 'Luxury' else 'ERROR' end) AS `Category`,`c`.`CustID` AS `CustID`,`c`.`Name` AS `Name`,`r`.`TotalAmount` AS `TotalAmount`,(case when (`r`.`PaymentDate` is not null) then 0 else `r`.`TotalAmount` end) AS `RentalBalance` from ((`customer` `c` join `vehicle` `v`) join `rental` `r`) where ((`r`.`CustID` = `c`.`CustID`) and (`r`.`VehicleID` = `v`.`VehicleID`)) order by `r`.`StartDate`) `t` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-05-08 21:45:07
