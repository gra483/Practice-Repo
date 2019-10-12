# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 17:05:19 2019

@author: gavin
"""

import draft
from read import readChampTable
import pandas as pd
from read import addPlayer

def main():
    print("Running")
    side = draft.readSide()
    banList = []  
    pickList = []
    champTable = readChampTable("data.csv")
    
    players = draft.readPlayers(champTable)
    banList = draft.readBansPart1(champTable, side, pickList, banList) 
    pickList = draft.readPicksPart1(champTable, side, pickList, banList, players)
    banList = draft.readBansPart2(champTable, side, pickList, banList)
    pickList = draft.readPicksPart2(champTable, side, pickList, banList , players)
    
if __name__ == "__main__":
    main()




