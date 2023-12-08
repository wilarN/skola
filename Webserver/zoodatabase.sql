-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               8.0.30 - MySQL Community Server - GPL
-- Server OS:                    Win64
-- HeidiSQL Version:             12.1.0.6537
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Dumping database structure for zoodatabase
CREATE DATABASE IF NOT EXISTS `zoodatabase` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `zoodatabase`;

-- Dumping structure for table zoodatabase.animals
CREATE TABLE IF NOT EXISTS `animals` (
  `animal_name` varchar(255) DEFAULT NULL,
  `breed` varchar(255) DEFAULT NULL,
  `owner` varchar(255) DEFAULT NULL,
  `age` int DEFAULT NULL,
  `description` text,
  `price` double DEFAULT NULL,
  `img_lnk` varchar(255) DEFAULT NULL,
  `weight` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table zoodatabase.animals: ~8 rows (approximately)
REPLACE INTO `animals` (`animal_name`, `breed`, `owner`, `age`, `description`, `price`, `img_lnk`, `weight`) VALUES
	('Peter', 'Indian Splonker', 'Peter', 3, 'He\'s a Splonker.', 900, 'http://www.orcasound.com/wp-content/uploads/2020/11/clifford-big-red-dog-movie-teaser-essay.jpg', 600),
	('Glub', 'GlibboGlobb', 'Peta', 13, 'He likes to run, in grass.', 3, 'https://i.ytimg.com/vi/4uH1Yrb5LgQ/hqdefault.jpg', 3),
	('Fido', 'Lagotto', 'Johan Jansson', 4, 'He is a normal dog.', 400, 'https://www.doglib.com/wp-content/uploads/sites/2/la/lagotto-lagotto-romagnolo-dog-face-breed.jpg', 12),
	('Glupert', 'Cat', 'John', 2, 'A very cute cat', 500, 'https://i.chzbgr.com/original/8979220480/hB62CEF7E/', 9),
	('Barky', 'Dog', 'Jane', 3, 'A very cute dog', 364, 'https://i2.wp.com/whatchareading.com/wp-content/uploads/2013/10/marvel-dog.jpg', 24),
	('Meow', 'Cat', 'John', 1, 'A very cute cat', 257, 'https://i.pinimg.com/736x/b3/7a/90/b37a90308310a77134e3391e9df1f1a7.jpg', 8),
	('Awoof', 'Dog', 'Jane', 2, 'A very cute dog', 435, 'https://pm1.narvii.com/7036/0b9c6a429b8f8ce671d7aac7608506ac6d40f744r1-1242-1234v2_uhq.jpg', 14),
	('Garage', 'Fish', 'Mary', 1, 'A very cute fish', 99999999, 'https://upload.wikimedia.org/wikipedia/commons/7/77/Puffer_Fish_DSC01257.JPG', NULL);

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
