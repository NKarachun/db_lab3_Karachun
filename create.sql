CREATE TABLE Wines
(
  wine_id              INT   NOT NULL,
  designation          char(100)  NOT NULL,
  country_id           char(80)  NOT NULL,
  province_id          char(2)  NOT NULL,
  points               float8 NOT NULL,
  price                float8 NOT NULL,
  tester_id            char(3)  NOT NULL
);


CREATE TABLE Countries
(
  country_id      char(2)  NOT NULL,
  country_name    char(20)  NOT NULL 
);


CREATE TABLE Provinces
(
  province_id     char(2)  NOT NULL,
  province_name   char(50)  NOT NULL
);


CREATE TABLE Testers
(
  tester_id      char(3)  NOT NULL ,
  tester_name    char(60) NOT NULL  
);


ALTER TABLE Wines ADD PRIMARY KEY (wine_id);
ALTER TABLE Countries ADD PRIMARY KEY (country_id);
ALTER TABLE Provinces ADD PRIMARY KEY (province_id);
ALTER TABLE Testers ADD PRIMARY KEY (tester_id);


ALTER TABLE Wines ADD CONSTRAINT FK_Wines_Countries FOREIGN KEY (country_id) REFERENCES Countries (country_id);
ALTER TABLE Wines ADD CONSTRAINT FK_Wines_Provinces FOREIGN KEY (province_id) REFERENCES Provinces (province_id);
ALTER TABLE Wines ADD CONSTRAINT FK_Wines_Testers FOREIGN KEY (tester_id) REFERENCES Testers (tester_id);