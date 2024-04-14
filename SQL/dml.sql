CREATE TABLE Members (
    MemberID SERIAL PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Username VARCHAR(50) NOT NULL,
    Password VARCHAR(50) NOT NULL
    

);

INSERT INTO Members (FirstName, LastName, Username, Password) VALUES ('John', 'Doe', 'johndoe', 'password');

CREATE TABLE Trainers (
    TrainerID SERIAL PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Username VARCHAR(50) NOT NULL,
    Password VARCHAR(50) NOT NULL
    
);

INSERT INTO Trainers (FirstName, LastName, Username, Password) VALUES ('Jane', 'Smith', 'janesmith', 'password');


CREATE TABLE Admins (
    AdminID SERIAL PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Username VARCHAR(50) NOT NULL,
    Password VARCHAR(50) NOT NULL
    
);

INSERT INTO Admins (FirstName, LastName, Username, Password) VALUES ('Admin', 'Admin', 'admin', 'password');

CREATE TABLE Goals (
    GoalID SERIAL PRIMARY KEY,
    GoalName VARCHAR(50) NOT NULL,
    GoalDescription VARCHAR(50) NOT NULL,
    StartDate DATE NOT NULL,
    EndDate DATE NOT NULL,
    MemberID INT NOT NULL REFERENCES Members(MemberID)
);

INSERT INTO Goals (GoalName, GoalDescription, StartDate, EndDate, MemberID) VALUES ('Weight Loss', 'Lose 10 pounds', '2021-01-01', '2021-02-01', 1);


CREATE TABLE HealthMetrics (
    HealthMetricID SERIAL PRIMARY KEY,
    Weight INT NOT NULL,
    Height INT NOT NULL,
    Age INT NOT NULL,
    BMI FLOAT NOT NULL,
    MemberID INT NOT NULL REFERENCES Members(MemberID)
);

INSERT INTO HealthMetrics (Weight, Height, Age, BMI, MemberID) VALUES (150, 170, 30, 21.4, 1);

CREATE TABLE PersonalTrainerSessions (
    SessionID SERIAL PRIMARY KEY,
    SessionDate DATE NOT NULL,
    DayOfWeek VARCHAR(50) NOT NULL,
    StartTime TIME NOT NULL,
    EndTime TIME NOT NULL,
    TrainerID INT NOT NULL REFERENCES Trainers(TrainerID),
    MemberID INT REFERENCES Members(MemberID)
    
   
);

INSERT INTO PersonalTrainerSessions (SessionDate, DayOfWeek, StartTime, EndTime, TrainerID, MemberID) VALUES ('2021-01-01', 'Monday', '10:00:00', '11:00:00', 1, 1);
INSERT INTO PersonalTrainerSessions (SessionDate, DayOfWeek, StartTime, EndTime, TrainerID, MemberID) VALUES ('2021-01-02', 'Tuesday', '12:00:00', '2:00:00', 1, NULL);

CREATE TABLE GroupTrainingSessions (
    SessionID SERIAL PRIMARY KEY,
    SessionDate DATE NOT NULL,
    DayOfWeek VARCHAR(50) NOT NULL,
    StartTime TIME NOT NULL,
    EndTime TIME NOT NULL,
    TrainerID INT NOT NULL REFERENCES Trainers(TrainerID)
    
    
    
);

INSERT INTO GroupTrainingSessions (SessionDate, DayOfWeek, StartTime, EndTime, TrainerID) VALUES ('2021-01-01', 'Wednesday', '1:00:00', '3:00:00', 1);

CREATE TABLE GroupTrainingSessionMembers (
    
    SessionID INT NOT NULL REFERENCES GroupTrainingSessions(SessionID),
    MemberID INT NOT NULL REFERENCES Members(MemberID)
    
);

INSERT INTO GroupTrainingSessionMembers (SessionID, MemberID) VALUES (1, 1);





