# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 16:15:13 2019

@author: tala1
"""
import numpy as np
def dataLoad(filename):
    data = np.loadtxt(filename)  #reads the data in the data 
    N = 0                        #number of valid rows in the data file.
    line = 0                     #line number
    error = False                #boolean to check errors 
    for line in range (len(data)):
        if(data[N,0] >= 60): # If value in the first column is greater or equal to 60 the error down below will be printed.
                             # 
            print(line + 1 , "The Temperature must be a number between 10 and 60.")
            error = True
      
        elif(data[N,0] <= 10): # If the value in the first column is  less or equal to 10 the error down below will be printed.
            print(line+1, "The Temperature must be a number between 10 and 60.")        
            error = True
        
        elif(data[N,1] < 0): # If the value in the second column is less than 0  the error down below will be printed
            print(line+1, "The Growth rate must be a positive number.")
            error = True
    
        elif(data[N,2] != 1) and (data[N,2] != 2) and (data[N,2] != 3) and (data[N,2] != 4):
            print(line+1, "The Bacteria must be one of the four mentioned in the table.")
            error = True # Checks if N is 
         
        elif error:       # If any of the statements are false and this last one is true, then
                          # deletes the data index N from the dataset. 
            data=np.delete(data,[N],axis=0)
            N=N-1       #get the right index for N
        N=N+1           #next line with new col.
        line = line+1   # next line with a line
        error = False   # reset the error

    return data          #returns the correct data

