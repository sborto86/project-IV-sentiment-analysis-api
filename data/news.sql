CREATE TABLE IF NOT EXISTS `news_sentiment`.`news` (
  `idnews` INT AUTO_INCREMENT,
  `time` DATETIME NOT NULL,
  `title` TEXT(1000) NOT NULL,
  `idpeople` INT NOT NULL,
  `polarity` DECIMAL(3,2) NULL,
  `subjectivity` DECIMAL(3,2) NULL,
  `neg` DECIMAL(3,2) NULL,
  `neu` DECIMAL(3,2) NULL,
  `pos` DECIMAL(3,2) NULL,
  `compound` DECIMAL(3,2) NULL,
  PRIMARY KEY (`idnews`),
  INDEX `fk_news_people_idx` (`idpeople` ASC) VISIBLE,
  CONSTRAINT `fk_news_people`
    FOREIGN KEY (`idpeople`)
    REFERENCES `news_sentiment`.`people` (`idpeople`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);