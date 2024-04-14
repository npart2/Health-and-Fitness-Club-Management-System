from datetime import timedelta
import sys
from database import *
#from fitClub import welcome


############################################################################################
 
# ADMIN FUNCTIONS #

############################################################################################
# Admin functions
def adminFunctions(id):
    print("Welcome to your FitClub account! \n")
    print("Please select an option: \n")
    print("1. Manage room bookings")
    print("2. Manage equipment maintenance")
    print("3. Manage class schedules")
    print("4. Manage billing and payments")
    print("5. Log out")

    while True:
        option = input("Enter your choice: ")
        if option in ["1", "2", "3", "4", "5"]:
            break
        print("Invalid choice. Please try again.")

    adminChoice(option, id)


# Display admin choices
def adminChoice(option, id):
        if option == "1":
            manageRoomBookings(id)
        elif option == "2":
            manageEquipmentMaintenance(id)
        elif option == "3":
            manageClassSchedules(id)
        elif option == "4":
            manageBillingAndPayments(id)
        elif option == "5":
            print("Logging out...")
            #welcome()
            sys.exit()
        else:
            print("Invalid choice. Please try again.")
            adminFunctions(id)
############################################################################################
# Manage room bookings
def manageRoomBookings(id):
    print("1. Assign a session to a room")
    print("2. View room bookings")
    print("3. Return to main menu")

    option = input("Enter your choice: ")

    if option not in ["1", "2", "3"]:
        print("Invalid choice. Please try again.")
        manageRoomBookings(id)

    if option == "1":
        # Start a transaction
        print ("Do you want to assign a personal training session or a group training session to a room? \n")
        print("1. Personal")
        print("2. Group")
        choice = input("Enter your choice: ")
        if choice == "1":
            print("Private training sessions: \n")

            cursor.execute("SELECT * FROM PersonalTrainerSessions")
            sessions = cursor.fetchall()
            # for each session id , check if it is in the rooms table
            print ("Here are the Private training sessions that are not assigned to a room: \n")
            for session in sessions:
                cursor.execute("SELECT RoomID FROM Rooms WHERE PrivateSessionID = %s", (session[0],))
                room = cursor.fetchone()
                if not room:
                    
                    print(f"Session ID: {session[0]}")
                    print(f"Session Date: {session[1]}")
                    print(f"Day of Week: {session[2]}")
                    print(f"Start Time: {session[3]}")
                    print(f"End Time: {session[4]}")
                    print(f"Trainer ID: {session[5]}")
                    print("\n")

            session_id = input("Enter the ID of the session you would like to assign to a room: ")
            print ("Here are the available rooms: \n")
            #get all room ids that are not assigned to a session
            cursor.execute("SELECT RoomID FROM Rooms WHERE PrivateSessionID IS NULL")
            rooms = cursor.fetchall()
            for room in rooms:
                print(f"Room ID: {room[0]}")
                
                print("\n")
            
            room_id = input("Enter the ID of the room you would like to assign to the sesson: ")
            cursor.execute("UPDATE Rooms SET PrivateSessionID = %s WHERE RoomID = %s", (session_id, room_id))  
            connection.commit()
            print("Session assigned to room successfully.")
            manageRoomBookings(id)

        if choice == "2":
            print("Group training sessions: \n")
            cursor.execute("SELECT * FROM GroupTrainingSessions")
            sessions = cursor.fetchall()
            print ("Here are the Group training sessions that are not assigned to a room: \n")
            for session in sessions:
                cursor.execute("SELECT RoomID FROM Rooms WHERE GroupSessionID = %s", (session[0],))
                room = cursor.fetchone()
                if not room:
                    print(f"Session ID: {session[0]}")
                    print(f"Session Date: {session[1]}")
                    print(f"Day of Week: {session[2]}")
                    print(f"Start Time: {session[3]}")
                    print(f"End Time: {session[4]}")
                    print(f"Trainer ID: {session[5]}")
                    print("\n")
            session_id = input("Enter the ID of the session you would like to assign to a room: ")
            print ("Here are the available rooms: \n")
            cursor.execute("SELECT RoomID FROM Rooms WHERE GroupSessionID IS NULL")
            rooms = cursor.fetchall()
            for room in rooms:
                print(f"Room ID: {room[0]}")
               
                print("\n")
            room_id = input("Enter the ID of the room you would like to assign to the sesson: ")
            cursor.execute("UPDATE Rooms SET GroupSessionID = %s WHERE RoomID = %s", (session_id, room_id))  
            connection.commit()
            print("Session assigned to room successfully.")
            manageRoomBookings(id)
    if option == "2":
        print("Here are the personal trainer room bookings: \n")
        cursor.execute("SELECT * FROM Rooms WHERE PrivateSessionID IS NOT NULL")
        rooms = cursor.fetchall()
        for room in rooms:
            # get session info
            cursor.execute("SELECT * FROM PersonalTrainerSessions WHERE SessionID = %s", (room[4],))
            session = cursor.fetchone()

            #get equipment in the room
            cursor.execute("SELECT EquipmentName FROM Equipment WHERE RoomNumber = %s", (room[0],))
            equipment = cursor.fetchall()

            print(f"Room ID: {room[0]}")
            print(f"Room Name: {room[1]}")
            print(f"Room Capacity: {room[2]}")
            print(f"Session ID: {session[0]}")
            print(f"Session Date: {session[1]}")
            print(f"Day of Week: {session[2]}")
            print(f"Start Time: {session[3]}")
            print(f"End Time: {session[4]}")
            print(f"Trainer ID: {session[5]}")
            print(f"Equipment: {equipment[0]} ")

            print("\n")
        
        if not rooms:
            print("No room bookings found.")
            print ("\n")

        print("Here are the group training room bookings: \n")
        cursor.execute("SELECT * FROM Rooms WHERE GroupSessionID IS NOT NULL")
        rooms = cursor.fetchall()
        for room in rooms:
            # get session info
            cursor.execute("SELECT * FROM GroupTrainingSessions WHERE SessionID = %s", (room[3],))
            session = cursor.fetchone()

            #get equipment in the room
        
            cursor.execute("SELECT EquipmentName FROM Equipment WHERE RoomNumber = %s", (room[0],))
            equipment = cursor.fetchall()
            
            print(f"Room ID: {room[0]}")
            print(f"Room Name: {room[1]}")
            print(f"Room Capacity: {room[2]}")
            print(f"Session ID: {session[0]}")
            print(f"Session Date: {session[1]}")
            print(f"Day of Week: {session[2]}")
            print(f"Start Time: {session[3]}")
            print(f"End Time: {session[4]}")
            print(f"Trainer ID: {session[5]}")
            print(f"Equipment: {equipment[0]} ")
            print("\n")

        if not rooms:
            print("No room bookings found.")
            print ("\n")

        manageRoomBookings(id)

    if option == "3":
        print("Returning to main menu...")
        adminFunctions(id)

