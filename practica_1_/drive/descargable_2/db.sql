CREATE DATABASE contact_escom;
USE contact_escom;

CREATE TABLE master (
  id_master int AUTO_INCREMENT PRIMARY KEY NOT NULL,
  name varchar(50) NOT NULL,
  surname varchar(50) NOT NULL,
  email varchar(50),
  stage varchar(50),
  instruction varchar(200),
  status int NOT NULL
);
CREATE TABLE user (
  email varchar(50) PRIMARY KEY NOT NULL,
  password varchar(100) NOT NULL
);

INSERT INTO user ('root@email.com', 'recuperacion2020');
