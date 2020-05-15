# This program is used to import csv file into the database.

from cs50 import SQL
from csv import reader, DictReader
from sys import argv

# Open database
open(f"database.db", "a").close()
db = SQL("sqlite:///database.db")

# Check for arguments (csv_import.py, *.csv)
if len(argv) != 2:
    print("Usage: python csv_import.py *.csv")
    exit()

# Create tables
db.execute("""CREATE TABLE csv (Position_Sensor_1_Time_s FLOAT, Position_Sensor_1_Data FLOAT,
                                Position_Sensor_2_Time_s FLOAT, Position_Sensor_2_Data FLOAT,
                                Pressure_Sensor_1_Time_s FLOAT, Pressure_Sensor_1_Data FLOAT,
                                Pressure_Sensor_2_Time_s FLOAT, Pressure_Sensor_2_Data FLOAT,
                                Debug_1_Time_s FLOAT, Debug_1_Data FLOAT,
                                Debug_2_Time_s FLOAT, Debug_2_Data FLOAT,
                                Supply_Pressure_Time_s FLOAT, Supply_Pressure_Data FLOAT)
            """)

# Open CSV file by command line argument and read it
with open(argv[1]) as database:

    # Read it into memory as a list
    database_reader = reader(database)
    for row in database_reader:

        # Insert the data into the csv database
        # Have to look inside the csv to see the format to choose the right column locator for row[i]
        db.execute("""INSERT INTO csv (Position_Sensor_1_Time_s, Position_Sensor_1_Data,
                                       Position_Sensor_2_Time_s, Position_Sensor_2_Data,
                                       Pressure_Sensor_1_Time_s, Pressure_Sensor_1_Data,
                                       Pressure_Sensor_2_Time_s, Pressure_Sensor_2_Data,
                                       Debug_1_Time_s, Debug_1_Data,
                                       Debug_2_Time_s, Debug_2_Data,
                                       Supply_Pressure_Time_s, Supply_Pressure_Data)
                      VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                   row[2], row[3], row[5], row[6], row[8], row[9], row[11],
                   row[12], row[14], row[15], row[17], row[18], row[20], row[21]
                   )