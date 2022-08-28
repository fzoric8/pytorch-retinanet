import os
import copy
import pandas as pd

def open_folder(folder): 
    
    files = []
    
    path = os.path.join(os.getcwd(), folder)

    for file in os.listdir(path):
        files.append(file)
        
    return files

def open_abs_folder(path): 
    
    files = []
    
    for file in os.listdir(path): 
        files.append(file)
    
    return files

def open_csv(file): 
    
    df = pd.read_csv(file)
    
    return df

def copy_file(src, dist): 
    
    cmd = 'cp {} {}'.format(src, dist)
    
    os.system(cmd)  

def recreate_df(dataframe): 
    
    recreated_df = dataframe.rename(columns={"filename": "image_id"})
    
    # Rename columns
    recreated_df['x'] = recreated_df['xmin']
    recreated_df['y'] = recreated_df['ymin'] 
    recreated_df['w'] = recreated_df['xmax'] - recreated_df['xmin']
    recreated_df['h'] = recreated_df['ymax'] - recreated_df['ymin']
    
    # Delete old columns
    del(recreated_df['xmin'])
    del(recreated_df['xmax'])
    del(recreated_df['ymin'])
    del(recreated_df['ymax'])
    
    return recreated_df

def create_df(path, folder): 
    
    full_path = "{}/{}".format(path, folder)
    debug = True
    if debug:
        print(full_path)
    files = open_abs_folder(full_path)
    
    for i, filename in enumerate(files):
        print(i)
        if filename.split(".")[-1] == "csv": 
            
            df_ = open_csv("{}/{}".format(full_path, filename))
            df_ = recreate_df(df_)
            if (i == 0):
                df_all = copy.deepcopy(df_)
            else: 
                df_all = df_all.append(copy.deepcopy(df_))
            #display(df_all)
    
    return df_all
                            