# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 16:22:32 2019

@author: tala1
"""

import numpy as np
import os
#import functions
from bacteriaDataAnalysis import dataLoad
from dataStatistics import dataStatistics
from displayMenu import displayMenu
from inputNumber import inputNumber
from plot import dataPlot

print("Menu: ")
# Define menu items
menuItems = np.array(["Load data", "Filter data","Display statistics","Generate plots", "Quit"])
# Define empty filename variable
filename = ""


# ------------------------------------------------------------------
#Helper functions: 

#Error message
def Error():
    print("Error! you have to load a file first ")
#Filter for the Bacteria type
def bacteriaType(data,N):
    data=data[data[:,2]==N]
    return data

#filter for the Growth rate
def growthRate(data,maxLimit,minLimit):
    data=data[data[:,1]<maxLimit]
    data=data[data[:,1]>minLimit]
    return data
# ------------------------------------------------------------------



# Start
while True:
    # Display menu options and ask user to choose a menu item
    choice = displayMenu(menuItems)

#------------------------------------------------------------------        

# 1. Load data
    
    if choice == 1:
        # Ask user to load filename and save it in variable
        filename = input("Enter filename: ")
        #if file is not empty, and the file actuelly does exist use load function
        if (filename != "") and (os.path.isfile(filename) == True):
            data = dataLoad(filename)
        #otherwise show an error
        else:
            Error()
            
# ------------------------------------------------------------------
# 2. Filter data
    elif choice == 2:
        # Display error message if the file is not laoded
        if filename == "":
            Error()
        else:
            # Display menu options and ask user to choose a menu item
            filterChoice = np.array(["Bacteria Type filter","Growth Rate filter"])
            choice = displayMenu(filterChoice)
            
            if choice == 1:
                # Display menu options and ask user to choose a menu item
                bacteriaName = np.array(["Salmonella enterica","Bacillus cereus",
                                      "Listeria","Brochothrix thermosphacta"])
                N = displayMenu(bacteriaName)
                #filte the selceted bacteria type 
                data=bacteriaType(data,N)

            elif choice == 2:
                #Ask the user for max and min growthrates
                minLimit = inputNumber("Enter min value: ")
                maxLimit = inputNumber("Enter max value: ")
                #filter the selected rates
                data=growthRate(data,maxLimit,minLimit)

                
            else: 
                choice 
                
# ------------------------------------------------------------------
# 3. Display statistics
    elif choice == 3:
        # Display error message if the file is not laoded
        if filename == "":
            Error()
        # Display menu options and ask user to choose a menu item
        else:
            statisticsDescription = np.array(["Mean Temperature", "Mean Growth rate",
                                         "Std Temperature", "Std Growth rate", "Rows", 
                                         "Mean Cold Growth rate", "Mean Hot Growth rate"])
            print("Enter statistic number : ")
            displayStatDescription = displayMenu(statisticsDescription)
            #calculate the selected statistic
            print(dataStatistics(data, statisticsDescription[int(displayStatDescription) -1]))
            
# ------------------------------------------------------------------
# 4. Generate plots
    elif choice == 4:
        # Display error message if the file is not laoded
        if filename == "":
            Error()
        #show the plotted data
        else:
            dataPlot(data)

# ------------------------------------------------------------------
#5. Quit 
    elif choice == 5:
        break
    else:
        print("choose an item from the menu!)

    
    