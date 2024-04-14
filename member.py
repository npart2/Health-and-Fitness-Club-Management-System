import sys
from database import *
#from fitClub import welcome


############################################################################################

# MEMBER FUNCTIONS #

############################################################################################
# Member functions
def memberFunctions(id):
    print("Welcome to your FitClub account! \n")
    print("Please select an option: \n")
    print("1. View your profile")
    print("2. View your dashboard")
    print("3. View your schedule")
    print("4. Log out")

    while True:
        option = input("Enter your choice: ")
        if option in ["1", "2", "3", "4"]:
            break
        print("Invalid choice. Please try again.")
    
    memberChoice(option, id)

def memberChoice(option, id):
    if option == "1":
        viewProfile(id)
    elif option == "2":
        viewDashboard(id)
    elif option == "3":
        viewSchedule(id)
    elif option == "4":
        print("Logging out...")
        #welcome()
        #exit program
        sys.exit()

############################################################################################
# Display profile member choices 
def viewProfile(id):
    print("Viewing profile...")
    print("Please select an option: \n")
    print("1. Update personal information")
    print("2. Update fitness goals")
    print("3. Update health metrics")
    print("4. Pay bill")
    print("5. Return to main menu")

    while True:
        option = input("Enter your choice: ")
        if option in ["1", "2", "3", "4", "5"]:
            break
        print("Invalid choice. Please try again.")

    viewProfileChoice(option, id)

def viewProfileChoice(option, id):
        if option == "1":
            updatePersonalInfo(id)
        elif option == "2":
            updateFitnessGoals(id)
        elif option == "3":
            updateHealthMetrics(id)
        elif option == "4":
            payBill(id)
        elif option == "5":
            print("Returning to main menu...")
            memberFunctions(id)
        else:
            print("Invalid choice. Please try again.")
            viewProfile(id)

############################################################################################
# Update personal information
def updatePersonalInfo(id):
    print("Here is your personal information: \n")
    # Get member info from database matching id
    cursor.execute("SELECT * FROM Members WHERE MemberID = %s", (id,))
    memberInfo = cursor.fetchone()
    
    if memberInfo:
        print(f"Member ID: {memberInfo[0]}")
        print(f"First Name: {memberInfo[1]}")
        print(f"Last Name: {memberInfo[2]}")
        print(f"Username: {memberInfo[3]}")
        print(f"Password: {memberInfo[4]}")
    else:
        print("No member found with the provided ID.")
        return

    print("Do you want to update your information? \n")
    print("1. Yes")
    print("2. No")
    choice = input("Enter your choice: ")

    if choice == "1":
        print("Please enter your new information: \n")
        newFirstName = input("Enter your first name: ")
        newLastName = input("Enter your last name: ")
        newUsername = input("Enter your username: ")
        newPassword = input("Enter your password: ")

        # Update member information in database
        cursor.execute("UPDATE Members SET FirstName = %s, LastName = %s, Username = %s, Password = %s WHERE MemberID = %s",
                       (newFirstName, newLastName, newUsername, newPassword, id))
        connection.commit()  # Commit the transaction

        # Verify the information has been updated
        cursor.execute("SELECT * FROM Members WHERE MemberID = %s", (id,))
        updatedInfo = cursor.fetchone()
        if (updatedInfo[1] == newFirstName and
            updatedInfo[2] == newLastName and
            updatedInfo[3] == newUsername and
            updatedInfo[4] == newPassword):
            print("Information updated successfully!")
            viewProfile(id)
        else:
            print("Information update failed. Please try again.")
            updatePersonalInfo(id)
    elif choice == "2":
        viewProfile(id)
    else:
        print("Invalid choice. Please try again.")
        updatePersonalInfo(id)

