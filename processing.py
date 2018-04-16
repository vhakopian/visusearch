import pandas as pd 
import numpy as np

def generate_words_dataframe (dataframe):
    """Returns a pandas dataframe where each row is a word from a query
    associated with the date of this query.
    """
    words_list = []

    for index, row in dataframe.iterrows():

        words = row["query"].split(" ")
        for word in words:
            words_list.append((np.datetime64(index),word))
            
    words_df = pd.DataFrame(words_list, columns = ["date","word"])

    return words_df


def time_standardization(time_list):
    for i in range(len(time_list)):
        time_list[i] = int(str(time_list[i])[:10])


def query_processing(dataframe):
    dataframe["number_query"]= 1
    dataframe["number_words"] = list(map(lambda x : len(x.split(" ")), dataframe["query"].values))
    

def word_occurences(word, words_df, resampling = "W"):
    """Counts the number of occurence of word in the word dataframe words_df
    with the sampling given in input.
    """
    words_df["number_occurence"] = 1
    occurrences = words_df.groupby("word").get_group(word).resample(resampling, on="date").sum()
    return occurrences