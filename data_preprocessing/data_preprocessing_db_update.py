# Import module
import sqlite3
import sys


def insert_job(data_path, notebook_path, processed_data_path, unprocessed_data_path, processed_notebook_path, status, start_time):
    # Connecting to sqlite
    # connection object
    connection_obj = sqlite3.connect('data_preprocessing.db')

    # cursor object
    cursor = connection_obj.cursor()   

    # Queries to INSERT records.
    values = (data_path, notebook_path, processed_data_path, unprocessed_data_path, processed_notebook_path, status, start_time)
    cursor.execute("INSERT INTO Jobs (data_path, notebook_path, processed_data_path, unprocessed_data_path, processed_notebook_path, status, start_time) VALUES (?,?,?,?,?,?,?)",values)
        
    # Commit your changes in the database    
    connection_obj.commit()

    # Closing the connection
    connection_obj.close()
    
    return cursor.lastrowid


def update_job_status(batch_id, status):
    # Connecting to sqlite
    # connection object
    connection_obj = sqlite3.connect('data_preprocessing.db')

    # cursor object
    cursor = connection_obj.cursor()   

    # Queries to INSERT records.
    values = (status, batch_id)
    cursor.execute("UPDATE Jobs SET status = ? WHERE batch_id = ?",values)
        
    # Commit your changes in the database    
    connection_obj.commit()

    # Closing the connection
    connection_obj.close()

def update_job_completion(batch_id, status, end_time):
    # Connecting to sqlite
    # connection object
    connection_obj = sqlite3.connect('data_preprocessing.db')

    # cursor object
    cursor = connection_obj.cursor()   

    # Queries to INSERT records.
    values = (status, end_time ,batch_id)
    cursor.execute("UPDATE Jobs SET status = ?, end_time = ? WHERE batch_id = ?",values)
        
    # Commit your changes in the database    
    connection_obj.commit()

    # Closing the connection
    connection_obj.close()
    

def get_jobs():
    connection_obj = sqlite3.connect('data_preprocessing.db')
    cursor = connection_obj.cursor()

    sqlite_select_query = """SELECT batch_id, data_path, notebook_path, processed_data_path, unprocessed_data_path, processed_notebook_path, status, start_time, end_time from Jobs"""
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