############################################################################################
# Update fitness goals
def updateFitnessGoals(id):
    print("Here are your fitness goals: \n")
    # Get fitness goals from the database for the specified member ID
    cursor.execute("SELECT * FROM Goals WHERE MemberID = %s", (id,))
    goals = cursor.fetchall()
    
    if goals:
        # Print each goal
        for goal in goals:
            print(f"Goal ID: {goal[0]}")
            print(f"Goal Name: {goal[1]}")
            print(f"Description: {goal[2]}")
            print(f"Start: {goal[3]}")
            print(f"End: {goal[4]}\n")
    else:
        print("You have no fitness goals. Please add some.")
    
    # Display options to the user
    print("Please select an option: \n")
    print("1. Add a new goal")
    print("2. Delete a goal")
    print("3. Return to main menu")
    
    option = input("Enter your choice: ")

    if option == "1":
        # Add a new goal
        goalName = input("Enter the name of your goal: ")
        goalDescription = input("Enter a description of your goal: ")
        goalStart = input("Enter the start date of your goal (YYYY-MM-DD): ")
        goalEnd = input("Enter the end date of your goal (YYYY-MM-DD): ")
        
        # Insert the new goal into the database
        cursor.execute("INSERT INTO Goals (GoalName, GoalDescription, StartDate, EndDate, MemberID) VALUES (%s, %s, %s, %s, %s)", (goalName, goalDescription, goalStart, goalEnd, id))
        connection.commit()  # Commit the transaction
        
        print("Goal added successfully!")
        # Return to the main menu
        viewProfile(id)
    elif option == "2":
        # Delete a goal
        goalID = input("Enter the ID of the goal you want to delete: ")
        cursor.execute("DELETE FROM Goals WHERE GoalID = %s AND MemberID = %s", (goalID, id))
        connection.commit()  # Commit the transaction
        
        # Check if the goal was successfully deleted
        cursor.execute("SELECT * FROM Goals WHERE GoalID = %s AND MemberID = %s", (goalID, id))
        remaining_goals = cursor.fetchall()
        
        if not remaining_goals:
            print("Goal deleted successfully!")
        else:
            print("Goal deletion failed. Please try again.")
        
        # Return to the main menu
        viewProfile(id)
    elif option == "3":
        viewProfile(id)
    else:
        print("Invalid choice. Please try again.")
        updateFitnessGoals(id)

############################################################################################
# Update health metrics
def updateHealthMetrics(id):
    print("Here are your health metrics: \n")
    
    # Fetch health metrics for the member
    cursor.execute("SELECT * FROM HealthMetrics WHERE MemberID = %s", (id,))
    healthMetrics = cursor.fetchall()
    
    if healthMetrics:
        # Display health metrics
        for healthMetric in healthMetrics:
            print(f"Weight (lb): {healthMetric[1]}")
            print(f"Height (cm): {healthMetric[2]}")
            print(f"Age: {healthMetric[3]}")
            print(f"BMI: {healthMetric[4]}\n")
    else:
        print("You have no health metrics. Please add some.")
    
    # Display options for the user
    print("Please select an option: \n")
    print("1. Update a health metric")
    print("2. Return to main menu")
    
    option = input("Enter your choice: ")

    if option not in ["1", "2"]:
        print("Invalid choice. Please try again.")
        updateHealthMetrics(id)
    
    
    # Update a health metric
    if option == "1":
        print("Please enter your new health metrics: \n")
        weight = float(input("Enter your new weight (lb): "))
        height = float(input("Enter your new height (cm): "))
        age = int(input("Enter your new age: "))
        # Calculate new BMI, avoid division by zero
        bmi = (weight / (height/2.54)**2) * 703
        
        # Update the health metric in the database
        cursor.execute("UPDATE HealthMetrics SET Weight = %s, Height = %s, Age = %s, BMI = %s WHERE MemberID = %s", (weight, height, age, bmi, id))

        #if no health metrics are found, insert new health metrics
        if not healthMetrics:
            cursor.execute("INSERT INTO HealthMetrics (Weight, Height, Age, BMI, MemberID) VALUES (%s, %s, %s, %s, %s)", (weight, height, age, bmi, id))

        
        connection.commit()  # Commit the transaction
        
        print("Health metric updated successfully!")
        viewProfile(id)
    
    # Return to main menu
    elif option == "2":
        viewProfile(id)
