### Purpose
At Hercules, there's the need to analyze a lot of data coming from the CMA valves. As there are .csv data files exported from testing and .json (specifically .sdat and .parameter) files that need to be dissected, there lies an opportunity to write scripts to import them into a database, store, read, compare, and utilize them. This is the software

### How to use the programs
If you want to import the .csv data into the database: 
Run python csv_import.py *.csv in the command line where * is the name of the csv file

If you want to import the .sdat data into the database:
- Open the sdat file and delete the END OF FILE line at the end. This is to avoid the IndexError: list index out of range
- Put sep=, in the beginning to override the ; seperator or replace all the ; with ,
- Save the *.sdat file as *.csv
- Run python sdat_import.py *.sdat in the command line where * is the name of the sdat file

If you want to import the .parameter data into the database:
- Rename the *.parameter file as *.json
- Run python parameter_import.py *.parameter in the command line where * is the name of the parameter file