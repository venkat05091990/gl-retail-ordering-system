import sys
import papermill as pm
import time
import os
import data_preprocessing_db_update as db
 
# get the source data and notebook name from the python parameters
source_data = sys.argv[1]
source_notebook = sys.argv[2]
    
def get_current_time():
    timesecondEpoch = time.time()
    time_obj = time.localtime(timesecondEpoch)
    current_time =  '%d_%d_%d__%d_%d_%d' % (time_obj.tm_mday, time_obj.tm_mon, time_obj.tm_year, time_obj.tm_hour, time_obj.tm_min, time_obj.tm_sec)
    return current_time


def set_paths_and_create_job():
    data_path = './/data//source//'
    processed_data_path = './/data//processed//'
    unprocessed_data_path = './/data//unprocessed//'

    notebook_path = './/notebooks//input//'
    output_notebook_path = './/notebooks//output//'
    
    start_time = get_current_time()
    source_notebook_path = notebook_path + source_notebook
    source_data_path = data_path + source_data
    output_notebook_path = output_notebook_path + start_time + '_' + source_notebook
    preprocessed_data = processed_data_path  + start_time + '_'+ source_data.replace('.xlsx','.csv')
    unprocessed_data = unprocessed_data_path + start_time + '_unprocessed_'+  source_data.replace('.xlsx','.csv')
    status = 0
    
    batch_id = db.insert_job(source_data_path, source_notebook_path, preprocessed_data, unprocessed_data ,output_notebook_path, status, start_time)
    return (batch_id, source_notebook_path, output_notebook_path, start_time, source_data_path, preprocessed_data, unprocessed_data)

def run_preprocessing(source_data, input_notebook):
    
    details_tuple = set_paths_and_create_job()
    
    batch_id = details_tuple[0]
    source_notebook_path = details_tuple[1]
    output_notebook_path = details_tuple[2]
    current_time = details_tuple[3]
    source_data_path = details_tuple[4]
    preprocessed_data = details_tuple[5]
    unprocessed_data = details_tuple[6]
    
    print("Pre-Processing the Source File "+ source_data  +" using notebook " + source_notebook +" Started.")
    
    status = 1
    db.update_job_status(batch_id, status)
    
    # using papermill to run the notebook and saving the processed data, unprocessed data and processed notebooks
    pm.execute_notebook(source_notebook_path,
                        output_notebook_path,
                        parameters={
                                        'current_time':current_time,
                                        'batch_id': batch_id,
                                        'source_data': source_data_path,
                                        'source_notebook' : source_notebook_path,
                                        'preprocessed_data':preprocessed_data,
                                        'unprocessed_data':unprocessed_data
                                   }
                       )

    print("Pre-Processing the Source File "+ source_data  +" using notebook " + source_notebook +" Completed.")

    status = 2
    completion_time = get_current_time()
    db.update_job_completion(batch_id, status, completion_time)
    
if __name__=='__main__':
    run_preprocessing(source_data, source_notebook)