############################################################################################
# Pay bill
def payBill(id):
    print("Here is your bill: \n")
    cursor.execute("SELECT COUNT(*) FROM Billing")
    row_count = cursor.fetchone()[0]
    
    if row_count == 0:
        print("The Billing table is empty.")
        viewProfile(id)
    
    # Get the cost from the Billing table for the member with payment status unpaid
    cursor.execute("SELECT Cost FROM Billing WHERE MemberID = %s AND PaymentStatus = 'Unpaid'", (id,))
    cost = cursor.fetchone()
    
    if cost is None:
        print("You have no outstanding bill.")
        viewProfile(id)
    else:
        cost_value = cost[0]  # Cost is the first element of the tuple
        print(f"Cost: ${cost_value:.2f}")
        print("Status: unpaid\n")
        
        print("Do you want to pay your bill? \n")
        print("1. Yes")
        print("2. No")
        choice = input("Enter your choice: ")

        if choice == "1":
            # Update the billing table to set payment status to paid and cost to 0 for the member
            cursor.execute("UPDATE Billing SET Cost = 0, PaymentStatus = 'paid' WHERE MemberID = %s", (id,))
            connection.commit()  # Commit the transaction if applicable
            print("Bill paid successfully!")
            viewProfile(id)
        elif choice == "2":
            viewProfile(id)
        else:
            print("Invalid choice. Please try again.")
            payBill(id)


############################################################################################
#view dashboard
def viewDashboard(id):
    print("Viewing dashboard...")
    print("Please select an option: \n")
    print("1. View your exercise routines")
    print("2. View your fitness achievements")
    print("3. View your health statistics")
    print("4. Return to main menu")

    option = input("Enter your choice: ")

    # Validate the input
    if option not in ["1", "2", "3", "4"]:
        print("Invalid choice. Please try again.")
        viewDashboard(id)
    else:
        viewDashboardChoice(option, id)

def viewDashboardChoice(option, id):
    match option:
        case "1":
            viewExerciseRoutines(id)
        case "2":
            viewFitnessAchievements(id)
        case "3":
            viewHealthStatistics(id)
        case "4":
            print("Returning to main menu...")
            memberFunctions(id)
        case _:
            print("Invalid choice. Please try again.")
            viewDashboard(id)

