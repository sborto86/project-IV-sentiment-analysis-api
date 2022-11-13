CREATE TABLE IF NOT EXISTS `country` (
  `countrycode` char(3) NOT NULL,
  `countryname` varchar(200) NOT NULL,
  `code` char(2) DEFAULT NULL,
  PRIMARY KEY (`countrycode`)
);
