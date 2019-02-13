CREATE DATABASE wanni_bot;

USE wanni_bot;

CREATE TABLE enfermedades(
    id_enfermedad int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nombre varchar(50) NOT NULL,
    causas varchar(500) NOT NULL,
    sintomas varchar(500) NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=latin1;


INSERT INTO enfermedades (nombre, causas, sintomas)
VALUES ('SIDA','Se produce por un virus Y Puede transmitirse por el contacto sexual o por el contacto con sangre','Fiebre,Dolor de cabeza,Dolor muscular y articular,Erupción cutánea, Dolor de garganta y llagas dolorosas en la boca'),
('Diabetes','No se sabe con certeza por qué sucede esto exactamente, aunque se cree que los factores genéticos y ambientales desempeñan un papel decisivo en el desarrollo de la diabetes','Aumento de la sed, Ganas frecuentes de orinar, Hambre extrema, Pérdida de peso inexplicable'),
('Gripe','Inhalan gotitas provenientes de la tos o los estornudos de alguien que tenga gripe.','tos, fiebre, dolor de cabeza, dolor de garganta y mucosidades nasales.');

SHOW TABLES;

SELECT * FROM enfermedades;

DESCRIBE enfermedades;

CREATE USER 'wanni'@'localhost' IDENTIFIED BY 'wanni.2019';
GRANT ALL PRIVILEGES ON wanni_bot.* TO 'wanni'@'localhost';
FLUSH PRIVILEGES;
