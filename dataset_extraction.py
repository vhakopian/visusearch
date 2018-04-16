import json
import processing
import numpy as np
import pandas as pd

NO_FILES = 28

def load_file(filename):
    """Returns a pandas dataframe containing pairs of date and query contained
    in .json file given as input. 
    The dataframe has timestamps as index and queries as first column.
    """
    file  = open(filename, "r", encoding='utf-8')
    data = json.load(file)
    data = data['event']
    
    time_list, query_list = [], []
    
    for line in data:
        time, query = int(line['query']['id'][0]['timestamp_usec']), line['query']['query_text']
        time_list.append(time)
        query_list.append(query)
        
    file.close()
    
    processing.time_standardization(time_list)
    time_list = np.array(time_list, dtype='datetime64[s]')
    
    dataframe = pd.DataFrame(query_list, index = time_list, columns = ["query"])
    
    return dataframe


def load_dataset():
    """Returns a pandas dataframe containing pairs of date and query contained
    in all the .json files that contain the google searchs.
    The dataframe has timestamps as index and queries as first column.
    """
    dataframe_list = []
    
    for i in range(1, NO_FILES):
        dataframe = load_file("/Users/vahagn/Projets d\'informatique/Visusearch project/searchs/"+str(i)+".json")
        dataframe_list.append(dataframe)
        
    dataframe = pd.concat(dataframe_list)
    dataframe = dataframe.sort_index()
    
    return dataframe