CREATE TABLE TrainerAvailability (
    sessionID SERIAL PRIMARY KEY,
    SessionDate DATE,
    DayOfWeek VARCHAR(50),
    StartTime TIME,
    EndTime TIME,
    TrainerID INT NOT NULL REFERENCES Trainers(TrainerID)

);

INSERT INTO TrainerAvailability (SessionDate, DayOfWeek, StartTime, EndTime, TrainerID) VALUES ('2021-01-01', 'Wednesday', '4:00:00', '5:00:00', 1);

CREATE TABLE Rooms (
    RoomID SERIAL PRIMARY KEY,
    RoomName VARCHAR(50) NOT NULL,
    RoomCapacity INT NOT NULL,
    SessionID INT REFERENCES GroupTrainingSessions(SessionID)

   
);

INSERT INTO Rooms (RoomName, RoomCapacity, SessionID) VALUES ('Room 1', 5, NULL);
INSERT INTO Rooms (RoomName, RoomCapacity, SessionID) VALUES ('Room 2', 20, NULL);
INSERT INTO Rooms (RoomName, RoomCapacity, SessionID) VALUES ('Room 3', 30, NULL);

CREATE TABLE Equipment (
    EquipmentID SERIAL PRIMARY KEY,
    EquipmentName VARCHAR(50) NOT NULL,
    EquipmentDescription VARCHAR(50) NOT NULL,
    EquipmentQuantity INT NOT NULL,
    RoomNumber INT NOT NULL REFERENCES Rooms(RoomID),
    LastMaintenanceDate DATE NOT NULL,
    NextMaintenanceDate DATE NOT NULL,
    MaintenanceStatus VARCHAR(50) NOT NULL
);

INSERT INTO Equipment (EquipmentName, EquipmentDescription, EquipmentQuantity, RoomNumber, LastMaintenanceDate, NextMaintenanceDate, MaintenanceStatus) VALUES ('Treadmill', 'Cardio equipment', 5, 1, '2021-01-01', '2021-02-01', 'Good');
INSERT INTO Equipment (EquipmentName, EquipmentDescription, EquipmentQuantity, RoomNumber, LastMaintenanceDate, NextMaintenanceDate, MaintenanceStatus) VALUES ('Dumbbells', 'Strength equipment', 10, 2, '2021-01-01', '2021-02-01', 'Good');
INSERT INTO Equipment (EquipmentName, EquipmentDescription, EquipmentQuantity, RoomNumber, LastMaintenanceDate, NextMaintenanceDate, MaintenanceStatus) VALUES ('Yoga Mats', 'Yoga equipment', 15, 3, '2021-01-01', '2021-02-01', 'Good');

CREATE TABLE Billing (
    BillingID SERIAL PRIMARY KEY,
    MemberID INT NOT NULL REFERENCES Members(MemberID),
    Cost INT NOT NULL,
    PaymentStatus VARCHAR(50) NOT NULL
);

INSERT INTO Billing (MemberID, Cost, PaymentStatus) VALUES (1, 100, 'Unpaid');


INSERT INTO Members (FirstName, LastName, Username, Password) VALUES ('John', 'Doe', 'johndoe', 'password');

INSERT INTO Trainers (FirstName, LastName, Username, Password) VALUES ('Jane', 'Smith', 'janesmith', 'password');
INSERT INTO Trainers (FirstName, LastName, Username, Password) VALUES ('John', 'Smith', 'johnsmith', 'password');

INSERT INTO Admins (FirstName, LastName, Username, Password) VALUES ('Admin', 'Admin', 'admin', 'password');


INSERT INTO Goals (GoalName, GoalDescription, StartDate, EndDate, MemberID) VALUES ('Weight Loss', 'Lose 10 pounds', '2024-01-01', '2024-02-01', 1);

INSERT INTO HealthMetrics (Weight, Height, Age, BMI, MemberID) VALUES (150, 170, 30, 21.4, 1);

