CREATE TABLE Members (
    MemberID SERIAL PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Username VARCHAR(50) NOT NULL,
    Password VARCHAR(50) NOT NULL
    

);

CREATE TABLE Trainers (
    TrainerID SERIAL PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Username VARCHAR(50) NOT NULL,
    Password VARCHAR(50) NOT NULL
    
);

CREATE TABLE Admins (
    AdminID SERIAL PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Username VARCHAR(50) NOT NULL,
    Password VARCHAR(50) NOT NULL
    
);

CREATE TABLE Goals (
    GoalID SERIAL PRIMARY KEY,
    GoalName VARCHAR(50) NOT NULL,
    GoalDescription VARCHAR(50) NOT NULL,
    StartDate DATE NOT NULL,
    EndDate DATE NOT NULL,
    MemberID INT NOT NULL REFERENCES Members(MemberID)
);

CREATE TABLE HealthMetrics (
    HealthMetricID SERIAL PRIMARY KEY,
    Weight INT NOT NULL,
    Height INT NOT NULL,
    Age INT NOT NULL,
    BMI FLOAT NOT NULL,
    MemberID INT NOT NULL REFERENCES Members(MemberID)
);

CREATE TABLE PersonalTrainerSessions (
    SessionID SERIAL PRIMARY KEY,
    SessionDate DATE NOT NULL,
    DayOfWeek VARCHAR(50) NOT NULL,
    StartTime TIME NOT NULL,
    EndTime TIME NOT NULL,
    TrainerID INT NOT NULL REFERENCES Trainers(TrainerID),
    MemberID INT REFERENCES Members(MemberID)
    
   
);

CREATE TABLE GroupTrainingSessions (
    SessionID SERIAL PRIMARY KEY,
    SessionDate DATE NOT NULL,
    DayOfWeek VARCHAR(50) NOT NULL,
    StartTime TIME NOT NULL,
    EndTime TIME NOT NULL,
    TrainerID INT NOT NULL REFERENCES Trainers(TrainerID)
    
    
    
);

CREATE TABLE GroupTrainingSessionMembers (
    
    SessionID INT NOT NULL REFERENCES GroupTrainingSessions(SessionID),
    MemberID INT REFERENCES Members(MemberID)
    
);



CREATE TABLE TrainerAvailability (
    sessionID SERIAL PRIMARY KEY,
    SessionDate DATE,
    DayOfWeek VARCHAR(50),
    StartTime TIME,
    EndTime TIME,
    TrainerID INT NOT NULL REFERENCES Trainers(TrainerID)

);

CREATE TABLE Rooms (
    RoomID SERIAL PRIMARY KEY,
    RoomName VARCHAR(50) NOT NULL,
    RoomCapacity INT NOT NULL,
    GroupSessionID INT REFERENCES GroupTrainingSessions(SessionID),
    PrivateSessionID INT REFERENCES PersonalTrainerSessions(SessionID)

   
);

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

CREATE TABLE Billing (
    BillingID SERIAL PRIMARY KEY,
    MemberID INT NOT NULL REFERENCES Members(MemberID),
    Cost INT NOT NULL,
    PaymentStatus VARCHAR(50) NOT NULL
);

