import sys
import papermill as pm
import time
 
timesecondEpoch = time.time()
 
time_obj = time.localtime(timesecondEpoch)
 
current_time =  '%d_%d_%d__%d_%d_%d' % (time_obj.tm_mday, time_obj.tm_mon, time_obj.tm_year, time_obj.tm_hour, time_obj.tm_min, time_obj.tm_sec)

#source data and notebook paths
source_data = sys.argv[1]
source_notebook = sys.argv[2]

# connect to sql and create a batch record
# insert batchid, data_path, notebook_path, processed_data_path, unprocessed_data_path ,processed_notebook_path, status,batch_start_time, batch_end_time
# initial status batch started = 0
# batch running status = 1
# completed successfully batch successfull = 2
# get the batch id

data_path = './/data//source//'
processed_data_path = './/data//processed//'
unprocessed_data_path = './/data//unprocessed//'

notebook_path = './/notebooks//input//'
output_notebook_path = './/notebooks//output//'


batch_id = '1000'
source_notebook_path = notebook_path + source_notebook
source_data_path = data_path + source_data
output_notebook_path = output_notebook_path + batch_id + '_' + current_time + '_' + source_notebook
preprocessed_data = processed_data_path  + batch_id + '_'  + current_time + '_'+ source_data.replace('.xlsx','.csv')
unprocessed_data = unprocessed_data_path + batch_id + '_'  + current_time + '_unprocessed_'+  source_data.replace('.xlsx','.csv')

print("Pre-Processing the Source File "+ source_data  +" using notebook " + source_notebook +" Started.")
print(output_notebook_path)

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