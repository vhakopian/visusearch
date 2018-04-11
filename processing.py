import pandas as pd 

def words_dictionnary (queries):
    dict = {}
    for q in queries:
        words = q.split(" ")
        
        for word in words:
            if word in dict:
                dict[word] += 1
            else:
                dict[word] = 1
            
    return dict

def sort_dictionnary(dictionnary):
    l = []
    for word in sorted(dictionnary, key=dictionnary.get, reverse=True):
        l.append((word, dictionnary[word]))
    return l

def time_standardization(time_list):
    time_std = time_list.copy()
    for i in range(len(time_std)):
        time_std[i] = int(str(time_std[i])[:10])
    return time_std
