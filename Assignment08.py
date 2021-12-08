# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# Anya Pryor, 12/7/21 ,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []

class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        Anya Pryor,12/6/21,Modified code to complete assignment 8
    """
    #pass
    # TODO: Add Code to the Product class
    def __init__(self, product_name, product_price):
        self.__PName = product_name
        self.__PPrice= product_price
    @property
    def product_name(self): #getter
        return str(__PName).title() #added title case
    @product_name.setter
    def product_name(self, value):
        if str(value).isNumeric == False:
            self.__PName=value
        else:
            raise Exception("Names cannot be numbers")
    @property
    def product_price(self):
        return float(__PPrice)
    @product_price.setter
    def product_price(self,value):
        if float(value).isNumeric == True:
            self.__PPrice=value
        else:
            raise Exception("Prices must be numbers")
    def listmethod(self):
        return [product_name, product_price]
# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
       Anya Pryor, 12/6/21,Modified code to complete assignment 8
    """
    #pass
    # TODO: Add Code to process data from a file
    def read_data_from_file(file_name, list_of_rows):
        file = open(file_name, "r")
        for row in list_of_rows:
            file.read(row)
        file.close()
        return list_of_rows
    # TODO: Add Code to process data to a file
    def write_data_to_file(file_name, list_of_rows):
        file = open(file_name, "w")
        for row in list_of_rows:
            file.write(row["Product Name"] + "," + row["Price"] + "/n")
        file.close()
        return list_of_rows
# Processing  ------------------------------------------------------------- #
    @staticmethod
    def add_data_to_list(product, price, list_of_rows):
        """ Adds data into a list of dictionary rows
        :param task (string) task to add:
        :param priority (string) priority to add:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        row = {"Product": str(Product.product_name).strip(), "Price": str(Product.product_price)}
        list_of_rows.append(row)
        return list_of_rows
# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    # TODO: Add docstring
    #pass
# Presentation (Input/Output)  -------------------------------------------- #
    """ Performs Input and Output tasks """

    @staticmethod
    def output_menu_tasks(): # TODO: Add code to show menu to user
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) See the current file
        2) Add a new Product and Price
        3) Save Data to File        
        4) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():     # TODO: Add code to get user's choice
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
        print()  # Add an extra line for looks
        return choice
    @staticmethod
    def output_current_prodcuts_in_list(list_of_rows):     # TODO: Add code to get user's choice
        """ Shows the current Tasks in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current products are: *******")
        for row in list_of_rows:
            print(row["Product"] + " (" + row["Price"] + ")")
        print("*******************************************")
        print()  # Add an extra line for looks
    @staticmethod
    def input_new_product_and_price():     # TODO: Add code to get product data from user
        """  Gather input from the user

        :parameter: task, priority
        :return: string, float
        """
        product = input("Enter a product: ")
        price = input("Enter a price ")
        return [product, price]

# Main Body of Script  ---------------------------------------------------- #
# Load data from file into a list of product objects when script starts
FileProcessor.read_data_from_file(file_name=strFileName, list_of_rows=lstOfProductObjects)
# Show user a menu of options
while (True):
# Get user's menu option choice
    IO.output_menu_tasks()
    choice=IO.input_menu_choice()
    # Show user current data in the list of product objects
    if choice =='1':
        IO.output_current_prodcuts_in_list(list_of_rows=lstOfProductObjects)
    # Let user add data to the list of product objects
    elif choice =='2':
        product, price=IO.input_new_product_and_price()
        list_of_rows = FileProcessor.add_data_to_list(product, price, lstOfProductObjects)
    # let user save current data to file and exit program
    elif choice =='3':
        list_of_rows = FileProcessor.write_data_to_file(file_name=strFileName, list_of_rows=lstOfProductObjects)
        print("All Saved!")
    elif choice =='4':
        print("goodbye")
        break


