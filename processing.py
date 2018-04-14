import pandas as pd 
import numpy as np

def generate_words_dataframe (dataframe):
    words_list = []

    for index, row in dataframe.iterrows():

        words = row["query"].split(" ")
        for word in words:
            words_list.append((np.datetime64(index),word))
            
    words_df = pd.DataFrame(words_list, columns = ["date","word"])

    return words_df


def sort_dictionnary(dictionnary):
    l = []
    for word in sorted(dictionnary, key=dictionnary.get, reverse=True):
        l.append((word, dictionnary[word]))
    return l


def time_standardization(time_list):
    for i in range(len(time_list)):
        time_list[i] = int(str(time_list[i])[:10])


def query_processing(dataframe):
    dataframe["number_query"]= 1
    dataframe["number_words"] = list(map(lambda x : len(x.split(" ")), dataframe["query"].values))
    

def word_occurences(word, words_df, resampling = "W"):
    words_df["number_occurence"] = 1
    return words_df.groupby("word").get_group(word).resample(resampling, on="date").sum()