############################################################################################
# Manage equipment maintenance
def manageEquipmentMaintenance(id):
    #assign equipment id to a maintenance schedule in the maintenance table
    # Display menu options
    print("1. Maintain equipment")
    print("2. View maintenance schedule")
    print("3. Return to main menu")

    # Prompt user for an option and validate input
    try:
        option = int(input("Enter your choice: "))
        if option not in [1, 2, 3]:
            raise ValueError
    except ValueError:
        print("Invalid choice. Please try again.")
        return manageEquipmentMaintenance(id)

    # Maintain equipment option
    if option == 1:
        # Retrieve equipment that needs maintenance today
        print("Here are the equipment that need urgent maintenance:")
        #select all equipment with maintenance status 'Bad'
        cursor.execute("SELECT EquipmentID, EquipmentName, NextMaintenanceDate, MaintenanceStatus FROM Equipment WHERE MaintenanceStatus = 'Bad'")
        rows = cursor.fetchall()

        if rows:
            for row in rows:
                equipment_id, name, next_date, status = row
                print(f"Equipment ID: {equipment_id}, Equipment Name: {name}")
                print(f"Next Maintenance Date: {next_date}")
                print(f"Maintenance Status: {status}\n")

        print("Enter the ID of the equipment you want to maintain: ")
        equipment_id = input("Equipment ID: ")

        date1 = date.today()

        d1 = date1.strftime("%Y-%m-%d")

        

        #get date 1 month from now
        next_date = date1 + timedelta(days=30)
        d2 = next_date.strftime("%Y-%m-%d")

        # Update the maintenance status of the equipment to 'Good' and set last maintenance date to today and next matencne date to 1 month from now
        cursor.execute("UPDATE Equipment SET MaintenanceStatus = 'Good', LastMaintenanceDate = %s, NextMaintenanceDate = %s WHERE EquipmentID = %s", (d1, d2, equipment_id))
        #cursor.execute("UPDATE Equipment SET MaintenanceStatus = 'Good' WHERE EquipmentID = %s", (equipment_id,))
        connection.commit()
        print("Equipment maintenance completed successfully.")
       
        manageEquipmentMaintenance(id)

    # View maintenance schedule option
    if option == 2:
        # Retrieve equipment scheduled for maintenance soon
        print("Here is the eqipment maintenance schedule:")
        cursor.execute("SELECT * FROM Equipment")
        rows = cursor.fetchall()
        
        if rows:
            for row in rows:
                print(f"Equipment ID: {row[0]}")
                print(f"Equipment Name: {row[1]}")
                print(f"Equipment Description: {row[2]}")
                print(f"Equipment Quantity: {row[3]}")
                print(f"Room: {row[4]}")
                print(f"Last Maintenance Date: {row[5]}")
                print(f"Next Maintenance Date: {row[6]}")
                print(f"Maintenance Status: {row[7]}\n")
      

        # Call function recursively to display the menu again
        manageEquipmentMaintenance(id)

    # Return to main menu option
    if option == 3:
        print("Returning to main menu...")
        adminFunctions(id)
