Natasha Partenheimer
101082999

Folders/Files Included:
- In the SQL folder there are 2 .sql files:
    - ddl.sql - shows how the database tables were created
    - dml.sql - shows some initial data to be included in the database

- The remaining files are the source code:
    - admin.py - the admin functions
    - database.py - sets up the database
    - fitClub.py - the 'main' or startingpoint of the program
    - member.py - the member functions
    - trainer.py - the trainer functions

Installation Instructions:
- First, ensure that psycopg2 is installed on your os
- Next, in pgAdmin4 create a new database titled 'FitClub'
- Open a new query in this database and open/paste ddl.sql file and execute it
- Once the database tables have been successfully created, open/paste the dml.sql file into the query and execute it 
- In the file database.py, pase in your personal database password into the 'password' variable so the database can be accessed by the connection

Compilation Instructions:
- Navigate to the program folder in the terminal and run the command 'python fitClub.py'

Testing Instructions:
- Follow the instructions on the screen
- It is recommended that you register as a new member first

