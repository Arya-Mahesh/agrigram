/*
SQLyog Community Edition- MySQL GUI v8.03 
MySQL - 5.6.12-log : Database - farmers_app
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`farmers_app` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `farmers_app`;

/*Table structure for table `category` */

DROP TABLE IF EXISTS `category`;

CREATE TABLE `category` (
  `category_id` int(11) NOT NULL AUTO_INCREMENT,
  `category_name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`category_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `category` */

insert  into `category`(`category_id`,`category_name`) values (1,'seeds'),(2,'plants'),(3,'creepers'),(4,'aa');

/*Table structure for table `govt_policy` */

DROP TABLE IF EXISTS `govt_policy`;

CREATE TABLE `govt_policy` (
  `policy_id` int(11) NOT NULL AUTO_INCREMENT,
  `date` date DEFAULT NULL,
  `title` varchar(100) DEFAULT NULL,
  `content` varchar(100) DEFAULT NULL,
  `url` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`policy_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `govt_policy` */

insert  into `govt_policy`(`policy_id`,`date`,`title`,`content`,`url`) values (2,'2022-04-12','a','b','c');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `user_type` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`user_type`) values (1,'admin','admin','admin'),(2,'namjoon@gmail.com','1','user'),(3,'jin@gmail.com','1','user'),(4,'a@gmail.com','2','reject');

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `user_id` int(11) DEFAULT NULL,
  `username` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `post` varchar(100) DEFAULT NULL,
  `pin` int(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `user` */

insert  into `user`(`user_id`,`username`,`place`,`post`,`pin`,`email`,`phone`) values (2,'kim namjoon','plc','pst',678895,'namjoon@gmail.com','8976567890'),(3,'jin','pp','oo',678883,'jin@gmail.com','9876567890');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
