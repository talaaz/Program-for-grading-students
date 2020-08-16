# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 18:40:56 2019

@author: tala1
"""

import numpy as np # Import NumPy
import matplotlib.pyplot as plt # Import the matplotlib.pyplot module


def dataPlot(data):
    #define the differnet types of bactaries
    SalmonellaEnterica = data[data[:,2]==1]
    BacillusCereus = data[data[:,2]==2]
    Listeria= data[data[:,2]==3]
    BrochothrixThermosphacta = data[data[:,2]==4]
  

    #Bar plot of the number of each of the different types of Bacteria in the data.         
    bars = ('Salmonella', 'Bacillus', 'Listeria', 'Brochothrix')
    number = [len(SalmonellaEnterica),len(BacillusCereus),len(Listeria),len(BrochothrixThermosphacta)]
    y_pos = np.arange(len(bars)) 
     
    plt.bar(y_pos, number, align='center', alpha=0.15, color=('c','b','g','r', ))
    plt.xticks(y_pos, bars)

    plt.title("Number of bacteria")          # Set the title of the graph 
    plt.xlabel("Bacteria name")              # Set the x-axis label
    plt.ylabel("Number")                     # Set the y-axis label

    NumberOfBacteria= plt.show()
    

    #Growth rate by temperature, a plot with the Temperature on the x-axis and the Growth rate on the y-axis    
    plt.plot(SalmonellaEnterica[:,0], SalmonellaEnterica[:,1],'-','b') # Plot line graph of x and y- Line - w. color
    
    plt.plot(BacillusCereus[:,0], BacillusCereus[:,1],'-', 'g')  
    
    plt.plot(Listeria[:,0], Listeria[:,1],'-','r') 
    
    plt.plot(BrochothrixThermosphacta[:,0], BrochothrixThermosphacta[:,1],'-', 'c') # Plot line graph of x and y
 
    plt.title("Growth rate by temperature")      # Set the title of the graph
    plt.xlabel("Temperature")                    # Set the x-axis label
    plt.ylabel("Growth rate")                    # Set the y-axis label
    plt.xlim([10, 60])                           # Set the limits of the x-axis
    plt.ylim(ymin=0)                             # Set the limits of the y-axis
    bacteriaNames = ["Salmonella enterica","Bacillus cereus","Listeria","Brochothrix thermosphacta"]
    plt.legend(bacteriaNames)                     # add a legend to the plot, to inform about the difference bewteen the 4 types
    
    GrowthRate=plt.show()
    
    return NumberOfBacteria,GrowthRate
