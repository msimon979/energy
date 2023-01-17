DROP DATABASE IF EXISTS `DB`;
CREATE DATABASE `DB`;
USE `DB`;

DROP TABLE IF EXISTS `product`;
CREATE TABLE `product` (
    `id` INT NOT NULL AUTO_INCREMENT primary key,
    `product_symbol` varchar(225),
    `product_description` varchar(225)
);