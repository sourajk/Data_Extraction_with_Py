#import required package
import sqlite3 as sq

#Create a connection
connection = sq.connect("classroomDB.db")#connection string

#Initialize cursor
cursor = connection.cursor()

#Write Query for creating table
create_table = """
                CREATE TABLE classroom (student_id INTEGER PRIMARY KEY,
                Name VARCHAR(20),
                Gender CHAR(1),
                Phy_marks INTEGER,
                Chem_marks INTEGER,
                Math_marks INTEGER);"""


#Execute query
cursor.execute(create_table)

#Commit changes
connection.commit()

#Close the connection
connection.close()

