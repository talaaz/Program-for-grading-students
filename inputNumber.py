# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 12:48:06 2019

@author: tala1
*modules_python
"""

def inputNumber(prompt):
    # INPUTNUMBER Prompts user to input a number
    while True:
        try:
            num = float(input(prompt))
            break
        except ValueError:
            pass
    return num

