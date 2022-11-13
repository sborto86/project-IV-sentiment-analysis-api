CREATE TABLE IF NOT EXISTS `news_sentiment`.`people` (
  `idpeople` INT AUTO_INCREMENT,
  `fname` VARCHAR(45) NOT NULL,
  `countrycode` CHAR(3) NOT NULL,
  `party_name` VARCHAR(45) NULL,
  PRIMARY KEY (`idpeople`),
  INDEX `fk_people_country1_idx` (`countrycode` ASC) VISIBLE,
  CONSTRAINT `fk_people_country1`
    FOREIGN KEY (`countrycode`)
    REFERENCES `news_sentiment`.`country` (`countrycode`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);