-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 14, 2024 at 07:16 AM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

CREATE DATABASE IF NOT EXISTS `career_guidance`

-- Table structure for table `recommended_roles`
CREATE TABLE `recommended_roles` (
  `user_id` int(11) NOT NULL,
  `role_id` int(11) NOT NULL,
  `rank` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Table structure for table `roles`
CREATE TABLE `roles` (
  `role_id` int(11) NOT NULL,
  `role` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Inserting data into `roles` table
INSERT INTO `roles` (`role_id`, `role`) VALUES
(1, 'Application Support Engineer'),
(2, 'Data Scientist'),
(3, 'Database Administrator'),
(4, 'Hardware Engineer'),
(5, 'Technical Writer'),
(6, 'Helpdesk Engineer'),
(7, 'Business Analyst'),
(8, 'Networking Engineer'),
(9, 'Project Manager'),
(10, 'Software tester'),
(11, 'Graphics Designer'),
(12, 'Customer Service Executive'),
(13, 'AI ML Specialist'),
(14, 'Cyber Security Specialist'),
(15, 'API Specialist'),
(16, 'Information Security Specialist'),
(17, 'Software Developer');

-- Table structure for table `skills`
CREATE TABLE `skills` (
  `skill_id` int(11) NOT NULL AUTO_INCREMENT,
  `skill_name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Inserting data into `skills` table
INSERT INTO `skills` (`skill_id`, `skill_name`) VALUES
(1, 'Database Fundamentals'),
(2, 'Computer Architecture'),
(3, 'Distributed Computing Systems'),
(4, 'Cyber Security'),
(5, 'Networking'),
(6, 'Software Development'),
(7, 'Programming Skills'),
(8, 'Project Management'),
(9, 'Computer Forensics Fundamentals'),
(10, 'Technical Communication'),
(11, 'AI ML'),
(12, 'Software Engineering'),
(13, 'Business Analysis'),
(14, 'Communication skills'),
(15, 'Data Science'),
(16, 'Troubleshooting skills'),
(17, 'Graphics Designing');

-- Table structure for table `users`
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


ALTER TABLE `recommended_roles`
  ADD PRIMARY KEY (`user_id`,`role_id`,`rank`),
  ADD KEY `role_id` (`role_id`);

ALTER TABLE `roles`
  ADD PRIMARY KEY (`role_id`);

ALTER TABLE `skills`
  ADD PRIMARY KEY (`skill_id`);

ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `recommended_roles`
  ADD CONSTRAINT `recommended_roles_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`),
  ADD CONSTRAINT `recommended_roles_ibfk_2` FOREIGN KEY (`role_id`) REFERENCES `roles` (`role_id`);
COMMIT;

