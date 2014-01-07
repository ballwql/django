DROP DATABASE IF EXISTS `zend`;
CREATE DATABASE `zend`
    DEFAULT CHARACTER SET utf8
    DEFAULT COLLATE utf8_general_ci;

USE 'mysql';
GRANT ALL PRIVILEGES ON zend.* TO 'root'@'localhost' IDENTIFIED BY '123'

WITH GRANT OPTION;
FLUSH PRIVILEGES;