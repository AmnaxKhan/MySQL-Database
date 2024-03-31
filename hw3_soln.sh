mysql <<EOFMYSQL
use amnak;
show tables;

DROP TABLE FoodOrder; 
DROP TABLE MenuItem; 
DROP TABLE Dish; 
DROP TABLE Restaurant; 

CREATE TABLE Restaurant (
    restaurantID INT,
    restaurantName CHAR(15) NOT NULL,
    type CHAR(15) NOT NULL,
    city CHAR(15) NOT NULL, 
    PRIMARY KEY (restaurantID)
);

CREATE TABLE Dish (
    dishNo INT,
    dishName CHAR(25) NOT NULL,
    PRIMARY KEY (dishNo),
    type ENUM('ap', 'en', 'ds') NOT NULL
);



CREATE TABLE MenuItem (
    itemNo INT,
    restaurantNo INT,
    dishNo INT,
    price DECIMAL(4,2),
    CHECK (price >= 5 AND price <= 50),
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
    FOREIGN KEY (itemNo) REFERENCES MenuItem(itemNo) ON DELETE CASCADE
);


INSERT INTO Restaurant VALUES (0, 'Tasty Thai', 'Asian', 'Dallas'); 
INSERT INTO Restaurant VALUES (3, 'Eureka Pizza', 'Pizza', 'Fayetteville'); 
INSERT INTO Restaurant VALUES (5, 'Tasty Thai', 'Asian', 'Las Vegas'); 

INSERT INTO Dish VALUES (13, 'Spring Rolls', 'ap'); 
INSERT INTO Dish VALUES (15, 'Pad Thai', 'en'); 
INSERT INTO Dish VALUES (16, 'Pot Stickers', 'ap'); 
INSERT INTO Dish VALUES (22, 'Masaman Curry', 'en');
INSERT INTO Dish VALUES (10, 'Custard', 'ds');
INSERT INTO Dish VALUES (12, 'Garlic Bread', 'ap');
INSERT INTO Dish VALUES (44, 'Salad', 'ap');
INSERT INTO Dish VALUES (07, 'Cheese Pizza', 'en');
INSERT INTO Dish VALUES (19, 'Pepperoni Pizza', 'en');
INSERT INTO Dish VALUES (77, 'Veggie Supreme Pizza', 'en');

INSERT INTO MenuItem VALUES (0, 0, 13, 8.00); 
INSERT INTO MenuItem VALUES (1, 0, 16, 9.00); 
INSERT INTO MenuItem VALUES (2, 0, 44, 10.00); 
INSERT INTO MenuItem VALUES (3, 0, 15, 19.00); 
INSERT INTO MenuItem VALUES (4, 0, 22, 19.00); 
INSERT INTO MenuItem VALUES (5, 3, 44, 6.25); 
INSERT INTO MenuItem VALUES (6, 3, 12, 5.50); 
INSERT INTO MenuItem VALUES (7, 3, 07, 12.50); 
INSERT INTO MenuItem VALUES (8, 3, 19, 13.50); 
INSERT INTO MenuItem VALUES (9, 5, 13, 6.00); 
INSERT INTO MenuItem VALUES (10, 5, 15, 15.00); 
INSERT INTO MenuItem VALUES (11, 5, 22, 14.00); 

INSERT INTO FoodOrder VALUES (0, 2, STR_TO_DATE('2024-03-01', '%Y-%m-%d'), '10:30');
INSERT INTO FoodOrder VALUES (1, 0, STR_TO_DATE('2024-03-02', '%Y-%m-%d'), '15:33');
INSERT INTO FoodOrder VALUES (2, 3, STR_TO_DATE('2024-03-01', '%Y-%m-%d'), '15:35');
INSERT INTO FoodOrder VALUES (3, 5, STR_TO_DATE('2024-03-03', '%Y-%m-%d'), '21:00');
INSERT INTO FoodOrder VALUES (4, 7, STR_TO_DATE('2024-03-01', '%Y-%m-%d'), '18:11');
INSERT INTO FoodOrder VALUES (5, 7, STR_TO_DATE('2024-03-04', '%Y-%m-%d'), '18:51');
INSERT INTO FoodOrder VALUES (6, 9, STR_TO_DATE('2024-03-01', '%Y-%m-%d'), '19:00');
INSERT INTO FoodOrder VALUES (7, 11, STR_TO_DATE('2024-03-05', '%Y-%m-%d'), '17:15');
INSERT INTO FoodOrder VALUES (8, 11, STR_TO_DATE('2024-04-01', '%Y-%m-%d'), '12:10');



EOFMYSQL
