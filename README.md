# Data Modeling with Postgres

# Project Description
 Modeling a Postgres database for Sparkify, A music streaming Start-up. The goal of this project is to model
 a relational database for Sparkify and build an ETL pipeline using Python,that transfers data from files in two local directories into tables that store User information and music streams log data,The Data analysts at Sparkify can then query this data and derive insights on what songs users are listening to and report on business performance.
 
 # Data base Schema
 The SparkifyDb database is a star schema design, contains the following fact and dimension tables:

### Fact Table
songplays - records log data dataset associated with song plays in app <br>
Columns : songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent

### Dimension Tables
1. users - users in the app <br>
 columns : user_id, first_name, last_name, gender, level
2. songs - songs in music database <br>
columns : song_id, title, artist_id, year, duration
3. artists - artists in music database <br>
columns : artist_id, name, location, latitude, longitude
4. time - timestamps of records in songplays broken down into specific units <br>
columns : start_time, hour, day, week, month, year, weekday
 
 
 # How it works
 Datasets
 JSON logs on user activity on the app (source :https://github.com/Interana/eventsim), as well as a directory with JSON metadata on the songs in their app (source : http://millionsongdataset.com/).
 
 ### sql_queries.py
 
 sql queries to create fact and dimension tables and insert records into them are stored in this file
 
 ### Create_tables.Py
 
 Python script to create database, and create fact and dimension tables
 
 ### etl.ipynb
Test ETL logic, see how it works, before implementing it as a python script
 
 ### etl.py
 
  Etl script to move log data and song data from directory into desired tables
 
 ### test.ipynb
 
 Run queries on the database to check creation of tables and inclusion of data. also contain common queries an Analyst will run:
 No of customers acquired, Top streamed artist, No of customers on Paid service
