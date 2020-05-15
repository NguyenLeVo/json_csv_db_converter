### Purpose
- At Hercules, there's the need to analyze a lot of data coming from the CMA valves. As there are .csv data files exported from testing and .json (.parameter) and .csv(.sdat) files that need to be dissected, there lies an opportunity to write scripts to import them into a database, store, read, compare, and utilize them. 
- This is the software package to transform them into neat data sets.
- Written in Python and SQL. Also used Pandas library.

### Result
- The .parameter (.json) went from 24938 lines of data to 859 lines, achieving a 96.5% reduction in data size.

### How to use the programs
If you want to import the .csv data into the database: 
- Run python csv_import.py x.csv in the command line where x is the name of the csv file

If you want to import the .sdat data into the database:
- Open the sdat file and delete the END OF FILE line at the end. This is to avoid the IndexError: list index out of range
- Put sep=, in the beginning to override the ; seperator or replace all the ; with ,
- Save the x.sdat file as x.csv
- Run python sdat_import.py x.sdat in the command line where x is the name of the sdat file

If you want to import the .parameter data into the database:
- Rename the x.parameter file as x.json
- Run: python parameter_import.py x.json xx.csv in the command line where x is the name of the parameter file and xx is the output file name

### Understanding of the files here
For .csv:
- PV9_Testing.csv is the original data file
- csv_import.py is the converter
- database_csv.db is the output

For .sdat:
- CMA_Release.csv is the data file that was renamed from the .sdat file
- sdat_import.py is the converter
- database_sdat.db is the output

For .json:
- Release.csv is the data file that was renamed from the .parameter file
- parameter_import.py is the converter
- database_parameter.db and output.csv are the output.

There is the orignal data attached in the folder.
