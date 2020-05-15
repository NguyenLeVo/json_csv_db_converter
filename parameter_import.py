# This program is used to import parameter file into the database.

from cs50 import SQL
from csv import reader, DictReader
from sys import argv
import pandas as pd
from pandas import json_normalize

# If we have a dictionary in json with no embedded array (meaning unnested json file) we could simply run
# df = pd.read_json("*.json") to read the json file
# dfn = json_normalize(df) to normalize it
# dfn.to_csv("output.csv", index = None) to export it
# But because the json file is embedded, we must unnest (flatten) then normalize it in order to do so

# If completely stuck: https://csvjson.com/json2csv

# Flatten the json file recursively.
# Source: https://towardsdatascience.com/flattening-json-objects-in-python-f5343c794b10
# Output is a dictionary
def flatten_json(y):
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x

    flatten(y)
    return out
    
# The most common forms of data:
# Just a dict: {} 
#   Use: flatten_json(data)
# List of dicts: [{}, {}, {}] 
#   Use: [flatten_json(x) for x in data]
# JSON with with top level keys, where the values repeat: {1: {}, 2: {}, 3: {}}
#   Use: [flatten_json(data[key]) for key in data.keys()]
# Other: {'key': [{}, {}, {}]}
#   Use: [flatten_json(x) for x in data['key']]
    
def json_convert(x):
    
    # Read the .json file
    file = pd.read_json(x)

    # Unnest or flatten the .json file using the function (depending case by case)
    # Output dff is a dictionary
    df = pd.DataFrame([flatten_json(x) for x in file['Devices']])
    
    # Transpose the table to allow for viewing pleasure
    df_t = df.T
    
    # Create the text file based on the output file name you chose in the command line
    # Export the table as a csv
    argv2=argv[2]
    df_t.to_csv(f'{argv2}', index=True)
    
def main():
    
    # Open database
    open(f"database.db", "w").close()
    db = SQL("sqlite:///database.db")

    # Check for arguments (parameter_import.py, *.json, **.csv)
    # .py is the converter, *.json is the renamed .parameter file, **.csv is the output file
    if len(argv) != 3:
        print("Usage: python parameter_import.py *.json **.csv")
        exit()

    # Create tables
    db.execute("""CREATE TABLE parameter (Title TEXT, VSM TEXT, Main_Inlet TEXT, Section_1 TEXT, 
                                          Section_2 TEXT, Section_3 TEXT, Section_4 TEXT, Section_5 TEXT, 
                                          Section_6 TEXT, Section_7 TEXT, Section_8 TEXT, Section_9 TEXT, 
                                          Section_10 TEXT, Section_11 TEXT, Section_12 TEXT, Section_13 TEXT)
               """)

    # Flatten the .json file and export it as a .csv
    json_convert(argv[1])
    
    # Open CSV file by command line argument and read it
    with open(argv[2]) as database:
    
        # Read it into memory as a list
        database_reader = reader(database)
        for row in database_reader:
    
            # Insert the data into the csv database
            # Have to look inside the csv to see the format to choose the right column locator for row[i]
            db.execute("""INSERT INTO parameter (Title, VSM, Main_Inlet, Section_1, 
                                           Section_2, Section_3, Section_4, Section_5, 
                                           Section_6, Section_7, Section_8, Section_9, 
                                           Section_10, Section_11, Section_12, Section_13)
                          VALUES(?,?,?,?,
                                 ?,?,?,?,
                                 ?,?,?,?,
                                 ?,?,?,?)""",
                       row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], 
                       row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15]
                       )
                       
        
if __name__ == '__main__':
    main()