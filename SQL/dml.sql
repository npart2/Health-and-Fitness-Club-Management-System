

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

