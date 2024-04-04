#   DO:  more $HOME/.my.cnf to see your MySQL username and  password
#  CHANGE:  MYUSERNAME and MYMYSQLPASSWORD in the test section of
#  this program to your username and mysql password
#  RUN: ./runpython.sh

import mysql.connector
from tabulate import tabulate
from datetime import datetime



def open_database(hostname, user_name, mysql_pw, database_name):
    global conn
    conn = mysql.connector.connect(host=hostname,
                                   user=user_name,
                                   password=mysql_pw,
                                   database=database_name
                                   )
    global cursor
    cursor = conn.cursor()


def printFormat(result):
    header = []
    for cd in cursor.description:  # get headers
        header.append(cd[0])
    #print('')
    print('Query Result:')
    #print('')
    print(tabulate(result, headers=header))  # print results in table format

# select and display query


def executeSelect(query):
    cursor.execute(query)
    printFormat(cursor.fetchall())


def insert(table, values):
    query = "INSERT into " + table + " values (" + values + ")" + ';'
    cursor.execute(query)
    conn.commit()


def executeUpdate(query):  # use this function for delete and update
    cursor.execute(query)
    conn.commit()


def close_db():  # use this function to close db
    cursor.close()
    conn.close()

def menu_interface(): 
   print("---------------MENU----------------\n")
   print("1) Find all available menu items at a given restaurant\n")
   print("2) Order an available menu item from a particular restaurant\n")
   print("3) List all food orders for a particular restaurant\n")
   print("4) Cancel a food order\n")
   print("5) Add a new dish for a restaurant\n")
   print("6) Quit\n")
   print("------------------------------------\n")
   userInput = input("Please choose an option from the menu: ")
   return int(userInput)


def menu_option_1(): 
    #Prompt the user for a restaurant name and city. 
    #Find and list all menu items available from that restaurant location. 
    #Output the restaurant name once (echo the user input) and then list the dish name and price for each available menu item.
    restaurant = input("Please enter restaurant name: ")
    city = input("Please enter city name: ")
    print("The following are all the menu items available from that restaurant location: ")
    executeSelect('SELECT dishName FROM Restaurant JOIN MenuItem ON Restaurant.restaurantID = MenuItem.restaurantNo JOIN Dish ON MenuItem.dishNo = Dish.dishNo WHERE Restaurant.RestaurantName = "' + restaurant + '" AND Restaurant.City = "' + city + '";')
    
def get_last_order_number():
    cursor.execute("SELECT MAX(orderNo) FROM FoodOrder")
    last_order_no = cursor.fetchone()[0]
    return last_order_no if last_order_no is not None else 0

def menu_option_2():
    # Prompt the user for the dishName of the item that they want to order. 
    # If the dish is found, display the itemNo, restaurantName, city and price for all matches. 
    # Prompt the user for the itemNo for the MenuItem that they want to order. Add the itemNo, current time, and current date to the FoodOrder table.
    dish_name = input("Please enter the name of the dish you want to order: ")
    query = f'''
            SELECT MenuItem.itemNo, Restaurant.restaurantName, Restaurant.city, MenuItem.price
            FROM MenuItem
            INNER JOIN Dish ON MenuItem.dishNo = Dish.dishNo
            INNER JOIN Restaurant ON MenuItem.restaurantNo = Restaurant.restaurantID
            WHERE Dish.dishName = '{dish_name}';
            '''
    cursor.execute(query)
    results = cursor.fetchall()

    if results:
        print("Here are the available options:")
        print("Item No | Restaurant Name | City      | Price")
        print("--------------------------------------------")
        for result in results:
            print(f"{result[0]:<8} | {result[1]:<14} | {result[2]:<9} | ${result[3]:.2f}")

        item_no = input("Please enter the Item No of the MenuItem you want to order: ")
        date = datetime.today().strftime('%Y-%m-%d')
        time = datetime.now().strftime('%H:%M:%S')
        
        # Get the last order number and increment it
        last_order_no = get_last_order_number()
        new_order_no = last_order_no + 1

        # Insert the order with the generated order number
        insert_query = f'''
                        INSERT INTO FoodOrder (orderNo, itemNo, date, time)
                        VALUES ({new_order_no}, {item_no}, '{date}', '{time}');
                        '''
        cursor.execute(insert_query)
        conn.commit()
        print("Order successfully placed!")
    else:
        print("Sorry, the dish is not available.")


    

def menu_option_3(): 
    #Prompt the user for the restaurantName and city . 
    # If the restaurant is found, display all orders for that restaurant. 
    # Display the restaurantName once (echo the user input) and then display the dishName, price, date, and time for all orders for that restaurant.
    restaurant_name = input("Please enter the restaurant name: ")
    city = input("Please enter the city: ")

    # Check if the restaurant exists
    query_restaurant = f'''
                        SELECT restaurantID
                        FROM Restaurant
                        WHERE restaurantName = '{restaurant_name}' AND city = '{city}';
                        '''
    cursor.execute(query_restaurant)
    restaurant_result = cursor.fetchone()

    if restaurant_result:
        restaurant_id = restaurant_result[0]
        # Retrieve orders for the specified restaurant
        query_orders = f'''
                        SELECT FoodOrder.orderNo, Dish.dishName, MenuItem.price, FoodOrder.date, FoodOrder.time
                        FROM FoodOrder
                        INNER JOIN MenuItem ON FoodOrder.itemNo = MenuItem.itemNo
                        INNER JOIN Dish ON MenuItem.dishNo = Dish.dishNo
                        INNER JOIN Restaurant ON MenuItem.restaurantNo = Restaurant.restaurantID
                        WHERE Restaurant.restaurantID = {restaurant_id};
                        '''
        cursor.execute(query_orders)
        orders = cursor.fetchall()

        if orders:
            print("Here are all food orders for", restaurant_name, "in", city)
            print("Order No | Dish Name       | Price | Date       | Time")
            print("-------------------------------------------------------")
            for order in orders:
                print(f"{order[0]:<9} | {order[1]:<15} | ${order[2]:.2f} | {order[3]} | {order[4]}")
        else:
            print("No food orders found for", restaurant_name, "in", city)
    else:
        print("Restaurant not found in the specified city.")



