CREATE DATABASE income

-- Last in, first out, order matters because of foreign keys have a waterfall esq reliance structure
DROP TABLE IF EXISTS `median_income`;
DROP TABLE IF EXISTS `neighborhoods`;

# Dump 
LE `median_income` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `amount` decimal(10,2) NOT NULL,
  `year` int(10) NOT NULL,
  `tract_id` int(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16401 DEFAULT CHARSET=latin1

# Dump 
CREATE TABLE `neighborhoods` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `neighborhood` varchar(60) NOT NULL,
  `tract_id` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=32801 DEFAULT CHARSET=latin1
