import sqlite3
 
# Connecting to sqlite
# connection object
connection_obj = sqlite3.connect('data_preprocessing.db')
 
# cursor object
cursor_obj = connection_obj.cursor()
 
# Drop the Jobs table if already exists.
cursor_obj.execute("DROP TABLE IF EXISTS Jobs")
 
# Creating table
table = """ CREATE TABLE Jobs (
            batch_id INTEGER PRIMARY KEY AUTOINCREMENT,
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
 
# Close the connection
connection_obj.close()