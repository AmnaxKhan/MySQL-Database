#!/bin/bash
mysql <<EOFMYSQL
use amnak;

#1)Show the tables that you have created. Use the command below:
SHOW TABLES;

#2)Show the schema of each table. Use the command below, once per tablename:
DESC Restaurant;
DESC Dish; 
DESC MenuItem; 
DESC FoodOrder; 

#3)Show how each table was created. Use the command below, once per tablename:
SHOW CREATE TABLE Restaurant;
SHOW CREATE TABLE Dish;
SHOW CREATE TABLE MenuItem;
SHOW CREATE TABLE FoodOrder;

#4)Show the foreign keys of each table. Use the command (fill in your own db name):
SELECT COLUMN_NAME, CONSTRAINT_NAME, REFERENCED_COLUMN_NAME, REFERENCED_TABLE_NAME
FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
WHERE REFERENCED_COLUMN_NAME IS NOT NULL AND CONSTRAINT_SCHEMA = 'amnak';

#5)Show all the records within every table. For each table, use the command:
SELECT * FROM Restaurant;
SELECT * FROM Dish;
SELECT * FROM MenuItem;
SELECT * FROM FoodOrder;

#6)Find and print the restaurant name and city for all restaurants serving Salad.
SELECT restaurantName, city 
FROM Restaurant
JOIN MenuItem ON Restaurant.restaurantID = MenuItem.restaurantNo
JOIN Dish ON MenuItem.dishNo = Dish.dishNo
WHERE Dish.dishName = 'Salad';

#7)Find all menu items served by Asian restaurants, sorted by price. Output the dish name, restaurant name, and price.

#8)Find and print the total number of menu items and the average price of the menu items for each restaurant.

#9)Find and print the total price of all orders placed for Eureka Pizza, assuming a 10% tax rate. Include the number of orders, the average base price of each order (without tax), the total base price of all orders (without tax), and total price (with tax) in the result. Note: There should be only 1 tuple in the result.

#10)Find and print the total price of all orders placed in March, assuming a 10% tax rate. Include the number of orders, the average base price of each order (without tax), the total base price of all orders (without tax), and total price (with tax) in the result. Note: There should be only 1 tuple in the result.


EOFMYSQL