#import required package
import sqlite3 as sq

#CREATING A TABLE
#Create a connection
connection = sq.connect("classroomDB.db") #connection string

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

################
#INSERTING DATA
################
connection = sq.connect("classroomDB.db")

cursor = connection.cursor()

#to insert one single tuple in a table
insert_one = """
              INSERT INTO classroom VALUES(1,"Kraken","M",50,50,50);"""

cursor.execute(insert_one)

#to insert data into multiple tuples of the table
classroom_data = [(1, "RXYZ", "M", 70, 84, 92),
                  (2, "PSDF", "F", 87, 69, 93),
                  (3, "NKKL", "M", 65, 83, 90),
                  (4, "RWER", "F", 83, 76, 89)]
for std in classroom_data:
    insert_many = """
              INSERT INTO classroom VALUES({0},"{1}","{2}",{3},{4},{5});""".format(std[0],std[1],std[2],std[3],std[4],std[5])
    cursor.execute(insert_many)
    
connection.commit()

connection.close()