############################################################################################
# View excersize routines
def viewExerciseRoutines(id):
    print("Here are your scheduled fitness sessions: \n")

    print("Personal training sessions: \n")
    # Get all personal training sessions for the member at id
    cursor.execute("SELECT * FROM PersonalTrainerSessions WHERE MemberID = %s", (id,))
    sessions = cursor.fetchall()

    if not sessions:
        print("You have no personal training sessions scheduled. Add some if you want.")
    else:
        for session in sessions:
            trainerID = session[5]

            # Get the name of the trainer for the session with trainerID
            cursor.execute("SELECT FirstName, LastName FROM Trainers WHERE TrainerID = %s", (trainerID,))
            trainer = cursor.fetchone()

            if trainer:
                trainer_name = f"{trainer[0]} {trainer[1]}"
            else:
                trainer_name = "Unknown Trainer"

            #get room number from rooms table
            cursor.execute("SELECT RoomID FROM Rooms WHERE PrivateSessionID = %s", (session[0],))
            room = cursor.fetchone()
            if not room:
                room = "Room not assigned yet"

            print(f"Session Date: {session[1]}")
            print(f"Day of Week: {session[2]}")
            print(f"Start Time: {session[3]}")
            print(f"End Time: {session[4]}")
            print(f"Trainer: {trainer_name}")
            print(f"Room: {room}")
            print("\n")

    print("Group training sessions: \n")
    # Get all group training sessions for the member at id
    cursor.execute("SELECT SessionID FROM GroupTrainingSessionMembers WHERE MemberID = %s", (id,))
    sessionIDs = cursor.fetchall()

    if not sessionIDs:
        print("You have no group training sessions scheduled. Add some if you want.")
    else:
        for sessionID in sessionIDs:
            cursor.execute("SELECT * FROM GroupTrainingSessions WHERE SessionID = %s", (sessionID,))
            sessions = cursor.fetchall()

            for session in sessions:
                trainerID = session[5]
                # Get the name of the trainer for the session with trainerID
                cursor.execute("SELECT FirstName, LastName FROM Trainers WHERE TrainerID = %s", (trainerID,))
                trainer = cursor.fetchone()

                if trainer:
                    trainer_name = f"{trainer[0]} {trainer[1]}"
                else:
                    trainer_name = "Unknown Trainer"
                
                cursor.execute("SELECT RoomID FROM Rooms WHERE GroupSessionID = %s", (session[0],))
                room = cursor.fetchone()

                #if room is not found, print out unknown room
                if not room:
                    room = "Room not assigned yet"

                print(f"Session Date: {session[1]}")
                print(f"Day of Week: {session[2]}")
                print(f"Start Time: {session[3]}")
                print(f"End Time: {session[4]}")
                print(f"Trainer: {trainer_name}")
                print(f"Room: {room}")
                print("\n")

    print("Are you done viewing your exercise routines? \n")
    print("1. Yes")
    print("2. No")
    choice = input("Enter your choice: ")

    if choice == "1":
        viewDashboard(id)
    else:
        viewExerciseRoutines(id)
############################################################################################
# View fitness achievements
def viewFitnessAchievements(id):
    print("Here are your fitness achievements:\n")
    
    # Get all goals for the member at id
    cursor.execute("SELECT GoalName, GoalDescription, StartDate, EndDate FROM Goals WHERE MemberID = %s", (id,))
    goals = cursor.fetchall()

    if not goals:
        print("You have no fitness achievements. Add some goals if you want.")
    else:
        # Get the current date as a date object
        current_date = date.today()

        # Iterate through goals and display their status
        for goal in goals:
            goal_name = goal[0]
            goal_description = goal[1]
            start_date = goal[2]
            end_date = goal[3]

            # Convert end date to a date object if it's a string
            if isinstance(end_date, str):
                end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d').date()

            print(f"Goal Name: {goal_name}")
            print(f"Description: {goal_description}")
            print(f"Start Date: {start_date}")
            print(f"End Date: {end_date}")

            # Check if the goal is completed
            if current_date > end_date:
                print("Congratulations! You have completed this goal.\n")
            else:
                print("You have not completed this goal yet. Keep working!\n")

    print("Are you done viewing your fitness achievements?\n")
    print("1. Yes")
    print("2. No")
    choice = input("Enter your choice: ")

    if choice == "1":
        viewDashboard(id)
    else:
        viewFitnessAchievements(id)