INSERT INTO PersonalTrainerSessions (SessionDate, DayOfWeek, StartTime, EndTime, TrainerID, MemberID) VALUES ('2024-01-01', 'Monday', '10:00:00', '11:00:00', 1, NULL);



INSERT INTO GroupTrainingSessions (SessionDate, DayOfWeek, StartTime, EndTime, TrainerID) VALUES ('2021-01-01', 'Wednesday', '1:00:00', '3:00:00', 1);

INSERT INTO GroupTrainingSessionMembers (SessionID, MemberID) VALUES (1, 1);

INSERT INTO Rooms (RoomName, RoomCapacity, PrivateSessionID, GroupSessionID) VALUES ('Room 1', 5, NULL);
INSERT INTO Rooms (RoomName, RoomCapacity, PrivateSessionID, GroupSessionID) VALUES ('Room 2', 20, NULL);
INSERT INTO Rooms (RoomName, RoomCapacity, PrivateSessionID, GroupSessionID) VALUES ('Room 3', 2, NULL);
INSERT INTO Rooms (RoomName, RoomCapacity, PrivateSessionID, GroupSessionID) VALUES ('Room 4', 10, NULL);
INSERT INTO Rooms (RoomName, RoomCapacity, PrivateSessionID, GroupSessionID) VALUES ('Room 5', 15, NULL);
INSERT INTO Rooms (RoomName, RoomCapacity, PrivateSessionID, GroupSessionID) VALUES ('Room 6', 20, NULL);
INSERT INTO Rooms (RoomName, RoomCapacity, PrivateSessionID, GroupSessionID) VALUES ('Room 7', 35, NULL);
INSERT INTO Rooms (RoomName, RoomCapacity, PrivateSessionID, GroupSessionID) VALUES ('Room 8', 15, NULL);
INSERT INTO Rooms (RoomName, RoomCapacity, PrivateSessionID, GroupSessionID) VALUES ('Room 9', 10, NULL);
INSERT INTO Rooms (RoomName, RoomCapacity, PrivateSessionID, GroupSessionID) VALUES ('Room 10', 3, NULL);

INSERT INTO Equipment (EquipmentName, EquipmentDescription, EquipmentQuantity, RoomNumber, LastMaintenanceDate, NextMaintenanceDate, MaintenanceStatus) VALUES ('Treadmill', 'Cardio equipment', 5, 1, '2023-01-01', '2025-02-01', 'Good');
INSERT INTO Equipment (EquipmentName, EquipmentDescription, EquipmentQuantity, RoomNumber, LastMaintenanceDate, NextMaintenanceDate, MaintenanceStatus) VALUES ('Dumbbells', 'Strength equipment', 10, 2, '2023-01-01', '2024-02-01', 'Bad');
INSERT INTO Equipment (EquipmentName, EquipmentDescription, EquipmentQuantity, RoomNumber, LastMaintenanceDate, NextMaintenanceDate, MaintenanceStatus) VALUES ('Yoga Mats', 'Yoga equipment', 15, 3, '2024-01-01', '2024-02-01', 'Good');
INSERT INTO Equipment (EquipmentName, EquipmentDescription, EquipmentQuantity, RoomNumber, LastMaintenanceDate, NextMaintenanceDate, MaintenanceStatus) VALUES ('Bench Press', 'Strength equipment', 5, 4, '2024-01-01', '2024-02-01', 'Bad');
INSERT INTO Equipment (EquipmentName, EquipmentDescription, EquipmentQuantity, RoomNumber, LastMaintenanceDate, NextMaintenanceDate, MaintenanceStatus) VALUES ('Elliptical', 'Cardio equipment', 5, 5, '2023-01-01', '2024-02-01', 'Bad');
INSERT INTO Equipment (EquipmentName, EquipmentDescription, EquipmentQuantity, RoomNumber, LastMaintenanceDate, NextMaintenanceDate, MaintenanceStatus) VALUES ('Yoga Blocks', 'Yoga equipment', 15, 6, '2024-01-01', '2024-02-01', 'Good');
INSERT INTO Equipment (EquipmentName, EquipmentDescription, EquipmentQuantity, RoomNumber, LastMaintenanceDate, NextMaintenanceDate, MaintenanceStatus) VALUES ('Squat Rack', 'Strength equipment', 5, 7, '2023-01-01', '2024-02-01', 'Good');
INSERT INTO Equipment (EquipmentName, EquipmentDescription, EquipmentQuantity, RoomNumber, LastMaintenanceDate, NextMaintenanceDate, MaintenanceStatus) VALUES ('Rowing Machine', 'Cardio equipment', 5, 8, '2022-01-01', '2024-02-01', 'Good');
INSERT INTO Equipment (EquipmentName, EquipmentDescription, EquipmentQuantity, RoomNumber, LastMaintenanceDate, NextMaintenanceDate, MaintenanceStatus) VALUES ('Yoga Straps', 'Yoga equipment', 15, 9, '2024-01-01', '2024-02-01', 'Good');
INSERT INTO Equipment (EquipmentName, EquipmentDescription, EquipmentQuantity, RoomNumber, LastMaintenanceDate, NextMaintenanceDate, MaintenanceStatus) VALUES ('Leg Press', 'Strength equipment', 5, 10, '2024-01-01', '2024-02-01', 'Good');









