# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 17:05:39 2019

@author: gavin
"""

import Champion
from difflib import SequenceMatcher  
from colorama import Fore
from colorama import Style


def displayPotentialPicks(champTable, pickList, banList, players):
    champFilter = champTable.Champion.str.contains('|'.join(pickList+banList))
    potentialPicks = champTable[[not x for x in champFilter]]
    
    allPicksP1 = potentialPicks[potentialPicks[players[0]]<4]
    availableSP1 = potentialPicks[potentialPicks[players[0]]==1]
    availableAP1 = potentialPicks[potentialPicks[players[0]]==2]
    availableBP1 = potentialPicks[potentialPicks[players[0]]==3]
    
    allPicksP2 = potentialPicks[potentialPicks[players[1]]<4]
    availableSP2 = potentialPicks[potentialPicks[players[1]]==1]
    availableAP2 = potentialPicks[potentialPicks[players[1]]==2]
    availableBP2 = potentialPicks[potentialPicks[players[1]]==3]
    
    allPicksP3 = potentialPicks[potentialPicks[players[2]]<4]
    availableSP3 = potentialPicks[potentialPicks[players[2]]==1]
    availableAP3 = potentialPicks[potentialPicks[players[2]]==2]
    availableBP3 = potentialPicks[potentialPicks[players[2]]==3]
    
    allPicksP4 = potentialPicks[potentialPicks[players[3]]<4]
    availableSP4 = potentialPicks[potentialPicks[players[3]]==1]
    availableAP4 = potentialPicks[potentialPicks[players[3]]==2]
    availableBP4 = potentialPicks[potentialPicks[players[3]]==3]
    
    allPicksP5 = potentialPicks[potentialPicks[players[4]]<4]
    availableSP5 = potentialPicks[potentialPicks[players[4]]==1]
    availableAP5 = potentialPicks[potentialPicks[players[4]]==2]
    availableBP5 = potentialPicks[potentialPicks[players[4]]==3]
    

   #really just a bunch of print statements to print each players picks, highlighted if flex
   #pprobably would have been faster to get a list of flex picks first, but I just checked every time b/c it works
    
    print()
    print()
    print("OPEN PICKS: \n")
    print("\u0332".join(players[0]))
    print("S Tier: ", end = "")
    for x in availableSP1["Champion"]:
        if(allPicksP2["Champion"].str.contains(x).any() or allPicksP3["Champion"].str.contains(x).any() or allPicksP4["Champion"].str.contains(x).any() or allPicksP5["Champion"].str.contains(x).any()):
            print(Fore.CYAN + x + Style.RESET_ALL, end = " ")
        else:
            print(x, end = " ")
    print("\nA Tier: ", end = "")
    for x in availableAP1["Champion"]:
        if(allPicksP2["Champion"].str.contains(x).any() or allPicksP3["Champion"].str.contains(x).any() or allPicksP4["Champion"].str.contains(x).any() or allPicksP5["Champion"].str.contains(x).any()):
            print(Fore.CYAN + x + Style.RESET_ALL, end = " ")
        else:
            print(x, end = " ")
    print("\nB Tier: ", end = "")
    for x in availableBP1["Champion"]:
        if(allPicksP2["Champion"].str.contains(x).any() or allPicksP3["Champion"].str.contains(x).any() or allPicksP4["Champion"].str.contains(x).any() or allPicksP5["Champion"].str.contains(x).any()):
            print(Fore.CYAN + x + Style.RESET_ALL, end = " ")
        else:
            print(x, end = " ")    
    print()
    print()
    print("\u0332".join(players[1]))
    print("S Tier: ", end = "")
    for x in availableSP2["Champion"]:
        if(allPicksP1["Champion"].str.contains(x).any() or allPicksP3["Champion"].str.contains(x).any() or allPicksP4["Champion"].str.contains(x).any() or allPicksP5["Champion"].str.contains(x).any()):
            print(Fore.CYAN + x + Style.RESET_ALL, end = " ")
        else:
            print(x, end = " ")
    print("\nA Tier: ", end = "")
    for x in availableAP2["Champion"]:
        if(allPicksP1["Champion"].str.contains(x).any() or allPicksP3["Champion"].str.contains(x).any() or allPicksP4["Champion"].str.contains(x).any() or allPicksP5["Champion"].str.contains(x).any()):
            print(Fore.CYAN + x + Style.RESET_ALL, end = " ")
        else:
            print(x, end = " ")
    print("\nB Tier: ", end = "")
    for x in availableBP2["Champion"]:
        if(allPicksP1["Champion"].str.contains(x).any() or allPicksP3["Champion"].str.contains(x).any() or allPicksP4["Champion"].str.contains(x).any() or allPicksP5["Champion"].str.contains(x).any()):
            print(Fore.CYAN + x + Style.RESET_ALL, end = " ")
        else:
            print(x, end = " ")
    print()
    print()
    print("\u0332".join(players[2]))
    print("S Tier: ", end = "")
    for x in availableSP3["Champion"]:
        if(allPicksP2["Champion"].str.contains(x).any() or allPicksP1["Champion"].str.contains(x).any() or allPicksP4["Champion"].str.contains(x).any() or allPicksP5["Champion"].str.contains(x).any()):
            print(Fore.CYAN + x + Style.RESET_ALL, end = " ")
        else:
            print(x, end = " ")
    print("\nA Tier: ", end = "")
    for x in availableAP3["Champion"]:
        if(allPicksP2["Champion"].str.contains(x).any() or allPicksP1["Champion"].str.contains(x).any() or allPicksP4["Champion"].str.contains(x).any() or allPicksP5["Champion"].str.contains(x).any()):
            print(Fore.CYAN + x + Style.RESET_ALL, end = " ")
        else:
            print(x, end = " ")
    print("\nB Tier: ", end = "")
    for x in availableBP3["Champion"]:
        if(allPicksP2["Champion"].str.contains(x).any() or allPicksP1["Champion"].str.contains(x).any() or allPicksP4["Champion"].str.contains(x).any() or allPicksP5["Champion"].str.contains(x).any()):
            print(Fore.CYAN + x + Style.RESET_ALL, end = " ")
        else:
            print(x, end = " ")
    print()
    print()
    print("\u0332".join(players[3]))
    print("S Tier: ", end = "")
    for x in availableSP4["Champion"]:
        if(allPicksP2["Champion"].str.contains(x).any() or allPicksP3["Champion"].str.contains(x).any() or allPicksP1["Champion"].str.contains(x).any() or allPicksP5["Champion"].str.contains(x).any()):
            print(Fore.CYAN + x + Style.RESET_ALL, end = " ")
        else:
            print(x, end = " ")
    print("\nA Tier: ", end = "")
    for x in availableAP4["Champion"]:
        if(allPicksP2["Champion"].str.contains(x).any() or allPicksP3["Champion"].str.contains(x).any() or allPicksP1["Champion"].str.contains(x).any() or allPicksP5["Champion"].str.contains(x).any()):
            print(Fore.CYAN + x + Style.RESET_ALL, end = " ")
        else:
            print(x, end = " ")
    print("\nB Tier: ", end = "")
    for x in availableBP4["Champion"]:
        if(allPicksP2["Champion"].str.contains(x).any() or allPicksP3["Champion"].str.contains(x).any() or allPicksP1["Champion"].str.contains(x).any() or allPicksP5["Champion"].str.contains(x).any()):
            print(Fore.CYAN + x + Style.RESET_ALL, end = " ")
        else:
            print(x, end = " ")
    print()
    print()
    print("\u0332".join(players[4]))
    print("S Tier: ", end = "")
    for x in availableSP5["Champion"]:
        if(allPicksP2["Champion"].str.contains(x).any() or allPicksP3["Champion"].str.contains(x).any() or allPicksP4["Champion"].str.contains(x).any() or allPicksP1["Champion"].str.contains(x).any()):
            print(Fore.CYAN + x + Style.RESET_ALL, end = " ")
        else:
            print(x, end = " ")
    print("\nA Tier: ", end = "")
    for x in availableAP5["Champion"]:
        if(allPicksP2["Champion"].str.contains(x).any() or allPicksP3["Champion"].str.contains(x).any() or allPicksP4["Champion"].str.contains(x).any() or allPicksP1["Champion"].str.contains(x).any()):
            print(Fore.CYAN + x + Style.RESET_ALL, end = " ")
        else:
            print(x, end = " ")
    print("\nB Tier: ", end = "")
    for x in availableBP5["Champion"]:
        if(allPicksP2["Champion"].str.contains(x).any() or allPicksP3["Champion"].str.contains(x).any() or allPicksP4["Champion"].str.contains(x).any() or allPicksP1["Champion"].str.contains(x).any()):
            print(Fore.CYAN + x + Style.RESET_ALL, end = " ")
        else:
            print(x, end = " ")
    print()
    print()
    
def pickedOrBanned(pickList, banList, pick):
    for champ in pickList:
        if(champ == pick):
            return True
    for champ in banList:
        if(champ == pick):
            return True
    return False


def searchTable(champTable, pick):
    booleans = []
    champFound = 0
    #The champ found part ended up being necessary becase champions like Kayle and Kayn have extremely high ratios
    for champ in champTable.Champion:
        if(champ == pick):
            champFound = 1
            booleans.append(True)
        else:
            booleans.append(False)
    if(champFound == 1):
        return booleans
    booleans = []
    for champ in champTable.Champion:
        if(SequenceMatcher(a=pick,b=champ).ratio()>.65 and pick[0].capitalize()==champ[0]):
            booleans.append(True)
        else:
            booleans.append(False)
    return booleans

def readPicksPart2(champTable, side, pickList, banList, players):
    partition = champTable
    if (side == "Blue"):     
        while (len(partition.Champion) != 1):
            displayPotentialPicks(champTable,pickList,banList,players)
            pick = input("Please enter enemy fourth pick: ").capitalize()
            partition = partition[searchTable(champTable,pick)]
            if(len(partition.Champion) != 1):
                print(Fore.YELLOW+ "Sorry that champion name was not recognized" +Style.RESET_ALL)
                partition = champTable
            elif(pickedOrBanned(pickList,banList,pick)):
                print(Fore.YELLOW + "Sorry that champion has been picked or banned already" +Style.RESET_ALL)
                partition = champTable
            else:    
                pickList.append(pick)               
        
        partition = champTable
        
        while (len(partition.Champion) != 1):
            displayPotentialPicks(champTable,pickList,banList,players)
            twoPicksBlue = input("Please enter your fourth and fifth picks (ie Jayce Gangplank): ").split()
            pick1 = twoPicksBlue[0].capitalize()
            pick2 = twoPicksBlue[1].capitalize()
            partition = partition[searchTable(champTable,pick1)]
            if(len(partition.Champion) != 1):
                print(Fore.YELLOW + "Sorry " +pick1+ " is not a champion we recognize" + Style.RESET_ALL)
                partition = champTable
                continue
            elif(pickedOrBanned(pickList,banList,pick1)):
                print(Fore.YELLOW + "Sorry " +pick1+ " has been picked or banned already" + Style.RESET_ALL)
                partition = champTable
                continue
            pick1 = partition.Champion.iloc[0]
            partition = champTable
            partition = partition[searchTable(champTable,pick2)]
            if(len(partition.Champion) != 1):
                print(Fore.YELLOW + "Sorry" +pick2+ "is not a champion we recognize" + Style.RESET_ALL)
                partition = champTable
                continue
            elif(pickedOrBanned(pickList,banList,pick2) or pick2 == pick1):
                print(Fore.YELLOW + "Sorry " +pick2+ " has been picked or banned already" + Style.RESET_ALL)
                partition = champTable
                continue
            pickList.append(pick1)
            pickList.append(pick2)
        
        partition = champTable
        
        while (len(partition.Champion) != 1):
            displayPotentialPicks(champTable,pickList,banList,players)
            pick = input("Please enter enemy fifth pick: ").capitalize()
            partition = partition[searchTable(champTable,pick)]
            if(len(partition.Champion) != 1):
                print(Fore.YELLOW+ "Sorry that champion name was not recognized" +Style.RESET_ALL)
                partition = champTable
            elif(pickedOrBanned(pickList,banList,pick)):
                print(Fore.YELLOW + "Sorry that champion has been picked or banned already" +Style.RESET_ALL)
                partition = champTable
            else:    
                pickList.append(pick) 

    elif side == "Red": 
        while (len(partition.Champion) != 1):
            displayPotentialPicks(champTable,pickList,banList,players)
            pick = input("Please enter your fourth pick: ").capitalize()
            partition = partition[searchTable(champTable,pick)]
            if(len(partition.Champion) != 1):
                print(Fore.YELLOW+ "Sorry that champion name was not recognized" +Style.RESET_ALL)
                partition = champTable
            elif(pickedOrBanned(pickList,banList,pick)):
                print(Fore.YELLOW + "Sorry that champion has been picked or banned already" +Style.RESET_ALL)
                partition = champTable
            else:    
                pickList.append(pick)               
        
        partition = champTable
        
        while (len(partition.Champion) != 1):
            displayPotentialPicks(champTable,pickList,banList,players)
            twoPicksBlue = input("Please enter enemy fourth and fifth picks (ie Jayce Gangplank): ").split()
            pick1 = twoPicksBlue[0].capitalize()
            pick2 = twoPicksBlue[1].capitalize()
            partition = partition[searchTable(champTable,pick1)]
            if(len(partition.Champion) != 1):
                print(Fore.YELLOW + "Sorry " +pick1+ " is not a champion we recognize" + Style.RESET_ALL)
                partition = champTable
                continue
            elif(pickedOrBanned(pickList,banList,pick1)):
                print(Fore.YELLOW + "Sorry " +pick1+ " has been picked or banned already" + Style.RESET_ALL)
                partition = champTable
                continue
            pick1 = partition.Champion.iloc[0]
            partition = champTable
            partition = partition[searchTable(champTable,pick2)]
            if(len(partition.Champion) != 1):
                print(Fore.YELLOW + "Sorry" +pick2+ "is not a champion we recognize" + Style.RESET_ALL)
                partition = champTable
                continue
            elif(pickedOrBanned(pickList,banList,pick2) or pick2 == pick1):
                print(Fore.YELLOW + "Sorry " +pick2+ " has been picked or banned already" + Style.RESET_ALL)
                partition = champTable
                continue
            pickList.append(pick1)
            pickList.append(pick2)
        
        partition = champTable
        
        while (len(partition.Champion) != 1):
            displayPotentialPicks(champTable,pickList,banList,players)
            pick = input("Please enter your fifth pick: ").capitalize()
            partition = partition[searchTable(champTable,pick)]
            if(len(partition.Champion) != 1):
                print(Fore.YELLOW+ "Sorry that champion name was not recognized" +Style.RESET_ALL)
                partition = champTable
            elif(pickedOrBanned(pickList,banList,pick)):
                print(Fore.YELLOW + "Sorry that champion has been picked or banned already" +Style.RESET_ALL)
                partition = champTable
            else:    
                pickList.append(pick) 
                
    return pickList

def readBansPart2(champTable, side, pickList, banList):
    partition = champTable
    if (side == "Blue"): 
        while (len(partition.Champion) != 1):
            pick = input("Please enter enemy fourth ban: ").capitalize()
            partition = partition[searchTable(champTable,pick)]
            if(len(partition.Champion) != 1):
                print(Fore.YELLOW + "Sorry that champion name was not recognized" + Style.RESET_ALL)
                partition = champTable
            elif(pickedOrBanned(pickList,banList,pick)):
                print(Fore.YELLOW + "Sorry that champion has been picked or banned already" + Style.RESET_ALL)
                partition = champTable
            else:    
                banList.append(partition.Champion.iloc[0])               
        
        partition = champTable
        
        while (len(partition.Champion) != 1):
            pick = input("Please enter your fourth ban: ").capitalize()
            partition = partition[searchTable(champTable,pick)]
            if(len(partition.Champion) != 1):
                print(Fore.YELLOW + "Sorry that champion name was not recognized" + Style.RESET_ALL)
                partition = champTable
            elif(pickedOrBanned(pickList,banList,pick)):
                print(Fore.YELLOW + "Sorry that champion has been picked or banned already" + Style.RESET_ALL)
                partition = champTable
            else:    
                banList.append(partition.Champion.iloc[0])               
        
        partition = champTable
        
        while (len(partition.Champion) != 1):
            pick = input("Please enter enemy fifth ban: ").capitalize()
            partition = partition[searchTable(champTable,pick)]
            if(len(partition.Champion) != 1):
                print(Fore.YELLOW + "Sorry that champion name was not recognized" + Style.RESET_ALL)
                partition = champTable
            elif(pickedOrBanned(pickList,banList,pick)):
                print(Fore.YELLOW + "Sorry that champion has been picked or banned already" + Style.RESET_ALL)
                partition = champTable
            else:    
                banList.append(partition.Champion.iloc[0])               
        
        partition = champTable
        
        while (len(partition.Champion) != 1):
            pick = input("Please enter your fifth ban: ").capitalize()
            partition = partition[searchTable(champTable,pick)]
            if(len(partition.Champion) != 1):
                print(Fore.YELLOW + "Sorry that champion name was not recognized" + Style.RESET_ALL)
                partition = champTable
            elif(pickedOrBanned(pickList,banList,pick)):
                print(Fore.YELLOW + "Sorry that champion has been picked or banned already" + Style.RESET_ALL)
                partition = champTable
            else:    
                banList.append(partition.Champion.iloc[0])               
        
    
    if (side == "Red"): 
        while (len(partition.Champion) != 1):
            pick = input("Please enter your fourth ban: ").capitalize()
            partition = partition[searchTable(champTable,pick)]
            if(len(partition.Champion) != 1):
                print(Fore.YELLOW + "Sorry that champion name was not recognized" + Style.RESET_ALL)
                partition = champTable
            elif(pickedOrBanned(pickList,banList,pick)):
                print(Fore.YELLOW + "Sorry that champion has been picked or banned already" + Style.RESET_ALL)
                partition = champTable
            else:    
                banList.append(partition.Champion.iloc[0])               
        
        partition = champTable
        
        while (len(partition.Champion) != 1):
            pick = input("Please enter enemy fourth ban: ").capitalize()
            partition = partition[searchTable(champTable,pick)]
            if(len(partition.Champion) != 1):
                print(Fore.YELLOW + "Sorry that champion name was not recognized" + Style.RESET_ALL)
                partition = champTable
            elif(pickedOrBanned(pickList,banList,pick)):
                print(Fore.YELLOW + "Sorry that champion has been picked or banned already" + Style.RESET_ALL)
                partition = champTable
            else:    
                banList.append(partition.Champion.iloc[0])               
        
        partition = champTable
        
        while (len(partition.Champion) != 1):
            pick = input("Please enter your fifth ban: ").capitalize()
            partition = partition[searchTable(champTable,pick)]
            if(len(partition.Champion) != 1):
                print(Fore.YELLOW + "Sorry that champion name was not recognized" + Style.RESET_ALL)
                partition = champTable
            elif(pickedOrBanned(pickList,banList,pick)):
                print(Fore.YELLOW + "Sorry that champion has been picked or banned already" + Style.RESET_ALL)
                partition = champTable
            else:    
                banList.append(partition.Champion.iloc[0])               
        
        partition = champTable
        
        while (len(partition.Champion) != 1):
            pick = input("Please enter enemy fifth ban: ").capitalize()
            partition = partition[searchTable(champTable,pick)]
            if(len(partition.Champion) != 1):
                print(Fore.YELLOW + "Sorry that champion name was not recognized" + Style.RESET_ALL)
                partition = champTable
            elif(pickedOrBanned(pickList,banList,pick)):
                print(Fore.YELLOW + "Sorry that champion has been picked or banned already" + Style.RESET_ALL)
                partition = champTable
            else:    
                banList.append(partition.Champion.iloc[0])   
    
    return banList

def readPicksPart1(champTable, side, pickList, banList, players):
    partition = champTable
    if (side == "Blue"):
        while (len(partition.Champion) != 1):
            displayPotentialPicks(champTable,pickList,banList,players)
            pick = input("Please enter your first pick: ").capitalize()
            partition = partition[searchTable(champTable,pick)]
            if(len(partition.Champion) != 1):
                print(Fore.YELLOW + "Sorry that champion name was not recognized" + Style.RESET_ALL)
                partition = champTable
            elif(pickedOrBanned(pickList,banList,pick)):
                print(Fore.YELLOW + "Sorry that champion has been picked or banned already" + Style.RESET_ALL)
                partition = champTable
            else:    
                pickList.append(partition.Champion.iloc[0])               
        
        partition = champTable
        
        while (len(partition.Champion) != 1):
            displayPotentialPicks(champTable,pickList,banList,players)
            twoPicksRed = input("Please enter enemy first and second picks (ie Jayce Gangplank): ").split()
            pick1 = twoPicksRed[0].capitalize()
            pick2 = twoPicksRed[1].capitalize()
            partition = partition[searchTable(champTable,pick1)]
            if(len(partition.Champion) != 1):
                print(Fore.YELLOW + "Sorry " +pick1+ " is not a champion we recognize" + Style.RESET_ALL)
                partition = champTable
                continue
            elif(pickedOrBanned(pickList,banList,pick1)):
                print(Fore.YELLOW + "Sorry " +pick1+ " has been picked or banned already" + Style.RESET_ALL)
                partition = champTable
                continue
            pick1 = partition.Champion.iloc[0]
            partition = champTable
            partition = partition[searchTable(champTable,pick2)]
            if(len(partition.Champion) != 1):
                print(Fore.YELLOW + "Sorry " +pick2+ " is not a champion we recognize" + Style.RESET_ALL)
                partition = champTable
                continue
            elif(pickedOrBanned(pickList,banList,pick2) or pick2 == pick1):
                print(Fore.YELLOW + "Sorry " +pick2+ " has been picked or banned already" + Style.RESET_ALL)
                partition = champTable
                continue
            pickList.append(pick1)
            pickList.append(partition.Champion.iloc[0])
        
        partition = champTable
        
        while (len(partition.Champion) != 1):
            displayPotentialPicks(champTable,pickList,banList,players)
            twoPicksBlue = input("Please enter your second and third picks (ie Jayce Gangplank): ").split()
            pick1 = twoPicksBlue[0].capitalize()
            pick2 = twoPicksBlue[1].capitalize()
            partition = partition[searchTable(champTable,pick1)]
            if(len(partition.Champion) != 1):
                print(Fore.YELLOW + "Sorry " +pick1+ " is not a champion we recognize" + Style.RESET_ALL)
                partition = champTable
                continue
            elif(pickedOrBanned(pickList,banList,pick1)):
                print(Fore.YELLOW + "Sorry " +pick1+ " has been picked or banned already" + Style.RESET_ALL)
                partition = champTable
                continue
            pick1 = partition.Champion.iloc[0]
            partition = champTable
            partition = partition[searchTable(champTable,pick2)]
            if(len(partition.Champion) != 1):
                print(Fore.YELLOW + "Sorry " +pick2+ " is not a champion we recognize" + Style.RESET_ALL)
                partition = champTable
                continue
            elif(pickedOrBanned(pickList,banList,pick2) or pick2 == pick1):
                print(Fore.YELLOW + "Sorry " +pick2+ " has been picked or banned already" + Style.RESET_ALL)
                partition = champTable
                continue
            pickList.append(pick1)
            pickList.append(partition.Champion.iloc[0])
        
        partition = champTable
        
        while (len(partition.Champion) != 1):
            displayPotentialPicks(champTable,pickList,banList,players)
            pick = input("Please enter enemy third pick: ").capitalize()
            partition = partition[searchTable(champTable,pick)]
            if(len(partition.Champion) != 1):
                print(Fore.YELLOW + "Sorry that champion name was not recognized" + Style.RESET_ALL)
                partition = champTable
            elif(pickedOrBanned(pickList,banList,pick)):
                print(Fore.YELLOW + "Sorry that champion has been picked or banned already" + Style.RESET_ALL)
                partition = champTable
            else:    
                pickList.append(partition.Champion.iloc[0])               
        
    if (side== "Red"):
        while (len(partition.Champion) != 1):
            displayPotentialPicks(champTable,pickList,banList,players)
            pick = input("Please enter enemy first pick: ").capitalize()
            partition = partition[searchTable(champTable,pick)]
            if(len(partition.Champion) != 1):
                print(Fore.YELLOW + "Sorry that champion name was not recognized" + Style.RESET_ALL)
                partition = champTable
            elif(pickedOrBanned(pickList,banList,pick)):
                print(Fore.YELLOW + "Sorry that champion has been picked or banned already" + Style.RESET_ALL)
                partition = champTable
            else:    
                pickList.append(partition.Champion.iloc[0])               
        
        partition = champTable
        
        while (len(partition.Champion) != 1):
            displayPotentialPicks(champTable,pickList,banList,players)
            twoPicksRed = input("Please enter your first and second picks (ie Jayce Gangplank): ").split()
            pick1 = twoPicksRed[0].capitalize()
            pick2 = twoPicksRed[1].capitalize()
            partition = partition[searchTable(champTable,pick1)]
            if(len(partition.Champion) != 1):
                print(Fore.YELLOW + "Sorry " +pick1+ " is not a champion we recognize" + Style.RESET_ALL)
                partition = champTable
                continue
            elif(pickedOrBanned(pickList,banList,pick1)):
                print(Fore.YELLOW + "Sorry " +pick1+ " has been picked or banned already" + Style.RESET_ALL)
                partition = champTable
                continue
            pick1 = partition.Champion.iloc[0]
            partition = champTable
            partition = partition[searchTable(champTable,pick2)]
            if(len(partition.Champion) != 1):
                print(Fore.YELLOW + "Sorry " +pick2+ " is not a champion we recognize" + Style.RESET_ALL)
                partition = champTable
                continue
            elif(pickedOrBanned(pickList,banList,pick2) or pick2 == pick1):
                print(Fore.YELLOW + "Sorry " +pick2+ " has been picked or banned already" + Style.RESET_ALL)
                partition = champTable
                continue
            pickList.append(pick1)
            pickList.append(partition.Champion.iloc[0])
        
        partition = champTable
        
        while (len(partition.Champion) != 1):
            displayPotentialPicks(champTable,pickList,banList,players)
            twoPicksBlue = input("Please enter enemy second and third picks (ie Jayce Gangplank): ").split()
            pick1 = twoPicksBlue[0].capitalize()
            pick2 = twoPicksBlue[1].capitalize()
            partition = partition[searchTable(champTable,pick1)]
            if(len(partition.Champion) != 1):
                print(Fore.YELLOW + "Sorry " +pick1+ " is not a champion we recognize" + Style.RESET_ALL)
                partition = champTable
                continue
            elif(pickedOrBanned(pickList,banList,pick1)):
                print(Fore.YELLOW + "Sorry " +pick1+ " has been picked or banned already" + Style.RESET_ALL)
                partition = champTable
                continue
            pick1 = partition.Champion.iloc[0]
            partition = champTable
            partition = partition[searchTable(champTable,pick2)]
            if(len(partition.Champion) != 1):
                print(Fore.YELLOW + "Sorry " +pick2+ " is not a champion we recognize" + Style.RESET_ALL)
                partition = champTable
                continue
            elif(pickedOrBanned(pickList,banList,pick2) or pick2 == pick1):
                print(Fore.YELLOW + "Sorry " +pick2+ " has been picked or banned already" + Style.RESET_ALL)
                partition = champTable
                continue
            pickList.append(pick1)
            pickList.append(partition.Champion.iloc[0])
        
        partition = champTable
        
        while (len(partition.Champion) != 1):
            displayPotentialPicks(champTable,pickList,banList,players)
            pick = input("Please enter your third pick: ").capitalize()
            partition = partition[searchTable(champTable,pick)]
            if(len(partition.Champion) != 1):
                print(Fore.YELLOW + "Sorry that champion name was not recognized" + Style.RESET_ALL)
                partition = champTable
            elif(pickedOrBanned(pickList,banList,pick)):
                print(Fore.YELLOW + "Sorry that champion has been picked or banned already" + Style.RESET_ALL)
                partition = champTable
            else:    
                pickList.append(partition.Champion.iloc[0])  
                
    return pickList
        

def readBansPart1(champTable, side, pickList, banList):
    partition = champTable
    if (side == "Blue"):
        while (len(partition.Champion) != 1):
            pick = input("Please enter your first ban: ").capitalize()
            partition = partition[searchTable(champTable,pick)]
            if(len(partition.Champion) != 1):
                print(Fore.YELLOW + "Sorry that champion name was not recognized" + Style.RESET_ALL)
                partition = champTable
            elif(pickedOrBanned(pickList,banList,pick)):
                print(Fore.YELLOW + "Sorry that champion has been picked or banned already" + Style.RESET_ALL)
                partition = champTable
            else:    
                banList.append(partition.Champion.iloc[0])               
        
        partition = champTable
        
        while (len(partition.Champion) != 1):
            pick = input("Please enter enemy first ban: ").capitalize()
            partition = partition[searchTable(champTable,pick)]
            if(len(partition.Champion) != 1):
                print(Fore.YELLOW + "Sorry that champion name was not recognized" + Style.RESET_ALL)
                partition = champTable
            elif(pickedOrBanned(pickList,banList,pick)):
                print(Fore.YELLOW + "Sorry that champion has been picked or banned already" + Style.RESET_ALL)
                partition = champTable
            else:    
                banList.append(partition.Champion.iloc[0])               
        
        partition = champTable
        
        while (len(partition.Champion) != 1):
            pick = input("Please enter your second ban: ").capitalize()
            partition = partition[searchTable(champTable,pick)]
            if(len(partition.Champion) != 1):
                print(Fore.YELLOW + "Sorry that champion name was not recognized" + Style.RESET_ALL)
                partition = champTable
            elif(pickedOrBanned(pickList,banList,pick)):
                print(Fore.YELLOW + "Sorry that champion has been picked or banned already" + Style.RESET_ALL)
                partition = champTable
            else:    
                banList.append(partition.Champion.iloc[0])               
        
        partition = champTable
        
        while (len(partition.Champion) != 1):
            pick = input("Please enter enemy second ban: ").capitalize()
            partition = partition[searchTable(champTable,pick)]
            if(len(partition.Champion) != 1):
                print(Fore.YELLOW + "Sorry that champion name was not recognized" + Style.RESET_ALL)
                partition = champTable
            elif(pickedOrBanned(pickList,banList,pick)):
                print(Fore.YELLOW + "Sorry that champion has been picked or banned already" + Style.RESET_ALL)
                partition = champTable
            else:    
                banList.append(partition.Champion.iloc[0])               
        
        partition = champTable
        
        while (len(partition.Champion) != 1):
            pick = input("Please enter your third ban: ").capitalize()
            partition = partition[searchTable(champTable,pick)]
            if(len(partition.Champion) != 1):
                print(Fore.YELLOW + "Sorry that champion name was not recognized" + Style.RESET_ALL)
                partition = champTable
            elif(pickedOrBanned(pickList,banList,pick)):
                print(Fore.YELLOW + "Sorry that champion has been picked or banned already" + Style.RESET_ALL)
                partition = champTable
            else:    
                banList.append(partition.Champion.iloc[0])               
        
        partition = champTable
        
        
        while (len(partition.Champion) != 1):
            pick = input("Please enter enemy third ban: ").capitalize()
            partition = partition[searchTable(champTable,pick)]
            if(len(partition.Champion) != 1):
                print(Fore.YELLOW + "Sorry that champion name was not recognized" + Style.RESET_ALL)
                partition = champTable
            elif(pickedOrBanned(pickList,banList,pick)):
                print(Fore.YELLOW + "Sorry that champion has been picked or banned already" + Style.RESET_ALL)
                partition = champTable
            else:    
                banList.append(partition.Champion.iloc[0])               
        
     
    if (side == "Red"):
        while (len(partition.Champion) != 1):
            pick = input("Please enter enemy first ban: ").capitalize()
            partition = partition[searchTable(champTable,pick)]
            if(len(partition.Champion) != 1):
                print(Fore.YELLOW + "Sorry that champion name was not recognized" + Style.RESET_ALL)
                partition = champTable
            elif(pickedOrBanned(pickList,banList,pick)):
                print(Fore.YELLOW + "Sorry that champion has been picked or banned already" + Style.RESET_ALL)
                partition = champTable
            else:    
                banList.append(partition.Champion.iloc[0])               
        
        partition = champTable
        
        while (len(partition.Champion) != 1):
            pick = input("Please enter your first ban: ").capitalize()
            partition = partition[searchTable(champTable,pick)]
            if(len(partition.Champion) != 1):
                print(Fore.YELLOW + "Sorry that champion name was not recognized" + Style.RESET_ALL)
                partition = champTable
            elif(pickedOrBanned(pickList,banList,pick)):
                print(Fore.YELLOW + "Sorry that champion has been picked or banned already" + Style.RESET_ALL)
                partition = champTable
            else:    
                banList.append(partition.Champion.iloc[0])               
        
        partition = champTable
        
        while (len(partition.Champion) != 1):
            pick = input("Please enter enemy second ban: ").capitalize()
            partition = partition[searchTable(champTable,pick)]
            if(len(partition.Champion) != 1):
                print(Fore.YELLOW + "Sorry that champion name was not recognized" + Style.RESET_ALL)
                partition = champTable
            elif(pickedOrBanned(pickList,banList,pick)):
                print(Fore.YELLOW + "Sorry that champion has been picked or banned already" + Style.RESET_ALL)
                partition = champTable
            else:    
                banList.append(partition.Champion.iloc[0])               
        
        partition = champTable
        
        while (len(partition.Champion) != 1):
            pick = input("Please enter your second ban: ").capitalize()
            partition = partition[searchTable(champTable,pick)]
            if(len(partition.Champion) != 1):
                print(Fore.YELLOW + "Sorry that champion name was not recognized" + Style.RESET_ALL)
                partition = champTable
            elif(pickedOrBanned(pickList,banList,pick)):
                print(Fore.YELLOW + "Sorry that champion has been picked or banned already" + Style.RESET_ALL)
                partition = champTable
            else:    
                banList.append(partition.Champion.iloc[0])               
        
        partition = champTable
        
        while (len(partition.Champion) != 1):
            pick = input("Please enter enemy third ban: ").capitalize()
            partition = partition[searchTable(champTable,pick)]
            if(len(partition.Champion) != 1):
                print(Fore.YELLOW + "Sorry that champion name was not recognized" + Style.RESET_ALL)
                partition = champTable
            elif(pickedOrBanned(pickList,banList,pick)):
                print(Fore.YELLOW + "Sorry that champion has been picked or banned already" + Style.RESET_ALL)
                partition = champTable
            else:    
                banList.append(partition.Champion.iloc[0])               
        
        partition = champTable
        
        
        while (len(partition.Champion) != 1):
            pick = input("Please enter your third ban: ").capitalize()
            partition = partition[searchTable(champTable,pick)]
            if(len(partition.Champion) != 1):
                print(Fore.YELLOW + "Sorry that champion name was not recognized" + Style.RESET_ALL)
                partition = champTable
            elif(pickedOrBanned(pickList,banList,pick)):
                print(Fore.YELLOW + "Sorry that champion has been picked or banned already" + Style.RESET_ALL)
                partition = champTable
            else:    
                banList.append(partition.Champion.iloc[0])  
        
    return banList
        

def searchPlayer(champTable, name):
    names = []
    for category in champTable:
        if(category == name and category != "Champion" and category != "Meta"):
            names.append(category)
            return names
    for category in champTable:
        if(SequenceMatcher(a=category,b=name).ratio()>.65 and name[0].capitalize()==category[0] and category != "Champion" and category != "Meta"):
            names.append(category)
            
    return names

def readSide():
    side = input("Please enter which side color you are: ").capitalize()
    return side

def readPlayers(champTable):
    players = []
    names = []
    while (len(names) != 1):
        playerToAdd = input("Please enter your top laner's name(ie Andy): ")
        names = searchPlayer(champTable, playerToAdd)
        if(len(names)!=1):
            print(Fore.YELLOW + "Sorry we do not have that player in our database" + Style.RESET_ALL)
            names = []
        else:
            players.append(names[0])
            
    names = []
    
    while (len(names) != 1):
        playerToAdd = input("Please enter your jungler's name(ie Jonathan): ")
        names = searchPlayer(champTable, playerToAdd)
        if(len(names)!=1):
            print(Fore.YELLOW + "Sorry we do not have that player in our database" + Style.RESET_ALL)
            names = []
        else:
            players.append(names[0])
            
    names = []
    
    while (len(names) != 1):
        playerToAdd = input("Please enter mid laner's name(ie Dustin): ")
        names = searchPlayer(champTable, playerToAdd)
        if(len(names)!=1):
            print(Fore.YELLOW + "Sorry we do not have that player in our database" + Style.RESET_ALL)
            names = []
        else:
            players.append(names[0])
            
    names = []
    
    while (len(names) != 1):
        playerToAdd = input("Please enter your bot laner's name(ie Mason): ")
        names = searchPlayer(champTable, playerToAdd)
        if(len(names)!=1):
            print(Fore.YELLOW + "Sorry we do not have that player in our database" + Style.RESET_ALL)
            names = []
        else:
            players.append(names[0])
            
    names = []
    
    while (len(names) != 1):
        playerToAdd = input("Please enter your support's name(ie Hwang): ")
        names = searchPlayer(champTable, playerToAdd)
        if(len(names)!=1):
            print(Fore.YELLOW + "Sorry we do not have that player in our database" + Style.RESET_ALL)
            names = []
        else:
            players.append(names[0])
            
    return players

def buildChampionList():
    championList = []
    aatrox = Champion.Champion("Aatrox", "Top")
    championList.append(aatrox)
    ahri = Champion.Champion("Ahri", "Mid")
    championList.append(ahri)
    akali = Champion.Champion("Akali","Mid")
    championList.append(akali)
    alistar = Champion.Champion("Alistar","Support")
    championList.append(alistar)
    amumu = Champion.Champion("Amumu","Jungle")
    championList.append(amumu)
    anivia = Champion.Champion("Anivia","Mid")
    championList.append(anivia)
    annie = Champion.Champion("Annie","Mid")
    championList.append(annie)
    ashe = Champion.Champion("Ashe","ADC")
    championList.append(ashe)
    aurelianSol = Champion.Champion("Aurelian Sol", "Mid")
    championList.append(aurelianSol)
    azir = Champion.Champion("Azir","Mid")
    championList.append(azir)
    bard = Champion.Champion("Bard","Support")
    championList.append(bard)
    blitzcrank = Champion.Champion("Blitzcrank","Support")
    championList.append(blitzcrank)
    brand = Champion.Champion("Brand","Support")
    championList.append(brand)
    braum = Champion.Champion("Braum","Support")
    championList.append(braum)
    caitlyn = Champion.Champion("Caitlyn","ADC")
    championList.append(caitlyn)
    camille = Champion.Champion("Camille","Top")
    championList.append(camille)
    cassiopeia = Champion.Champion("Cassiopeia","Mid")
    championList.append(cassiopeia)
    chogath = Champion.Champion("Chogath","Top")
    championList.append(chogath)
    corki = Champion.Champion("Corki","Mid")
    championList.append(corki)
    darius = Champion.Champion("Darius","Top")
    championList.append(darius)
    diana = Champion.Champion("Diana","Mid")
    championList.append(diana)
    drMundo = Champion.Champion("DrMundo","Top")
    championList.append(drMundo)
    draven = Champion.Champion("Draven","ADC")
    championList.append(draven)
    ekko = Champion.Champion("Ekko", "Mid")
    championList.append(ekko)
    elise = Champion.Champion("Elise","Jungle")
    championList.append(elise)
    evelynn = Champion.Champion("Evelynn","Jungle")
    championList.append(evelynn)
    ezreal = Champion.Champion("Ezreal","ADC")
    championList.append(ezreal)
    fiddlesticks = Champion.Champion("Fiddlesticks", "Jungle")
    championList.append(fiddlesticks)
    fiora = Champion.Champion("Fiora", "Top")
    championList.append(fiora)
    fizz = Champion.Champion("Fizz","Mid")
    championList.append(fizz)
    galio = Champion.Champion("Galio", "Mid")
    championList.append(galio)
    gangplank = Champion.Champion("Gangplank", "Top")
    championList.append(gangplank)
    garen = Champion.Champion("Garen", "Top")
    championList.append(garen)
    gnar = Champion.Champion("Gnar", "Top")
    championList.append(gnar)
    gragas = Champion.Champion("Gragas", "Jungle")
    championList.append(gragas)
    graves = Champion.Champion("Graves","Jungle")
    championList.append(graves)
    hecarim = Champion.Champion("Hecarim","Jungle")
    championList.append(hecarim)
    heimerdinger = Champion.Champion("Heimerdinger","Mid")
    championList.append(heimerdinger)
    illaoi = Champion.Champion("Illaoi", "Top")
    championList.append(illaoi)
    irelia = Champion.Champion("Irelia","Top")
    championList.append(irelia)
    ivern = Champion.Champion("Ivern","Jungle")
    championList.append(ivern)
    janna = Champion.Champion("Janna","Support")
    championList.append(janna)
    jarvanIV = Champion.Champion("Jarvan IV", "Jungle")
    championList.append(jarvanIV)
    jax = Champion.Champion("Jax","Top")
    championList.append(jax)
    jayce = Champion.Champion("Jayce","Top")
    championList.append(jayce)
    jhin = Champion.Champion("Jhin","ADC")
    championList.append(jhin)
    jinx = Champion.Champion("Jinx","ADC")
    championList.append(jinx)
    kaisa = Champion.Champion("Kaisa","ADC")
    championList.append(kaisa)
    kalista = Champion.Champion("Kalista","ADC")
    championList.append(kalista)
    karma = Champion.Champion("Karma","Support")
    championList.append(karma)
    karthus = Champion.Champion("Karthus","Jungle")
    championList.append(karthus)
    kassadin = Champion.Champion("Kassadin","Mid")
    championList.append(kassadin)
    katarina = Champion.Champion("Katarina","Mid")
    championList.append(katarina)
    kayle = Champion.Champion("Kayle","Top")
    championList.append(kayle)
    kayn = Champion.Champion("Kayn","Jungle")
    championList.append(kayn)
    kennen = Champion.Champion("Kennen","Top")
    championList.append(kennen)
    khazix = Champion.Champion("Khazix","Jungle")
    championList.append(khazix)
    kindred = Champion.Champion("Kindred","Jungle")
    championList.append(kindred)
    kled = Champion.Champion("Kled", "Top")
    championList.append(kled)
    kogmaw = Champion.Champion("Kogmaw","ADC")
    championList.append(kogmaw)
    leblanc = Champion.Champion("LeBlanc", "Mid")
    championList.append(leblanc)
    leesin = Champion.Champion("Lee Sin", "Jungle")
    championList.append(leesin)
    leona = Champion.Champion("Leona","Support")
    championList.append(leona)
    lissandra = Champion.Champion("Lissandra", "Mid")
    championList.append(lissandra)
    lucian = Champion.Champion("Lucian", "ADC")
    championList.append(lucian)
    lulu = Champion.Champion("Lulu", "Support")
    championList.append(lulu)
    lux = Champion.Champion("Lux","Support")
    championList.append(lux)
    malphite = Champion.Champion("Malphite","Top")
    championList.append(malphite)
    malzahar = Champion.Champion("Malzahar", "Mid")
    championList.append(malzahar)
    maokai = Champion.Champion("Maokai","Top")
    championList.append(maokai)
    masterYi = Champion.Champion("Master Yi", "Jungle")
    championList.append(masterYi)
    missFortune = Champion.Champion("Miss Fortune","ADC")
    championList.append(missFortune)
    mordekaiser = Champion.Champion("Mordekaiser", "Top")
    championList.append(mordekaiser)
    morgana = Champion.Champion("Morgana","Support")
    championList.append(morgana)
    nami = Champion.Champion("Nami", "Support")
    championList.append(nami)
    nasus = Champion.Champion("Nasus", "Top")
    championList.append(nasus)
    nautilus = Champion.Champion("Nautilus", "Support")
    championList.append(nautilus)
    neeko = Champion.Champion("Neeko","Mid")
    championList.append(neeko)
    nidalee = Champion.Champion("Nidalee","Jungle")
    championList.append(nidalee)
    nocturne = Champion.Champion("Nocturne","Jungle")
    championList.append(nocturne)
    nunu = Champion.Champion("Nunu", "Jungle")
    championList.append(nunu)
    olaf = Champion.Champion("Olaf", "Jungle")
    championList.append(olaf)
    orianna = Champion.Champion("Orianna", "Mid")
    championList.append(orianna)
    ornn = Champion.Champion("Ornn", "Top")
    championList.append(ornn)
    pantheon = Champion.Champion("Pantheon","Top")
    championList.append(pantheon)
    poppy = Champion.Champion("Poppy", "Top")
    championList.append(poppy)
    pyke = Champion.Champion("Pyke","Support")
    championList.append(pyke)
    qiyana = Champion.Champion("Qiyana", "Mid")
    championList.append(qiyana)
    quinn = Champion.Champion("Quinn", "Top")
    championList.append(quinn)
    rakan = Champion.Champion("Rakan", "Support")
    championList.append(rakan)
    rammus = Champion.Champion("Rammus", "Jungle")
    championList.append(rammus)
    reksai = Champion.Champion("Reksai", "Jungle")
    championList.append(reksai)
    renekton = Champion.Champion("Renekton","Top")
    championList.append(renekton)
    rengar = Champion.Champion("Rengar", "Jungle")
    championList.append(rengar)
    riven = Champion.Champion("Riven", "Top")
    championList.append(riven)
    rumble = Champion.Champion("Rumble", "Top")
    championList.append(rumble)
    ryze = Champion.Champion("Ryze", "Mid")
    championList.append(ryze)
    sejuani = Champion.Champion("Sejuani", "Jungle")
    championList.append(sejuani)
    shaco = Champion.Champion("Shaco", "Jungle")
    championList.append(shaco)
    shen = Champion.Champion("Shen", "Top")
    championList.append(shen)
    shyvana = Champion.Champion("Shyvana", "Jungle")
    championList.append(shyvana)
    singed = Champion.Champion("Singed", "Top")
    championList.append(singed)
    sion = Champion.Champion("Sion", "Top")
    championList.append(sion)
    sivir = Champion.Champion("Sivir", "ADC")
    championList.append(sivir)
    skarner = Champion.Champion("Skarner", "Jungle")
    championList.append(skarner)
    sona = Champion.Champion("Sona", "Support")
    championList.append(sona)
    soraka = Champion.Champion("Soraka","Support")
    championList.append(soraka)
    swain = Champion.Champion("Swain", "Mid")
    championList.append(swain)
    sylas = Champion.Champion("Sylas", "Mid")
    championList.append(sylas)
    syndra = Champion.Champion("Syndra", "Mid")
    championList.append(syndra)
    tahmKench = Champion.Champion("Tahm Kench", "Support")
    championList.append(tahmKench)
    taliyah = Champion.Champion("Taliyah", "Mid")
    championList.append(taliyah)
    talon = Champion.Champion("Talon", "Mid")
    championList.append(talon)
    taric = Champion.Champion("Taric", "Support")
    championList.append(taric)
    teemo = Champion.Champion("Teemo", "Top")
    championList.append(teemo)
    thresh = Champion.Champion("Thresh", "Support")
    championList.append(thresh)
    tristana = Champion.Champion("Tristana", "ADC")
    championList.append(tristana)
    trundle = Champion.Champion("Trundle", "Jungle")
    championList.append(trundle)
    tryndamere = Champion.Champion("Tryndamere", "Top")
    championList.append(tryndamere)
    twistedFate = Champion.Champion("Twisted Fate", "Mid")
    championList.append(twistedFate)
    twitch = Champion.Champion("Twitch", "ADC")
    championList.append(twitch)
    udyr = Champion.Champion("Udyr", "Jungle")
    championList.append(udyr)
    urgot = Champion.Champion("Urgot", "Top")
    championList.append(urgot)
    varus = Champion.Champion("Varus", "ADC")
    championList.append(varus)
    vayne = Champion.Champion("Vayne", "ADC")
    championList.append(vayne)
    veigar = Champion.Champion("Veigar", "Mid")
    championList.append(veigar)
    velkoz = Champion.Champion("Velkoz", "Mid")
    championList.append(velkoz)
    vi = Champion.Champion("Vi", "Jungle")
    championList.append(vi)
    viktor = Champion.Champion("Viktor", "Mid")
    championList.append(viktor)
    vladimir = Champion.Champion("Vladimir", "Mid")
    championList.append(vladimir)
    volibear = Champion.Champion("Volibear", "Jungle")
    championList.append(volibear)
    warwick = Champion.Champion("Warwick", "Jungle")
    championList.append(warwick)
    wukong = Champion.Champion("Wukong", "Top")
    championList.append(wukong)
    xayah = Champion.Champion("Xayah", "ADC")
    championList.append(xayah)
    xerath = Champion.Champion("Xerath", "Mid")
    championList.append(xerath)
    xin = Champion.Champion("Xin Zhao", "Jungle")
    championList.append(xin)
    yasuo = Champion.Champion("Yasuo", "Mid")
    championList.append(yasuo)
    yorick = Champion.Champion("Yorick", "Top")
    championList.append(yorick)
    yuumi = Champion.Champion("Yuumi", "Support")
    championList.append(yuumi)
    zac = Champion.Champion("Zac", "Jungle")
    championList.append(zac)
    zed = Champion.Champion("Zed", "Mid")
    championList.append(zed)
    ziggs = Champion.Champion("Ziggs", "Mid")
    championList.append(ziggs)
    zilean = Champion.Champion("Zilean", "Support")
    championList.append(zilean)
    zoe = Champion.Champion("Zoe", "Mid")
    championList.append(zoe)
    zyra = Champion.Champion("Zyra", "Support")
    championList.append(zyra)
    championDict = {}
    for x in championList:
        championDict[x.name] = x
    return championDict
