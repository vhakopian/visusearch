#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 17:35:15 2018

@author: vahagn
"""

WEEK = 60*60*24*7

def words_list (queries):
    l = []
    for q in queries:
        l = l + q.split(" ")
    return l

def time_standardization(time_list):
    time_std = time_list.copy()
    for i in range(len(time_std)):
        time_std[i] = int(str(time_std[i])[:10])
    return time_std

def count_searchs_week(time_list, time_min, time_max):
    # week 0 starts Monday 4 July 2011 Midnight = 1309730400
    duree = time_max - time_min
    
    c_week = [0 for i in range(int(duree/WEEK)+1)]
    
    for t in time_list:
        c_week[int((t - time_min)/WEEK)] += 1
        
    return c_week
        
  
def count_searchs_month(time_list, time_min, time_max):
    month = 60*60*24*30.4167
    duree = time_max - time_min
    
    c_month = [0 for i in range(int(duree/month)+1)]
    
    for t in time_list:
        c_month[int((t - time_min)/month)] += 1
        
    return c_month