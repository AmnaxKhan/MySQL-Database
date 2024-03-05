#!/bin/bash
mysql <<EOFMYSQL
use amnak;

CREATE TABLE Restaurant (
    restaurantID INT PRIMARY KEY,
    restaurantName CHAR(15) NOT NULL,
    type CHAR(15) NOT NULL,
    city CHAR(15) NOT NULL
);

CREATE TABLE Dish (
    dishNo INT PRIMARY KEY,
    dishName CHAR(25) NOT NULL,
    type ENUM('ap', 'en', 'ds') NOT NULL
);

CREATE TABLE MenuItem (
    itemNo INT PRIMARY KEY,
    restaurantNo INT,
    dishNo INT,
    price DECIMAL(4,2),
    FOREIGN KEY (restaurantNo) REFERENCES Restaurant(restaurantID),
    FOREIGN KEY (dishNo) REFERENCES Dish(dishNo)
    CHECK (price >= '5' AND price <= '50')
);

CREATE TABLE FoodOrder (
    orderNo INT PRIMARY KEY,
    itemNo INT,
    date DATE CHECK (date >= '2024-01-01'),
    time TIME,
    FOREIGN KEY (itemNo) REFERENCES MenuItem(itemNo)
);


show tables;
EOFMYSQL
