# This program is used to import sdat file into the database.

from cs50 import SQL
from csv import reader, DictReader
from sys import argv

# Open database
open(f"database.db", "a").close()
db = SQL("sqlite:///database.db")

# Check for arguments (sdat_import.py, *.sdat)
if len(argv) != 2:
    print("Usage: python sdat_import.py *.sdat")
    exit()

# Create tables
db.execute("""CREATE TABLE sdata (Node_Name TEXT, Description TEXT,
                                  Object_ID INT, Data_Type TEXT, Value REAL)
            """)

# Open CSV file by command line argument and read it
with open(argv[1]) as database:

    # Read it into memory as a list
    database_reader = reader(database)
    for row in database_reader:

        # Insert the data into the sdat database
        db.execute("INSERT INTO sdata (Node_Name, Description, Object_ID, Data_Type, Value) VALUES(?,?,?,?,?)", row[0], row[1], row[2], row[3], row[4])https://stackoverflow.com/questions/37706351/nested-json-to-csv-generic-approach