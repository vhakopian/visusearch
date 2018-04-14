import dataset_extraction
import processing
import matplotlib.pyplot as plt
import numpy as np

def plot_general(dataframe):

    fig = plt.figure(figsize=(14, 10))
    
    ax_week = plt.subplot(221)
    plt.title("Number of searches by week", fontsize=14, ha="center") 
    
    ax_month = plt.subplot(222)
    plt.title("Number of searches by month", fontsize=14, ha="center") 
    
    ax_wordperweek = plt.subplot(223)
    plt.title("Average number of words by query by week", fontsize=14, ha="center") 
    
    ax_wordpermonth = plt.subplot(224)
    plt.title("Average number of words by query by month", fontsize=14, ha="center") 
    
    
    fig.patch.set_facecolor('white')
    
    
    ax_week.plot(dataframe["number_query"].resample("W").sum())
    ax_month.plot(dataframe["number_query"].resample("M").sum())
    ax_wordperweek.plot(dataframe["number_words"].resample("1W").mean())
    ax_wordpermonth.plot(dataframe["number_words"].resample("M").mean())
    
    
    
    
def plot_word(words_df, words):
    
    n = len(words)
    
    fig = plt.figure(figsize=(15, n*1.7))
    
    plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=0.3)
    
    xmin, xmax = min(words_df["date"].values), max(words_df["date"].values)
   
    for k in range(n):
        
        ax = plt.subplot(n,1,k+1)
        
        if (k==0):
            plt.title("Number of searches of by month", fontsize=14, ha="center") 
           
       
        fig.patch.set_facecolor('white')

        df_month = processing.word_occurences(words[k],words_df,resampling="M")
        index_month, values_month = df_month.index.values, df_month["number_occurence"].values
        
        ax.set_xlim(xmin, xmax)
        ax.bar(index_month, values_month, int(0.75*30))
        
        ax.legend([words[k]], loc='upper left', frameon=True)
        
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)
        ax.spines['left'].set_visible(False)
        
        plt.tick_params(axis='y', which='both', left='off', right='off', labelleft='off') 


        if (k+1 != n):
            plt.tick_params(axis='x', which='both', bottom='off', top='off', labelbottom='off') 



def plot_hours(dataframe):
    
    #filtering
    #dataframe = dataframe.loc[dataframe.index > '2018-01-01 08:00:00']
    
    #processing
    df = dataframe["number_query"].resample("H").sum()
    
    n = len(df)
    repartition = np.zeros(24)
    
    for k in range(n):
        hour = df.index[k].hour
        number_query = df.values[k]
        
        repartition[hour] += number_query
    
    plt.plot(repartition)
        


# Data extraction: first time from json====================================
dataframe = dataset_extraction.load_dataset()
words_df = processing.generate_words_dataframe(dataframe)
processing.query_processing(dataframe)
# =========================================================================
#plot_general(dataframe)
#plot_word(words_df,["facebook","flights","amazon"])
plot_hours(dataframe)