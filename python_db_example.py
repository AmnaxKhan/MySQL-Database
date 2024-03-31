#   DO:  more $HOME/.my.cnf to see your MySQL username and  password
#  CHANGE:  MYUSERNAME and MYMYSQLPASSWORD in the test section of
#  this program to your username and mysql password
#  RUN: ./runpython.sh

import mysql.connector
from tabulate import tabulate


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
    print('')
    print('Query Result:')
    print('')
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
   print("6. Quit\n")
   print("------------------------------------\n")
   userInput = input("Please choose an option from the menu: ")
   return int(userInput)


def menu_option_1(): 
    #Prompt the user for a restaurant name and city. 
    #Find and list all menu items available from that restaurant location. 
    #Output the restaurant name once (echo the user input) and then list the dish name and price for each available menu item.
    pass

def menu_option_2(): 
    #Prompt the user for the dishName of the item that they want to order. 
    # If the dish is found, display the itemNo, restaurantName, city and price for all matches. 
    # Prompt the user for the itemNo for the MenuItem that they want to order. 
    # Add the itemNo, current time, and current date to the FoodOrder table.
    pass

def menu_option_3(): 
    #Prompt the user for the restaurantName and city . 
    # If the restaurant is found, display all orders for that restaurant. 
    # Display the restaurantName once (echo the user input) and then display the dishName, price, date, and time for all orders for that restaurant.
    pass

def menu_option_4(): 
    #Display all food orders (orderNo, dishName, restaurantName, date, time). 
    # Prompt the user for the orderNo of the order that they wish to cancel. 
    # Remove that order from the FoodOrder table.
    pass

def menu_option_5(): 
    # Prompt the user for the restaurantName and city. 
    # If the restaurant is found, prompt for the name, type, and price of the the new dish. 
    # Assume that the dish is unique. Insert it into the Dish table. Insert it into the MenuItem table.
    pass

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

# print(' ')
# print('Testing select: ')
# print('=======================================')
# executeSelect('SELECT * FROM Restaurant')

# print(' ')
# print('\nTesting insert of dept MATH:')
# print('=======================================')
# insert("DEPT", "'MATH', 'Mathematics', 309, 'SCEN'")
# executeSelect('SELECT * FROM DEPT WHERE DEPT_CODE = "MATH";')

# print(' ')
# print('\nTesting delete of dept MATH:')
# print('=======================================')
# executeUpdate('DELETE FROM DEPT WHERE DEPT_CODE = "MATH";')
# executeSelect('SELECT * FROM DEPT WHERE DEPT_CODE = "MATH";')

# print(' ')
# print('\nTesting update of professor name :')
# print('=======================================')
# executeSelect("SELECT * FROM PROFESSOR WHERE PROF_ID = 123456;")
# executeUpdate("Update PROFESSOR set PROF_NAME = 'Susan Dyer' WHERE PROF_ID = 123456;")
# executeSelect("SELECT * FROM PROFESSOR WHERE PROF_ID = 123456;")



