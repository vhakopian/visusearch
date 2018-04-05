#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 17:42:34 2018

@author: vahagn
"""

import processing
import dataset_extraction
import matplotlib.pyplot as plt

def plot(count_weeks, count_months, time_min, time_max):


    fig = plt.figure(figsize=(8, 6))
    ax = plt.subplot(111)
    
    plt.title("Nombre de recherche par semaine", fontsize=14, ha="center")  
    
    fig.patch.set_facecolor('white')
    
    ax.spines["top"].set_visible(False)    
    ax.spines["bottom"].set_visible(False)    
    ax.spines["right"].set_visible(False)    
    ax.spines["left"].set_visible(False)
    
    ax.get_xaxis().tick_bottom()    
    ax.get_yaxis().tick_left()
     
    plt.xlim(0, len(count_weeks))
    plt.yticks(range(0, max(count_weeks)+50, 50), fontsize=12)  
    
    f = lambda t : int((t - time_min)/processing.WEEK)
    plt.xticks(f_list(f,[1325372400+k*60*60*24*365.25 for k in range(7)]), [2012+k for k in range(7)], fontsize=12)
    
    for y in range(0, max(count_weeks)+50, 50):    
        plt.plot(range(len(count_weeks)+10), [y] * len(range(len(count_weeks)+10)), "--", lw=0.5, color="black", alpha=0.5)  
        
    plt.tick_params(axis="both", which="both", bottom="on", top="off", labelbottom="on", left="off", right="off", labelleft="on") 
    
    
    ax.plot(range(len(count_weeks)),count_weeks)
    
    
    
    
def f_list(function, list):
    listc = list.copy()
    for k in range(len(list)):
        listc[k] = function(list[k])
        
    return listc

def main():
    time_list, queries_list = dataset_extraction.load_dataset()
    time_list = processing.time_standardization(time_list)
    
    time_min = min(time_list)
    time_max = max(time_list)
    
    
    
    count_weeks = processing.count_searchs_week(time_list, time_min, time_max)
    count_months = processing.count_searchs_month(time_list, time_min, time_max)
    
    plot(count_weeks, count_months, time_min, time_max)
    
if __name__ == "__main__":
    main()

