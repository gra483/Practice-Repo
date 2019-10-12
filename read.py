# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 21:05:40 2019

@author: gavin
"""

import pandas as pd
import os 

def readChampTable(fileName):
    champTable = pd.DataFrame()
    if(os.path.exists(fileName)):
        champTable = pd.read_csv(fileName)
    return champTable

def addPlayer(name, tierDictionary):
    file = "C:\\Users\\gavin\\Draft Tool\\data.csv"
    champTable = pd.read_csv(file,sep=",")
    toAdd = []
    for champ in champTable.Champion:
        if(champ in tierDictionary[1]):
            toAdd.append(1)
        elif(champ in tierDictionary[2]):
            toAdd.append(2)
        elif(champ in tierDictionary[3]):
            toAdd.append(3)
        else:
            toAdd.append(4)
    champTable[name] = toAdd
    champTable.to_csv("C:\\Users\\gavin\\Draft Tool\\data.csv", index = False)