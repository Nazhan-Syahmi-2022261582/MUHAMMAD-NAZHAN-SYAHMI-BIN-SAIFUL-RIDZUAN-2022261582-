-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 03, 2024 at 06:52 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hotel`
--

-- --------------------------------------------------------

--
-- Table structure for table `hotel`
--

CREATE TABLE `hotel` (
  `first_name_label` text NOT NULL,
  `last_name_label` text NOT NULL,
  `contact_label` int(100) NOT NULL,
  `age_label` int(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `checkin_label` int(100) NOT NULL,
  `checkout_label` int(100) NOT NULL,
  `terms_check` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `hotel`
--

INSERT INTO `hotel` (`first_name_label`, `last_name_label`, `contact_label`, `age_label`, `email`, `checkin_label`, `checkout_label`, `terms_check`) VALUES
('ADAM', 'ISKANDAR', 133844604, 25, 'Registered', 14, 26, 'Accepted'),
('LUZMAN ', 'THAQIF', 1234567890, 27, 'Registered', 30, 10, 'Accepted'),
('NAZHAN', 'SYAHMI', 1155154386, 32, 'Registered', 30, 15, 'Accepted'),
('AFIF', 'ZAIDI', 1987776502, 32, 'Registered', 4, 14, 'Accepted'),
('IZZAT', 'SYAHMI', 133752873, 18, 'Registered', 7, 14, 'Accepted');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
