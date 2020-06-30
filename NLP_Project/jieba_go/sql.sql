

#创建数据表
CREATE TABLE IF NOT EXISTS `gov_report`(
   `id` INT UNSIGNED AUTO_INCREMENT,
   `title` VARCHAR(100) NOT NULL,
	`years` VARCHAR(40) NOT NULL,
   `countent` VARCHAR(65535) NOT NULL,
   `submission_date` DATE,
   PRIMARY KEY ( `id` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8;




#插入数据
INSERT INTO gov_report (id,title,years,countent)
                       VALUES
                       ('','1979政府工作报告_华国锋','1979','');