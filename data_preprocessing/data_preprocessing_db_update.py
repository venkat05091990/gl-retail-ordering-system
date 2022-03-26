# Import module
import sqlite3
import sys
import mysql
import mysql.connector
import json


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
    
def insert_job(data_path, notebook_path, processed_data_path, unprocessed_data_path, processed_notebook_path, status, start_time):
    # Connecting to sqlite
    # connection object
    connection_obj = get_db_connection()
    
    # cursor object
    cursor = connection_obj.cursor()   

    # Queries to INSERT records.
    values = (data_path, notebook_path, processed_data_path, unprocessed_data_path, processed_notebook_path, status, start_time)
    
    cursor.execute('''INSERT INTO grocart.DataPreprocessingJobs (data_path, notebook_path, processed_data_path, unprocessed_data_path, processed_notebook_path, status, start_time) VALUES (%s, %s, %s, %s, %s, %s, %s)''' , values)
        
    # Commit your changes in the database    
    connection_obj.commit()

    # Closing the connection
    connection_obj.close()
    
    return cursor.lastrowid


def update_job_status(batch_id, status):
    # Connecting to sqlite
    # connection object
    connection_obj = get_db_connection()

    # cursor object
    cursor = connection_obj.cursor()   

    # Queries to INSERT records.
    values = (status, batch_id)
    cursor.execute("UPDATE grocart.DataPreprocessingJobs SET status = %s WHERE batch_id = %s",values)
        
    # Commit your changes in the database    
    connection_obj.commit()

    # Closing the connection
    connection_obj.close()

def update_job_completion(batch_id, status, end_time):
    # Connecting to sqlite
    # connection object
    connection_obj = get_db_connection()

    # cursor object
    cursor = connection_obj.cursor()   

    # Queries to INSERT records.
    values = (status, end_time ,batch_id)
    cursor.execute("UPDATE grocart.DataPreprocessingJobs SET status = %s, end_time = %s WHERE batch_id = %s",values)
        
    # Commit your changes in the database    
    connection_obj.commit()

    # Closing the connection
    connection_obj.close()
    

def get_jobs():
    connection_obj = get_db_connection()
    cursor = connection_obj.cursor()

    sqlite_select_query = """SELECT batch_id, data_path, notebook_path, processed_data_path, unprocessed_data_path, processed_notebook_path, status, start_time, end_time from grocart.DataPreprocessingJobs"""
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()
    print("Total Jobs are:  ", len(records))
    print("Printing each Job")

    for row in records:
        print("Batch Id: ", row[0])
        print("Source Data Path ", row[1])
        print("Input Notebook Path", row[2])
        print("Processed Data Path", row[3])
        print("Unprocessed Data Path", row[4])
        print("Processed Notebook Path", row[5])
        print("Status", row[6])
        print("Start Time", row[7])
        print("End Time", row[8])
        print("\n")

    cursor.close()
    connection_obj.close()
    
    
def get_preprocessed_data_from_db():
    connection_obj = get_db_connection()
    cursor = connection_obj.cursor()

    sqlite_select_query = """SELECT * FROM grocart.PreprocessedData"""
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()
    print("Total Preprocessed Records are:  ", len(records))
    print("Printing each preprocessed record")

    for row in records:
        print("Sub_Category_Name: ", row[0])
        print("Category_Name", row[1])
        print("Product_Name", row[2])
        print("Brand", row[3])
        print("Weight", row[4])
        print("Price", row[5])
        print("productid", row[6])
        print("Image", row[7])
        print("Product_Rating", row[8])
        print("\n")

    cursor.close()
    connection_obj.close()
    

    
def get_unprocessed_data_from_db():
    connection_obj = get_db_connection()
    cursor = connection_obj.cursor()

    sqlite_select_query = """SELECT * FROM grocart.UnprocessedData"""
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()
    print("Total Unprocessed Records are:  ", len(records))
    print("Printing each unprocessed record")

    for row in records:
        print("Sub_Category_Name: ", row[0])
        print("Category_Name", row[1])
        print("Product_Name", row[2])
        print("Brand", row[3])
        print("Weight", row[4])
        print("Price", row[5])
        print("productid", row[6])
        print("Image", row[7])
        print("Product_Rating", row[8])
        print("\n")

    cursor.close()
    connection_obj.close()
