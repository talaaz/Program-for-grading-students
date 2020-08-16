# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 12:46:25 2019

@author: tala1
*modules_python
"""
from inputNumber import inputNumber
import numpy as np

def displayMenu(options):
    # Display menu options
    for i in range(len(options)):
        print("{:d}. {:s}".format(i+1, options[i]))
    # Get a valid menu choice
    choice = 0
    while not(np.any(choice == np.arange(len(options))+1)):
        choice = inputNumber("Please choose a menu item: ")
    return choice



