# Music-Recommendation-System
I have developed Music Recommendation System using Python and MySQL. It offers personalized music suggestion based on user preferences.

Mysql queries- thiss should perform before running the code

CREATE TABLE `artid` (
  `artistid` int DEFAULT NULL,
  `artistname` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

CREATE TABLE `fav_artist` (
  `Username` varchar(20) DEFAULT NULL,
  `Artist_name` varchar(100) DEFAULT NULL,
  KEY `Username` (`Username`),
  CONSTRAINT `fav_artist_ibfk_1` FOREIGN KEY (`Username`) REFERENCES `info` (`Username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

CREATE TABLE `info` (
  `Username` varchar(20) NOT NULL,
  `Email_id` varchar(20) DEFAULT NULL,
  `Phone_no` varchar(20) DEFAULT NULL,
  `Password` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`Username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

CREATE TABLE `mood_id` (
  `id` int DEFAULT NULL,
  `mood_name` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

CREATE TABLE `mood_id` (
  `id` int DEFAULT NULL,
  `mood_name` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