INSERT INTO Members (FirstName, LastName, Username, Password) VALUES ('John', 'Doe', 'johndoe', 'password');

INSERT INTO Trainers (FirstName, LastName, Username, Password) VALUES ('Jane', 'Smith', 'janesmith', 'password');
INSERT INTO Trainers (FirstName, LastName, Username, Password) VALUES ('John', 'Smith', 'johnsmith', 'password');

INSERT INTO Admins (FirstName, LastName, Username, Password) VALUES ('Admin', 'Admin', 'admin', 'password');


INSERT INTO Goals (GoalName, GoalDescription, StartDate, EndDate, MemberID) VALUES ('Weight Loss', 'Lose 10 pounds', '2024-01-01', '2024-02-01', 1);

INSERT INTO HealthMetrics (Weight, Height, Age, BMI, MemberID) VALUES (150, 170, 30, 21.4, 1);

INSERT INTO PersonalTrainerSessions (SessionDate, DayOfWeek, StartTime, EndTime, TrainerID, MemberID) VALUES ('2024-01-01', 'Monday', '10:00:00', '11:00:00', 1, NULL);



INSERT INTO GroupTrainingSessions (SessionDate, DayOfWeek, StartTime, EndTime, TrainerID) VALUES ('2021-01-01', 'Wednesday', '1:00:00', '3:00:00', 1);

INSERT INTO GroupTrainingSessionMembers (SessionID, MemberID) VALUES (1, 1);

INSERT INTO Rooms (RoomName, RoomCapacity, PrivateSessionID, GroupSessionID) VALUES ('Room 1', 5, NULL, NULL);
INSERT INTO Rooms (RoomName, RoomCapacity, PrivateSessionID, GroupSessionID) VALUES ('Room 2', 20, NULL, NULL);
INSERT INTO Rooms (RoomName, RoomCapacity, PrivateSessionID, GroupSessionID) VALUES ('Room 3', 2, NULL, NULL);
INSERT INTO Rooms (RoomName, RoomCapacity, PrivateSessionID, GroupSessionID) VALUES ('Room 4', 10, NULL, NULL);
INSERT INTO Rooms (RoomName, RoomCapacity, PrivateSessionID, GroupSessionID) VALUES ('Room 5', 15, NULL, NULL);
INSERT INTO Rooms (RoomName, RoomCapacity, PrivateSessionID, GroupSessionID) VALUES ('Room 6', 20, NULL, NULL);
INSERT INTO Rooms (RoomName, RoomCapacity, PrivateSessionID, GroupSessionID) VALUES ('Room 7', 35, NULL, NULL);
INSERT INTO Rooms (RoomName, RoomCapacity, PrivateSessionID, GroupSessionID) VALUES ('Room 8', 15, NULL, NULL);
INSERT INTO Rooms (RoomName, RoomCapacity, PrivateSessionID, GroupSessionID) VALUES ('Room 9', 10, NULL, NULL);
INSERT INTO Rooms (RoomName, RoomCapacity, PrivateSessionID, GroupSessionID) VALUES ('Room 10', 3, NULL, NULL);

