import json
import processing
import numpy as np
import pandas as pd

def load_file(filename):
    
    file  = open(filename, "r", encoding='utf-8')
    data = json.load(file)
    
    data = data['event']
    
    timeList = []
    queryList =[]
    
    for line in data:
        (time, query) = (int(line['query']['id'][0]['timestamp_usec']),line['query']['query_text'])
        timeList.append(time)
        queryList.append(query)
        
    file.close()
    
    timeList = processing.time_standardization(timeList)
    timeList = np.array(timeList,dtype='datetime64[s]')
    
    dataframe = pd.DataFrame(queryList, index = timeList, columns = ["query"])
    
    return dataframe



def load_dataset():
    
    dataframeList = []
    
    for i in range(1,28):
        dataframe = load_file("/Users/vahagn/Projets d\'informatique/Visusearch project/searchs/"+str(i)+".json")
        dataframeList.append(dataframe)
        
    dataframe = pd.concat(dataframeList)
    dataframe = dataframe.sort_index()
    
    dataframe["numberQuery"]= 1
    dataframe["numberWords"] = list(map(lambda x : len(x.split(" ")), dataframe["query"].values))

    return dataframe