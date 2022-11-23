# Part-1 Data Processing and Cleaning
# Importing modules
import csv
import sqlite3
from sqlite3 import Error



# Connecting to our database
connection = sqlite3.connect('risk_index.db')
# Creating a cursor object to execute
# SQL queries on a database table
cursor = connection.cursor()

# ****** Creating Risk Table **************
# Table Definition
create_table_risk = '''CREATE TABLE risk(
				country TEXT NOT NULL,
				wri REAL NOT NULL,
				vul REAL NOT NULL,
				year INTEGER NOT NULL)
				'''
# Creating the table into our
# database
cursor.execute(create_table_risk)
# Opening the csv file
risk_file = open('data/risk.csv')
# Reading the contents of the
# csv file
risk_contents = csv.reader(risk_file)
# SQL query to insert data into the
# risk table
insert_records_risk = "INSERT INTO risk (country, wri, vul, year) VALUES(?, ?, ?, ?)"
# Importing the contents of the file
# into our person table
cursor.executemany(insert_records_risk, risk_contents)
# Committing the changes
connection.commit()


# ****** Creating temperature Table **************
# Table Definition
create_table_temp = '''CREATE TABLE temperature(
				country TEXT NOT NULL,
				temp REAL NOT NULL,
				year INTEGER NOT NULL)
				'''
# Creating the table into our
# database
cursor.execute(create_table_temp)
# Opening the csv file
temp_file = open('data/temp.csv')
# Reading the contents of the
# csv file
temp_contents = csv.reader(temp_file)
# SQL query to insert data into the
# risk table
insert_records_temp = "INSERT INTO temperature (country, year, temp) VALUES(?, ?, ?)"
# Importing the contents of the file
# into our person table
cursor.executemany(insert_records_temp, temp_contents)
# Committing the changes
connection.commit()

# ****** Creating 3rd Final table wrisk **************
# The purpose of creating wrisk table is to 
# combine data from both risk and temperature into one table
# using LEFT JOIN operator

# Table Definition
create_table_wrisk = '''CREATE TABLE wrisk(
				country TEXT NOT NULL,
				wri REAL NOT NULL,
				vul REAL NOT NULL,
				year INTEGER NOT NULL,
				temp REAL NOT NULL
)
				'''
# Creating the table into our
# database
cursor.execute(create_table_wrisk)

# creating sql query for left join of risk and temperature table
join_table = '''
INSERT INTO wrisk
SELECT risk.country, wri, vul, risk.year, temp
FROM risk
LEFT JOIN temperature
ON risk.country=temperature.country AND risk.year=temperature.year;
'''
cursor.execute(join_table)
connection.commit()
# closing the database connection
connection.close()

print("**********************  Process Done - Table Created [risk, temperature, and wrisk]  **********************")