INSERT INTO Equipment (EquipmentName, EquipmentDescription, EquipmentQuantity, RoomNumber, LastMaintenanceDate, NextMaintenanceDate, MaintenanceStatus) VALUES ('Treadmill', 'Cardio equipment', 5, 1, '2023-01-01', '2025-02-01', 'Good');
INSERT INTO Equipment (EquipmentName, EquipmentDescription, EquipmentQuantity, RoomNumber, LastMaintenanceDate, NextMaintenanceDate, MaintenanceStatus) VALUES ('Dumbbells', 'Strength equipment', 10, 2, '2023-01-01', '2024-02-01', 'Bad');
INSERT INTO Equipment (EquipmentName, EquipmentDescription, EquipmentQuantity, RoomNumber, LastMaintenanceDate, NextMaintenanceDate, MaintenanceStatus) VALUES ('Yoga Mats', 'Yoga equipment', 15, 3, '2024-01-01', '2024-02-01', 'Good');
INSERT INTO Equipment (EquipmentName, EquipmentDescription, EquipmentQuantity, RoomNumber, LastMaintenanceDate, NextMaintenanceDate, MaintenanceStatus) VALUES ('Bench Press', 'Strength equipment', 5, 4, '2024-01-01', '2024-02-01', 'Bad');
INSERT INTO Equipment (EquipmentName, EquipmentDescription, EquipmentQuantity, RoomNumber, LastMaintenanceDate, NextMaintenanceDate, MaintenanceStatus) VALUES ('Elliptical', 'Cardio equipment', 5, 5, '2023-01-01', '2024-02-01', 'Bad');
INSERT INTO Equipment (EquipmentName, EquipmentDescription, EquipmentQuantity, RoomNumber, LastMaintenanceDate, NextMaintenanceDate, MaintenanceStatus) VALUES ('Yoga Blocks', 'Yoga equipment', 15, 6, '2024-01-01', '2024-02-01', 'Good');
INSERT INTO Equipment (EquipmentName, EquipmentDescription, EquipmentQuantity, RoomNumber, LastMaintenanceDate, NextMaintenanceDate, MaintenanceStatus) VALUES ('Squat Rack', 'Strength equipment', 5, 7, '2023-01-01', '2024-02-01', 'Good');
INSERT INTO Equipment (EquipmentName, EquipmentDescription, EquipmentQuantity, RoomNumber, LastMaintenanceDate, NextMaintenanceDate, MaintenanceStatus) VALUES ('Rowing Machine', 'Cardio equipment', 5, 8, '2022-01-01', '2024-02-01', 'Good');
INSERT INTO Equipment (EquipmentName, EquipmentDescription, EquipmentQuantity, RoomNumber, LastMaintenanceDate, NextMaintenanceDate, MaintenanceStatus) VALUES ('Yoga Straps', 'Yoga equipment', 15, 9, '2024-01-01', '2024-02-01', 'Good');
INSERT INTO Equipment (EquipmentName, EquipmentDescription, EquipmentQuantity, RoomNumber, LastMaintenanceDate, NextMaintenanceDate, MaintenanceStatus) VALUES ('Leg Press', 'Strength equipment', 5, 10, '2024-01-01', '2024-02-01', 'Good');

INSERT INTO Equipment (EquipmentName, EquipmentDescription, EquipmentQuantity, RoomNumber, LastMaintenanceDate, NextMaintenanceDate, MaintenanceStatus) VALUES ('Treadmill', 'Cardio equipment', 5, 1, '2023-01-01', '2025-02-01', 'Bad');

