from datetime import date, datetime
import psycopg2





connection = psycopg2.connect(
    host="localhost",
    database="FitClub",
    user="postgres",
    password="XXXXXXXXXXX" #ADD YOUR PASSWORD HERE

)

cursor = connection.cursor()