############################################################################################
# View health statistics
def viewHealthStatistics(id):
    print("Here are your health statistics:\n")

    # Get all health metrics for the member at id
    cursor.execute("SELECT * FROM HealthMetrics WHERE MemberID = %s", (id,))
    healthMetrics = cursor.fetchall()

    # Check if the member has no health metrics
    if not healthMetrics:
        print("You have no health metrics. Add some if you want.")
    else:
        # Loop through health metrics and provide information and feedback
        for healthMetric in healthMetrics:
            weight = healthMetric[1]
            height = healthMetric[2]
            age = healthMetric[3]
            bmi = healthMetric[4]

            print(f"Weight (lb): {weight}")
            print(f"Height (cm): {height}")
            print(f"Age: {age}")
            print(f"BMI: {bmi:.2f}")

            # Provide feedback based on BMI
            if bmi < 18.5:
                print("Your BMI indicates that you are underweight. Try to gain weight using a healthy diet and exercise plan.")
            elif 18.5 <= bmi < 24.9:
                print("Your BMI indicates that you are normal weight. Keep up the good work!")
            elif 25 <= bmi < 29.9:
                print("Your BMI indicates that you are overweight. Try to lose weight using a healthy diet and exercise plan.")
            else:  # bmi >= 30
                print("Your BMI indicates that you are obese. Consult with a doctor or try to lose weight using a healthy diet and exercise plan.")
            
            print("\n")

    print("Are you done viewing your health statistics?\n")
    print("1. Yes")
    print("2. No")

    # Validate user choice input
    choice = input("Enter your choice: ")
    if choice == "1":
        viewDashboard(id)
    elif choice == "2":
        viewHealthStatistics(id)
    else:
        print("Invalid choice. Please try again.")
        viewHealthStatistics(id)

############################################################################################
def viewSchedule(id):
    print("Viewing schedule...\n")
    print("Please select an option:\n")
    print("1. Schedule a personal training session")
    print("2. Schedule a group training session")
    print("3. Return to main menu")

    # Prompt user for input
    option = input("Enter your choice: ")

    # Validate the choice

    if option not in ["1", "2", "3"]:
        print("Invalid choice. Please try again.")
        viewSchedule(id)
    else:
        # Call the corresponding function based on the choice
        viewScheduleChoice(option, id)

def viewScheduleChoice(option, id):
    if option == "1":
        schedulePersonalTraining(id)
    elif option == "2":
        scheduleGroupTraining(id)
    elif option == "3":
        print("Returning to main menu...")
        memberFunctions(id)
############################################################################################
# Schedule personal training
def schedulePersonalTraining(id):
    
    # Display all available personal training sessions
    print("Here are all of the available personal training sessions: \n")
    cursor.execute("SELECT * FROM PersonalTrainerSessions WHERE MemberID IS NULL")
    sessions = cursor.fetchall()

    # Check if there are any available sessions
    if not sessions:
        print("No available personal training sessions at the moment.")
        viewSchedule(id)
        return
    
    # Display the available sessions
    for session in sessions:
        session_id = session[0]
        session_date = session[1]
        day_of_week = session[2]
        start_time = session[3]
        end_time = session[4]
        trainer_id = session[5]
        room_number = session[6]

        # Fetch the trainer's name
        cursor.execute("SELECT FirstName, LastName FROM Trainers WHERE TrainerID = %s", (trainer_id,))
        trainer = cursor.fetchone()
        trainer_name = f"{trainer[0]} {trainer[1]}"

        price = 100

        # Display session details
        print(f"Session ID: {session_id}")
        print(f"Session Date: {session_date}")
        print(f"Day of Week: {day_of_week}")
        print(f"Start Time: {start_time}")
        print(f"End Time: {end_time}")
        print(f"Trainer: {trainer_name}")
        print(f"Room Number: {room_number}")
        print(f"Cost: ${price}\n")

    # Prompt the user to enter a session ID to schedule
    session_id_input = input("Enter the ID of the session you would like to schedule: ")

    # Validate the entered session ID
    cursor.execute("SELECT * FROM PersonalTrainerSessions WHERE SessionID = %s AND MemberID IS NULL", (session_id_input,))
    session = cursor.fetchone()

    if not session:
        print("Invalid session ID. Please try again.")
        schedulePersonalTraining(id)
    
    else:

        # Schedule the session by updating the MemberID
        cursor.execute("UPDATE PersonalTrainerSessions SET MemberID = %s WHERE SessionID = %s", (id, session_id_input))
        

        # Update the billing table with the session cost
        cursor.execute("SELECT Cost FROM Billing WHERE MemberID = %s", (id,))
        billing_cost = cursor.fetchone()

        # If no existing billing cost is found, start with a cost of 0
        if billing_cost:
            current_cost = billing_cost[0]
        else:
            current_cost = 0

        # Calculate new cost and update the billing table
        new_cost = current_cost + price
        cursor.execute("UPDATE Billing SET Cost = %s, PaymentStatus = 'Unpaid' WHERE MemberID = %s", (new_cost, id))
        #if no billing cost is found, insert new cost
        if not billing_cost:
            cursor.execute("INSERT INTO Billing (MemberID, Cost, PaymentStatus) VALUES (%s, %s, 'Unpaid')", (id, new_cost))
        # Commit the changes to the database
        connection.commit()
        print("Session scheduled successfully!")
        print(f"New cost added to bill: ${price}")

        

    # Return to the schedule view
    viewSchedule(id)
    
