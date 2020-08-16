# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 16:22:03 2019

@author: tala1
"""
import numpy as np
def dataStatistics(data, statistic):
    #This function calculates the selected value of statistic, using some built-in functions
    if statistic == "Mean Temperature":
        result = np.mean(data[:,0]) # returns the average of each element in datas first
                                    # column (Temperature)
    
    elif statistic == "Mean Growth rate":
        result = np.mean(data[:,1]) # returns the average of each element in datas second
                                    # column (Growth rate)
    
    elif statistic == "Std Temperature": 
        result = np.std(data[:,0]) # returns the standard deviation of each element in datas 
                                   # first column (Temperature)
                                   
    elif statistic == "Std Growth rate": 
        result = np.std(data[:,1]) # returns the standard deviation of each element in datas 
                                   # second column (Growth rate)
    
    elif statistic == "Rows":
        result = np.size(data,0)   # returns the size of data, which mean the amount of elements
                                   # in the first column (Temperature)
    
    elif statistic == "Mean Cold Growth rate": 
        lowTemp = data[data[:,0] < 20]
        result
        result = np.mean(lowTemp[:,1]) # returns all the elements datas first
                                       # column (Temperature) if less than 20 = lowTemp. If less
                                       # than 20 it return all elements from Growth rate less
                                       #  than 20
     
    elif statistic == "Mean Hot Growth rate": 
        highTemp = data[data[:,0] > 50] 
        result = np.mean(highTemp[:,1])# returns all the element in datas first
                                       # column (Temperature) if greater than 20 = highTemp. 
                                       # If grater than 50 it return all elements from Growth rate 
                                       # greater than 50
        
    return result