#!/bin/bash
mysql <<EOFMYSQL
use amnak;

DROP TABLE Restaurant; 
DROP TABLE Dish; 
DROP TABLE MenuItem; 
DROP TABLE FoodOrder; 

EOFMYSQL