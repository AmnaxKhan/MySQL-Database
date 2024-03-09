#!/bin/bash
mysql <<EOFMYSQL
use amnak;

CREATE TABLE Restaurant (
    restaurantID INT,
    restaurantName CHAR(15) NOT NULL,
    type CHAR(15) NOT NULL,
    city CHAR(15) NOT NULL, 
    PRIMARY KEY (restaurantID)
);

#different version for changing the default values (shown in line 15)
CREATE TABLE Restaurant (
    restaurantID INT PRIMARY KEY,
    restaurantName CHAR(15) NOT NULL DEFAULT 'NOT NULL',
    type CHAR(15) NOT NULL DEFAULT 'NOT NULL',
    city CHAR(15) NOT NULL DEFAULT 'NOT NULL'
);

CREATE TABLE Dish (
    dishNo INT,
    dishName CHAR(25) NOT NULL,
    PRIMARY KEY (dishNo),
    type ENUM('ap', 'en', 'ds') NOT NULL
);

CREATE TABLE MenuItem (
    itemNo INT PRIMARY KEY,
    restaurantNo INT,
    dishNo INT,
    price DECIMAL(4,2),
    FOREIGN KEY (restaurantNo) REFERENCES Restaurant(restaurantID),
    FOREIGN KEY (dishNo) REFERENCES Dish(dishNo),
    CHECK (price>= 5 AND price<= 50)
);

CREATE TABLE MenuItem (
    itemNo INT,
    restaurantNo INT,
    dishNo INT,
    price DECIMAL(4,2),
    PRIMARY KEY (itemNo),
    FOREIGN KEY (restaurantNo) REFERENCES Restaurant(restaurantID) ON DELETE RESTRICT,
    FOREIGN KEY (dishNo) REFERENCES Dish(dishNo) ON DELETE SET NULL
);


CREATE TABLE FoodOrder (
    orderNo INT,
    itemNo INT,
    date DATE CHECK (date >= '2024-01-01'),
    time TIME,
    PRIMARY KEY (orderNo),
    FOREIGN KEY (itemNo) REFERENCES MenuItem(itemNo)
);

CREATE TABLE FoodOrder (
    orderNo INT,
    itemNo INT,
    date DATE,
    time TIME,
    PRIMARY KEY (orderNo),
    FOREIGN KEY (itemNo) REFERENCES MenuItem(itemNo) ON DELETE CASCADE
);



show tables;
EOFMYSQL