def menu_option_4(): 
    # Display all food orders (orderNo, dishName, restaurantName, date, time). 
    # Prompt the user for the orderNo of the order that they wish to cancel. 
    # Remove that order from the FoodOrder table.
    cursor.execute('''
        SELECT FoodOrder.orderNo, Dish.dishName, Restaurant.restaurantName, FoodOrder.date, FoodOrder.time
        FROM FoodOrder
        INNER JOIN MenuItem ON FoodOrder.itemNo = MenuItem.itemNo
        INNER JOIN Dish ON MenuItem.dishNo = Dish.dishNo
        INNER JOIN Restaurant ON MenuItem.restaurantNo = Restaurant.restaurantID
        ORDER BY FoodOrder.orderNo
    ''')
    orders = cursor.fetchall()

    if orders:
        print("All food orders:")
        print("Order No | Dish Name       | Restaurant Name | Date       | Time")
        print("-------------------------------------------------------------------")
        for order in orders:
            print(f"{order[0]:<9} | {order[1]:<15} | {order[2]:<15} | {order[3]} | {order[4]}")

        order_no_to_cancel = input("Please enter the Order No of the order you wish to cancel: ")
        
        # Check if the order to cancel exists
        if any(order_no_to_cancel == str(order[0]) for order in orders):
            # Delete the order
            delete_query = f"DELETE FROM FoodOrder WHERE orderNo = {order_no_to_cancel}"
            cursor.execute(delete_query)
            conn.commit()
            print("Order successfully cancelled.")
        else:
            print("Invalid Order No. Please try again.")
    else:
        print("No food orders found.")


def menu_option_5(): 
    # Prompt the user for the restaurantName and city. 
    # If the restaurant is found, prompt for the name, type, and price of the the new dish. 
    # Assume that the dish is unique. Insert it into the Dish table. Insert it into the MenuItem table.
    restaurant_name = input("Please enter the restaurant name: ")
    city = input("Please enter the city: ")

    # Check if the restaurant exists
    query_restaurant = f'''
                        SELECT restaurantID
                        FROM Restaurant
                        WHERE restaurantName = '{restaurant_name}' AND city = '{city}';
                        '''
    cursor.execute(query_restaurant)
    restaurant_result = cursor.fetchone()

    if restaurant_result:
        # Get details of the new dish from the user
        dish_name = input("Please enter the name of the new dish: ")
        dish_type = input("Please enter the type of the new dish (ap, en, ds): ")
        price = input("Please enter the price of the new dish: ")

        # Retrieve the maximum dish number and increment it by 1
        cursor.execute("SELECT MAX(dishNo) FROM Dish")
        max_dish_no = cursor.fetchone()[0]
        new_dish_no = max_dish_no + 1

        # Insert the new dish into the Dish table
        insert_query_dish = f'''
                            INSERT INTO Dish (dishNo, dishName, type)
                            VALUES ({new_dish_no}, '{dish_name}', '{dish_type}');
                            '''
        cursor.execute(insert_query_dish)
        conn.commit()

        # Get the restaurant ID
        restaurant_id = restaurant_result[0]

        # Insert the new dish into the MenuItem table
        insert_query_menu_item = f'''
                                INSERT INTO MenuItem (restaurantNo, dishNo, price)
                                VALUES ({restaurant_id}, {new_dish_no}, {price});
                                '''
        cursor.execute(insert_query_menu_item)
        conn.commit()

        print("New dish added successfully!")
    else:
        print("Restaurant not found in the specified city.")


def main():
    mysql_username = 'amnak'  # please change to your username
    mysql_password = 'ooSh9Phu'  # please change to your MySQL password

    open_database('localhost', mysql_username, mysql_password, mysql_username)  # open database

    quit = False
    while quit == False:
         userInput = int(menu_interface())
         if userInput == 1:
            #1) Find all available menu items at a given restaurant
            menu_option_1()
         
         elif userInput == 2:
            #2) Order an available menu item from a particular restaurant
            menu_option_2()
         
         elif userInput == 3:
            #3) List all food orders for a particular restaurant
            menu_option_3()
         
         elif userInput == 4:
            #4) Cancel a food order
            menu_option_4()
         
         elif userInput == 5:
            #5) Add a new dish for a restaurant
            menu_option_5()
         
         elif userInput == 6:
            print("Quitting")
            quit = True
         else:
            print("Invalid option. Try again. ")

    close_db()  # close database



if __name__ == "__main__":
    main()