############################################################################################
# Schedule group training
def scheduleGroupTraining(id):
    print("Here are all of the available group training sessions: \n")
    
    # Fetch all group training sessions from the database
    cursor.execute("SELECT * FROM GroupTrainingSessions")
    sessions = cursor.fetchall()

    
    for session in sessions:

        #check if member is already in the session, if they are skip the session
        cursor.execute("SELECT * FROM GroupTrainingSessionMembers WHERE SessionID = %s AND MemberID = %s", (session[0], id))
        member = cursor.fetchone()
        if member:
            continue

        else:

            # Extract details of the session
            session_id = session[0]
            session_date = session[1]
            day_of_week = session[2]
            start_time = session[3]
            end_time = session[4]
            trainer_id = session[5]
            
            # Fetch trainer's name
            cursor.execute("SELECT FirstName, LastName FROM Trainers WHERE TrainerID = %s", (trainer_id,))
            trainer = cursor.fetchone()
            trainer_name = f"{trainer[0]} {trainer[1]}" if trainer else "Unknown"
            
            price = 50  # Fixed price for group training sessions
            
            # Display session details
            print(f"Session ID: {session_id}")
            print(f"Session Date: {session_date}")
            print(f"Day of Week: {day_of_week}")
            print(f"Start Time: {start_time}")
            print(f"End Time: {end_time}")
            print(f"Trainer: {trainer_name}")
            print(f"Cost: ${price}\n")
    
    # Get the ID of the session the user wants to schedule
    session_id = input("Enter the ID of the session you would like to schedule: ")
    
    # Validate the session ID
    cursor.execute("SELECT * FROM GroupTrainingSessions WHERE SessionID = %s", (session_id,))
    session = cursor.fetchone()
    
    if not session:
        print("Invalid session ID. Please try again.")
        scheduleGroupTraining(id)
        return
    
    # Update the group session by adding the member ID to the session
    cursor.execute("INSERT INTO GroupTrainingSessionMembers (SessionID, MemberID) VALUES (%s, %s)", (session_id, id))
    print("Session scheduled successfully!")
    
    # Retrieve the current cost from the billing table
    cursor.execute("SELECT Cost FROM Billing WHERE MemberID = %s", (id,))
    billing_cost = cursor.fetchone()
    
    # Calculate the new cost
    current_cost = billing_cost[0] if billing_cost else 0
    new_cost = current_cost + price
    
    # Update the billing table with the new cost and set the payment status to 'unpaid'
    cursor.execute("UPDATE Billing SET Cost = %s, PaymentStatus = 'Unpaid' WHERE MemberID = %s", (new_cost, id))

    #if no billing cost is found, insert new cost
    if not billing_cost:
        cursor.execute("INSERT INTO Billing (MemberID, Cost, PaymentStatus) VALUES (%s, %s, 'Unpaid')", (id, new_cost))
    
    # Commit the transaction to save changes to the database
    connection.commit()
    
    print(f"Cost added to bill: ${price}")
    
    # Continue to view the schedule
    viewSchedule(id)