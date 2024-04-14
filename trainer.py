import sys
from database import *
#from fitClub import welcome



############################################################################################

# TRAINER FUNCTIONS #

############################################################################################
# Trainer functions
def trainerFunctions(id):
    print("Welcome to your FitClub account! \n")
    print("Please select an option: \n")
    print("1. Manage Schedule")
    print("2. View member profiles")
    print("3. Log out")

   
    #check if option is valid
    while True:
        option = input("Enter your choice: ")
        if option in ["1", "2", "3"]:
            break
        print("Invalid choice. Please try again.")

    trainerChoice(option, id)

# Display trainer choices
def trainerChoice(option, id):
        if option == "1":
            manageSchedule(id)
        elif option == "2":
            viewMemberProfiles(id)
        elif option == "3":
            print("Logging out...")
            #welcome()
            sys.exit()
        else:
            print("Invalid choice. Please try again.")
            trainerFunctions(id)
############################################################################################
#manage schedule
def manageSchedule(id):
    while True:
        print("1. View schedule")
        print("2. Update availability")
        print("3. Return to main menu")

        # Prompt the user to enter an option
        option = input("Enter your choice: ")

        # Validate option input
        try:
            option = int(option)
            if option not in [1, 2, 3]:
                raise ValueError
        except ValueError:
            print("Invalid choice. Please try again.")
            continue

        # Process the option chosen by the user
        if option == 1:
            # View schedule
            viewTrainerSchedule(id)
        elif option == 2:
            # Update availability
            updateAvailability(id)
        elif option == 3:
            # Return to main menu
            trainerFunctions(id)
            break

def viewTrainerSchedule(id):
    print("\n")
    print("Here are your upcoming personal training sessions:\n")
    
    # Fetch personal training sessions
    cursor.execute("SELECT * FROM PersonalTrainerSessions WHERE TrainerID = %s", (id,))
    sessions = cursor.fetchall()

    # Display personal training sessions
    if sessions:
        for session in sessions:
            #get name of member
            cursor.execute("SELECT FirstName, LastName FROM Members WHERE MemberID = %s", (session[6],))
            member_name = cursor.fetchone()


            # if private session id is null then the room has not been assigned

            #printPersonalTrainingSession(session)
            print(f"Session ID: {session[0]}")
            print(f"Session Date: {session[1]}")
            print(f"Day of Week: {session[2]}")
            print(f"Start Time: {session[3]}")
            print(f"End Time: {session[4]}")
            print(f"Member: {member_name[0]} {member_name[1]}")
            print("\n")
    else:
        print("No personal training sessions available.")

    print("\nHere are your upcoming group training sessions:\n")
    
    # Fetch group training sessions
    cursor.execute("SELECT * FROM GroupTrainingSessions WHERE TrainerID = %s", (id,))
    group_sessions = cursor.fetchall()

    # Display group training sessions
    if group_sessions:
        for session in group_sessions:
            printGroupTrainingSession(session)
    else:
        print("No group training sessions available.")

def printPersonalTrainingSession(session):
    print(f"Session ID: {session[0]}")
    print(f"Session Date: {session[1]}")
    print(f"Day of Week: {session[2]}")
    print(f"Start Time: {session[3]}")
    print(f"End Time: {session[4]}")
    print("\n")

def printGroupTrainingSession(session):
    session_id = session[0]

    # Fetch member details for the group training session
    cursor.execute("SELECT MemberID FROM GroupTrainingSessionMembers WHERE SessionID = %s", (session_id,))
    member_ids = cursor.fetchall()
    members = []

    for member_id in member_ids:
        cursor.execute("SELECT FirstName, LastName FROM Members WHERE MemberID = %s", (member_id,))
        member_name = cursor.fetchone()
        members.append(f"{member_name[0]} {member_name[1]}")
    
    #get room name


    print(f"Session ID: {session[0]}")
    print(f"Session Date: {session[1]}")
    print(f"Day of Week: {session[2]}")
    print(f"Start Time: {session[3]}")
    print(f"End Time: {session[4]}")
    print(f"Members: {', '.join(members)}")
    print("\n")

def updateAvailability(id):
    print("Please choose one of the following options: \n")
    print("1. Add personal training session availability")
    print("2. Add group training session availability")

    # Prompt the user to enter an option
    option = input("Enter your choice: ")

    # Validate option input
    try:
        option = int(option)
        if option not in [1, 2]:
            raise ValueError
    except ValueError:
        print("Invalid choice. Please try again.")
        return manageSchedule(id)

    # Prompt the user to enter session details
    date = input("Date (YYYY-MM-DD): ")
    day = input("Day: ")
    start_time = input("Start time (HH:MM:SS): ")
    end_time = input("End time (HH:MM:SS): ")

    # Process the choice and update the availability
    if option == 1:
        # Check for existing personal training sessions
        cursor.execute("SELECT * FROM PersonalTrainerSessions WHERE SessionDate = %s AND DayOfWeek = %s AND StartTime = %s AND EndTime = %s", (date, day, start_time, end_time))
        existing_sessions = cursor.fetchall()

        if not existing_sessions:
            # Insert new personal training session availability
            cursor.execute("INSERT INTO PersonalTrainerSessions (SessionDate, DayOfWeek, StartTime, EndTime, TrainerID, MemberID) VALUES (%s, %s, %s, %s, %s, %s)", (date, day, start_time, end_time, id, None))
            connection.commit()
            print("Personal training session availability added successfully.")
        else:
            print("This session conflicts with an existing session. Please try again.")
    elif option == 2:
        # Check for existing group training sessions
        cursor.execute("SELECT * FROM GroupTrainingSessions WHERE SessionDate = %s AND DayOfWeek = %s AND StartTime = %s AND EndTime = %s", (date, day, start_time, end_time))
        existing_sessions = cursor.fetchall()

        if not existing_sessions:
            # Insert new group training session availability
            cursor.execute("INSERT INTO GroupTrainingSessions (SessionDate, DayOfWeek, StartTime, EndTime, TrainerID) VALUES (%s, %s, %s, %s, %s)", (date, day, start_time, end_time, id))
            
            connection.commit()
            print("Group training session availability added successfully.")
        else:
            print("This session conflicts with an existing session. Please try again.")

############################################################################################
#View member profiles
def viewMemberProfiles(id):
    print("Enter the name of the member you would like to view: ")
    fName = input("First Name: ")
    lName = input("Last Name: ")

    print("Searching for member...")
    cursor.execute("SELECT * FROM Members WHERE FirstName = %s AND LastName = %s", (fName, lName))
    rows = cursor.fetchall()
    print ("Here are the details of the member: \n")
    for row in rows:
        print("Member ID: ", row[0])
        print("First Name: ", row[1])
        print("Last Name: ", row[2])
        print("Username: ", row[3])
        print("\n")
    
    print("Would you like to return to the main menu?")
    print("1. Yes")
    print("2. No")
    option = input("Enter your choice: ")
    if option == "1":
        trainerFunctions(id)
    else:
        viewMemberProfiles(id)
############################################################################################