############################################################################################
# Manage class schedules
def manageClassSchedules(id):
    print("Please select an option:")
    print("1. Cancel a class")
    print("2. Return to main menu")

    try:
        option = int(input("Enter your choice: "))
        if option not in [1, 2]:
            raise ValueError
    except ValueError:
        print("Invalid choice. Please try again.")
        return manageClassSchedules(id)

    if option == 1:
        print("Do you want to cancel a personal trainer class or a group training class?")
        print("1. Personal")
        print("2. Group")
        try:
            choice = int(input("Enter your choice: "))
            if choice not in [1, 2]:
                raise ValueError
        except ValueError:
            print("Invalid choice. Please try again.")
            return manageClassSchedules(id)

        if choice == 1:
            print("Here are all of the personal training classes:\n")
            cursor.execute("SELECT * FROM PersonalTrainerSessions")
            rows = cursor.fetchall()
            if rows:
                for row in rows:
                    print(f"Session ID: {row[0]}")
                    print(f"Date: {row[1]}")
                    print(f"Day: {row[2]}")
                    print(f"Start Time: {row[3]}")
                    print(f"End Time: {row[4]}")
                    print(f"Trainer ID: {row[5]}")
                    print(f"Member ID: {row[6]}")
                    print("\n")
                
                classID = input("Enter the session ID of the class you would like to cancel: ")

                #check if it is assigned to a room
                cursor.execute("SELECT RoomID FROM Rooms WHERE PrivateSessionID = %s", (classID,))
                room = cursor.fetchone()
                if room:
                    #delete from rooms table
                    cursor.execute("UPDATE Rooms SET PrivateSessionID = NULL WHERE PrivateSessionID = %s", (classID,))
                    connection.commit()
                
                cursor.execute("DELETE FROM PersonalTrainerSessions WHERE SessionID = %s", (classID,))
                connection.commit()
                print("Class has been cancelled.")
            else:
                print("No personal training classes found.")
        ########################################################################################################
        else:
            print("Here are all of the group training classes:")
            cursor.execute("SELECT *  FROM GroupTrainingSessions")
            rows = cursor.fetchall()
            if rows:
                for row in rows:
                    print(f"Class ID: {row[0]}")
                    print(f"Date: {row[1]}")
                    print(f"Day: {row[2]}")
                    print(f"Start Time: {row[3]}")
                    print(f"End Time: {row[4]}")
                    print(f"Trainer ID: {row[5]}")
                    print("Members:")

                    #get list of memebrs in the class
                    cursor.execute("SELECT MemberID FROM GroupTrainingSessionMembers WHERE SessionID = %s", (row[0],))
                    members = cursor.fetchall()
                    for member in members:
                        print(f"Member ID: {member[0]}")
                    print("\n")
                
                classID = input("Enter the class ID of the class you would like to cancel: ")

                cursor.execute("SELECT RoomID FROM Rooms WHERE GroupSessionID = %s", (classID,))
                room = cursor.fetchone()
                if room:
                    cursor.execute("UPDATE Rooms SET GroupSessionID = NULL WHERE GroupSessionID = %s", (classID,))
                    connection.commit()

                #delete session id and members from group training session members table
                cursor.execute("DELETE FROM GroupTrainingSessionMembers WHERE SessionID = %s", (classID,))

                #delete from group training sessions table
                cursor.execute("DELETE FROM GroupTrainingSessions WHERE SessionID = %s", (classID,))
                
                connection.commit()
                print("Class has been cancelled.")
            else:
                print("No group training classes found.")
        
        return manageClassSchedules(id)
        
    if option == 2:
        print("Returning to main menu...")
        adminFunctions(id)

############################################################################################
# Manage billing and payments
def manageBillingAndPayments(id):
    print("Please select an option: \n")
    print("1. View billing and payments")
    print("2. Return to main menu")

    # Prompt the user to enter their choice
    option = input("Enter your choice: ")
    
    # Check if the option is either "1" or "2"
    if option not in ["1", "2"]:
        print("Invalid choice. Please try again.")
        return manageBillingAndPayments(id)

    # If the user chose to view billing and payments
    if option == "1":
        print("Here are all of the billing and payments for all members: \n")
        
        # Execute the query to fetch all rows from the Billing table
        cursor.execute("SELECT * FROM Billing")
        rows = cursor.fetchall()

        # Loop through each row and display the billing details
        for row in rows:
            print(f"Billing ID: {row[0]}")
            print(f"Member ID: {row[1]}")
            print(f"Amount: {row[2]}")
            print(f"Payment Status: {row[3]}")
            print("\n")

        # Return to the function to show the menu again
        return manageBillingAndPayments(id)

    # If the user chose to return to the main menu
    if option == "2":
        print("Returning to main menu...")
        # Call the function that handles returning to the main menu
        adminFunctions(id)
############################################################################################
        

        


        

       

    


