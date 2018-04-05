#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 17:20:15 2018

@author: vahagn
"""

import json

def load_file(filename):
    
    file  = open(filename, "r", encoding='utf-8')
    data = json.load(file)
    
    data = data['event']
    
    time_list = []
    query_list = []
    
    for line in data:
        (time, query) = (int(line['query']['id'][0]['timestamp_usec']),line['query']['query_text'])
        time_list.append(time)
        query_list.append(query)

    file.close()
    
    return time_list, query_list



def load_dataset():
    
    time_list = []
    query_list = []
    
    for i in range(1,28):
        time_list_file,query_list_file = load_file("/Users/vahagn/Projets d\'informatique/Visusearch project/searchs/"+str(i)+".json")
        time_list += time_list_file
        query_list += query_list_file

    return time_list, query_list