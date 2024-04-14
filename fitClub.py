
'''
from datetime import date, datetime
import psycopg2

from member import *



connection = psycopg2.connect(
    host="localhost",
    database="FitClub",
    user="postgres",
    password="Natuna14" #update password

)

cursor = connection.cursor()
'''

from member import *
from trainer import *
from admin import *


############################################################################################
def welcome():
    print("Welcome to FitClub! \n")
    print("Please select an option: \n")
    print("1. Register a new member")
    print("2. Login as a member")
    print("3. Login as a trainer")
    print("4. Login as an admin")
    print ("\n")

   
    option = input("Enter your choice: ")
    if option not in ["1", "2", "3", "4"]:
        print("Invalid choice. Please try again.")
        welcome()
    
    

    choice(option)
        

def choice(choice):
    match choice:
        case "1":
            register()
        case "2":
            memberLogin()
        case "3":
            trainerLogin()
        case "4":
            adminLogin()
        case _:
            print("Invalid choice. Please try again.")
            welcome()

############################################################################################
#Register as a new member
def register():
    print("Please enter the following details to register as a new FitClub member: \n")
    fName = input("First Name: ")
    lName = input("Last Name: ")
    userName = input("Username: ")
    password = input("Password: ")


    
    #insert data into Members table
    cursor.execute("INSERT INTO Members (FirstName, LastName, Username, Password) VALUES (%s, %s, %s, %s)", (fName, lName, userName, password))
    connection.commit()

    #check if data has been inserted
    cursor.execute("SELECT MemberID FROM Members WHERE Username = %s AND Password = %s", (userName, password))
    row = cursor.fetchone()

    if row:
        print(f"Registration successful! Welcome to FitClub {userName}!")
        id = row[0]  # Retrieve MemberID from the fetched row
        # Proceed to member functions using the retrieved memberID
        memberFunctions(id)
    else:
        print("Registration failed. Please try again.")
        register()


############################################################################################
# Login as a returning member 
def memberLogin():
    print("Please enter your member login details: \n")
    userName = input("Username: ")
    password = input("Password: ")

    # Check if username and password match
    cursor.execute("SELECT MemberID FROM Members WHERE Username = %s AND Password = %s", (userName, password))
    result = cursor.fetchone()

    if result:
        # Member login successful
        print(f"Member login successful! Welcome back, {userName}!")
        id = result[0]  # Retrieve MemberID from the fetched tuple
        memberFunctions(id)
    else:
        # Invalid username or password
        print("Invalid username or password. Please try again.")
        # Use a while loop instead of recursion to avoid recursion limit issues
        while True:
            memberLogin()

############################################################################################
# Login as a returning trainer
def trainerLogin():
    print("Please enter your trainer login details: \n")
    userName = input("Username: ")
    password = input("Password: ")

    # Check if username and password match
    cursor.execute("SELECT TrainerID FROM Trainers WHERE Username = %s AND Password = %s", (userName, password))
    row = cursor.fetchone()

    if row:
        # Trainer login successful
        print(f"Trainer login successful! Welcome back, {userName}!")
        id = row[0]  # Retrieve TrainerID from the fetched tuple
        trainerFunctions(id)
    else:
        # Invalid username or password
        print("Invalid username or password. Please try again.")
        # Use a loop instead of recursion to allow the user to try again
        while True:
            trainerLogin()

############################################################################################
# Login as a returning admin
def adminLogin():
    print("Please enter your admin login details: \n")
    userName = input("Username: ")
    password = input("Password: ")

    # Check if username and password match
    cursor.execute("SELECT AdminID FROM Admins WHERE Username = %s AND Password = %s", (userName, password))
    row = cursor.fetchone()
    
    if row:
        # Admin login successful
        print(f"Admin login successful! Welcome back, {userName}!")
        id = row[0]  # Retrieve AdminID from the fetched tuple
        adminFunctions(id)
    else:
        # Invalid username or password
        print("Invalid username or password. Please try again.")
        # Use a loop to allow the user to try again
        while True:
            adminLogin()

############################################################################################


welcome() # Start the program by displaying the welcome screen

# end of program
print("Thank you for using FitClub. Goodbye!\n")
connection.commit()
connection.close()


        


        

       

    


