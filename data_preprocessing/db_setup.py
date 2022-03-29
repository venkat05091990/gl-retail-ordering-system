# Import module
import sys
import mysql.connector
import json

# CHANGE THE MYSQL DATABASE CONNECTION HERE
def get_db_connection():
    with open("connection.json", "r") as read_file:
        conn_j = json.load(read_file)
        username=conn_j['username']
        password=conn_j['password']
        database=conn_j['database']
        server=conn_j['server']
        port=conn_j['port']
        conn=mysql.connector.connect(user=username, password=password, host=server, database=database)
        return conn
 
# Connecting to sqlite
# connection object
connection_obj = get_db_connection()
 
# cursor object
cursor_obj = connection_obj.cursor()

 
# Drop the Jobs table if already exists.
cursor_obj.execute("DROP TABLE IF EXISTS grocart.DataPreprocessingJobs")
 
# Creating Job table
table = """ CREATE TABLE grocart.DataPreprocessingJobs (
            batch_id INTEGER PRIMARY KEY AUTO_INCREMENT,
            data_path NVARCHAR(500) NOT NULL,
            notebook_path NVARCHAR(500) NOT NULL,
            processed_data_path NVARCHAR(500) NOT NULL,
            unprocessed_data_path NVARCHAR(500) NOT NULL,
            processed_notebook_path NVARCHAR(500) NOT NULL,
            status INT NOT NULL,
            start_time VARCHAR(100) NOT NULL,
            end_time VARCHAR(100) NULL
            ); """
 
cursor_obj.execute(table)
 
print("Job Table is Ready")

# Drop the Jobs table if already exists.
cursor_obj.execute("DROP TABLE IF EXISTS grocart.PreprocessedData")

# Creating Preprocessed table
table = """ CREATE TABLE grocart.PreprocessedData (
            Sub_Category_Name  NVARCHAR(500) NOT NULL,
            Category_Name  NVARCHAR(500) NOT NULL,
            Brand NVARCHAR(100) NOT NULL,
            Product_Name NVARCHAR(500) NOT NULL,
            Weight NVARCHAR(100) NOT NULL,
            Price DECIMAL(6,2) NOT NULL,
            productid INT NOT NULL ,
            Image   NVARCHAR(2000) NOT NULL,
            Product_Rating DECIMAL(2,1) NOT NULL
        ); """
 
cursor_obj.execute(table)
 
print("Preprocessed Table is Ready")


# Drop the Jobs table if already exists.
cursor_obj.execute("DROP TABLE IF EXISTS grocart.UnprocessedData")

# Creating Preprocessed table
table = """ CREATE TABLE grocart.UnprocessedData (
            Sub_Category_Name  NVARCHAR(500) NULL,
            Category_Name  NVARCHAR(500) NULL,
            Brand NVARCHAR(100) NULL,
            Product_Name NVARCHAR(500) NULL,
            Weight NVARCHAR(100) NULL,
            Price DECIMAL(10,2) NULL,
            productid NVARCHAR(100) NULL, 
            Image   NVARCHAR(2000) NULL,
            Product_Rating DECIMAL(6,2) NULL
        ); """
 
cursor_obj.execute(table)
 
print("Unprocessed Table is Ready")
 
# Close the connection
connection_obj.close()
