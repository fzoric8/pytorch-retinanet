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


"""
font = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 0.8
color = (255, 0, 0)
thickness = 2


def plot_img(df, image_name):
    
    fig, ax = plt.subplots(1, 2, figsize = (10, 10))
    ax = ax.flatten()
    records = df[df['image_id'] == image_name]
    img_path = os.path.join(os.getcwd(), DIR_TRAIN, image_name)

    image = cv2.imread(img_path, cv2.IMREAD_COLOR)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB).astype(np.float32)
    image /= 255.0
    image2 = image
    
    ax[0].set_title('Original Image')
    ax[0].imshow(image)
    
    for idx, row in records.iterrows():
        box = row[['x', 'y', 'w', 'h']].values
        class_id = row['id']
        xmin = box[0]
        ymin = box[1]
        width = box[2]
        height = box[3]
        
        cv2.rectangle(image2, (int(xmin),int(ymin)), (int(xmin + width),int(ymin + height)), (255,0,0), 5)
        cv2.putText(image, 'id: {}'.format(class_id), (xmin-3, ymin-3), font, fontScale, color, thickness)
    
    ax[1].set_title('Image with Boundary Box')
    ax[1].imshow(image2)

    plt.show()
                            
"""