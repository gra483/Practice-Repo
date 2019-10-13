# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 17:05:39 2019

@author: gavin
"""


from difflib import SequenceMatcher  
from colorama import Fore
from colorama import Style


def unique(allyPickList, allPicksPlayer, allPicks1, allPicks2, allPicks3, allPicks4):
    for pick in allyPickList:
        if(allPicksPlayer["Champion"].str.contains(pick).any() and not allPicks1["Champion"].str.contains(pick).any() and not allPicks2["Champion"].str.contains(pick).any() and not allPicks3["Champion"].str.contains(pick).any() and not allPicks4["Champion"].str.contains(pick).any()):
           return True
    return False

def displayPotentialPicks(champTable, pickList, banList, players):
    champFilter = champTable.Champion.str.contains('|'.join(pickList[0] + pickList[1] +banList))
    potentialPicks = champTable[[not x for x in champFilter]]
    
    poolP1 = champTable[champTable[players[0]]<4]
    allPicksP1 = potentialPicks[potentialPicks[players[0]]<4]
    availableSP1 = potentialPicks[potentialPicks[players[0]]==1]
    availableAP1 = potentialPicks[potentialPicks[players[0]]==2]
    availableBP1 = potentialPicks[potentialPicks[players[0]]==3]
    
    poolP2 = champTable[champTable[players[1]]<4]
    allPicksP2 = potentialPicks[potentialPicks[players[1]]<4]
    availableSP2 = potentialPicks[potentialPicks[players[1]]==1]
    availableAP2 = potentialPicks[potentialPicks[players[1]]==2]
    availableBP2 = potentialPicks[potentialPicks[players[1]]==3]
    
    poolP3 = champTable[champTable[players[2]]<4]
    allPicksP3 = potentialPicks[potentialPicks[players[2]]<4]
    availableSP3 = potentialPicks[potentialPicks[players[2]]==1]
    availableAP3 = potentialPicks[potentialPicks[players[2]]==2]
    availableBP3 = potentialPicks[potentialPicks[players[2]]==3]
    
    poolP4 = champTable[champTable[players[3]]<4]
    allPicksP4 = potentialPicks[potentialPicks[players[3]]<4]
    availableSP4 = potentialPicks[potentialPicks[players[3]]==1]
    availableAP4 = potentialPicks[potentialPicks[players[3]]==2]
    availableBP4 = potentialPicks[potentialPicks[players[3]]==3]
    
    poolP5 = champTable[champTable[players[4]]<4]
    allPicksP5 = potentialPicks[potentialPicks[players[4]]<4]
    availableSP5 = potentialPicks[potentialPicks[players[4]]==1]
    availableAP5 = potentialPicks[potentialPicks[players[4]]==2]
    availableBP5 = potentialPicks[potentialPicks[players[4]]==3]
       

   #really just a bunch of print statements to print each players picks, highlighted if flex
   #pprobably would have been faster to get a list of flex picks first, but I just checked every time b/c it works
     
    print()
    print()
    print("OPEN PICKS: \n")
    if(not unique(pickList[0], poolP1, poolP2, poolP3, poolP4, poolP5)):
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
    if(not unique(pickList[0], poolP2, poolP1, poolP3, poolP4, poolP5)):
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
    if(not unique(pickList[0], poolP3, poolP2, poolP1, poolP4, poolP5)):
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
    if(not unique(pickList[0], poolP4, poolP2, poolP3, poolP1, poolP5)):
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
    if(not unique(pickList[0], poolP5, poolP2, poolP3, poolP4, poolP1)):
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
                pickList[1].append(pick)               
        
        partition = champTable
        
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
                pickList[0].append(pick)               
        
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
                pickList[0].append(pick)               
        
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
                pickList[1].append(pick) 

    elif (side == "Red"): 
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
                pickList[0].append(pick)               
        
        partition = champTable
        
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
                pickList[1].append(pick)               
        
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
                pickList[1].append(pick)               
        
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
                pickList[0].append(pick) 
                
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
                pickList[0].append(partition.Champion.iloc[0])               
        
        partition = champTable
        
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
                pickList[1].append(partition.Champion.iloc[0])               
        
        partition = champTable 
        
        while (len(partition.Champion) != 1):
            displayPotentialPicks(champTable,pickList,banList,players)
            pick = input("Please enter enemy second pick: ").capitalize()
            partition = partition[searchTable(champTable,pick)]
            if(len(partition.Champion) != 1):
                print(Fore.YELLOW + "Sorry that champion name was not recognized" + Style.RESET_ALL)
                partition = champTable
            elif(pickedOrBanned(pickList,banList,pick)):
                print(Fore.YELLOW + "Sorry that champion has been picked or banned already" + Style.RESET_ALL)
                partition = champTable
            else:    
                pickList[1].append(partition.Champion.iloc[0])               
        
        partition = champTable
        
        while (len(partition.Champion) != 1):
            displayPotentialPicks(champTable,pickList,banList,players)
            pick = input("Please enter your second pick: ").capitalize()
            partition = partition[searchTable(champTable,pick)]
            if(len(partition.Champion) != 1):
                print(Fore.YELLOW + "Sorry that champion name was not recognized" + Style.RESET_ALL)
                partition = champTable
            elif(pickedOrBanned(pickList,banList,pick)):
                print(Fore.YELLOW + "Sorry that champion has been picked or banned already" + Style.RESET_ALL)
                partition = champTable
            else:    
                pickList[0].append(partition.Champion.iloc[0])               
        
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
                pickList[0].append(partition.Champion.iloc[0])               
        
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
                pickList[1].append(partition.Champion.iloc[0])               
        
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
                pickList[1].append(partition.Champion.iloc[0])               
        
        partition = champTable
        
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
                pickList[0].append(partition.Champion.iloc[0])               
        
        partition = champTable 
        
        while (len(partition.Champion) != 1):
            displayPotentialPicks(champTable,pickList,banList,players)
            pick = input("Please enter your second pick: ").capitalize()
            partition = partition[searchTable(champTable,pick)]
            if(len(partition.Champion) != 1):
                print(Fore.YELLOW + "Sorry that champion name was not recognized" + Style.RESET_ALL)
                partition = champTable
            elif(pickedOrBanned(pickList,banList,pick)):
                print(Fore.YELLOW + "Sorry that champion has been picked or banned already" + Style.RESET_ALL)
                partition = champTable
            else:    
                pickList[0].append(partition.Champion.iloc[0])               
        
        partition = champTable
        
        while (len(partition.Champion) != 1):
            displayPotentialPicks(champTable,pickList,banList,players)
            pick = input("Please enter enemy second pick: ").capitalize()
            partition = partition[searchTable(champTable,pick)]
            if(len(partition.Champion) != 1):
                print(Fore.YELLOW + "Sorry that champion name was not recognized" + Style.RESET_ALL)
                partition = champTable
            elif(pickedOrBanned(pickList,banList,pick)):
                print(Fore.YELLOW + "Sorry that champion has been picked or banned already" + Style.RESET_ALL)
                partition = champTable
            else:    
                pickList[1].append(partition.Champion.iloc[0])               
        
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
                pickList[1].append(partition.Champion.iloc[0])               
        
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
                pickList[0].append(partition.Champion.iloc[0])   
            
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
    preSet = ""
    role = "1"
    while(not(preSet == "A" or preSet == "B" or preSet == "C" or preSet == "U" or preSet == "a" or preSet == "b" or preSet == "c" or preSet == "u") ):
        preSet = input("What team is playing? A for Premier, B for Academy, C for Ice Cream, U for unique (You can pick a preset then choose subs too): " )
        if(not(preSet == "A" or preSet == "B" or preSet == "C" or preSet == "U" or preSet == "a" or preSet == "b" or preSet == "c" or preSet == "u") ):
            print(Fore.YELLOW + "Sorry we do not recognize that team" + Style.RESET_ALL)

    if(preSet == "A" or preSet == "a"):
        names = ["Andy", "Jonathan", "Dustin", "Mason", "Hwang"]
        while(1):
            indicator = input("Will anybody else be subbing in? If not, type done, otherwise type anything (note Jan is considered a Sub): ")
            if(indicator == "done" or indicator == "Done"):
                return names
            else:
                playerToAdd = input("Please enter the name of the player subbing: ")
                namesHelp = searchPlayer(champTable, playerToAdd)
                if(len(namesHelp)!=1):
                    print(Fore.YELLOW + "Sorry we do not have that player in our database" + Style.RESET_ALL)
                    namesHelp = []
                else:
                    while(1):
                        role = input("What role will " + namesHelp[0] + " be playing? 1 for top, 2 for jungle.... 5 for support: ")
                        if("1" in role):
                            names[0] = namesHelp[0]
                            break
                        elif("2" in role):
                            names[1] = namesHelp[0]
                            break
                        elif("3" in role):
                            names[2] = namesHelp[0]
                            break
                        elif("4" in role):
                            names[3] = namesHelp[0]
                            break
                        elif("5" in role):
                            names[4] = namesHelp[0]
                            break
                        else:
                            print("We do not recognize that role")
    elif(preSet == "B" or preSet == "b"):
        names = ["Kevin", "Denis", "Ben", "Tailer", "Tanner"]
        while(1):
            indicator = input("Will anybody else be subbing in? If not, type done, otherwise type anything: ")
            if(indicator == "done" or indicator == "Done"):
                return names
            else:
                playerToAdd = input("Please enter the name of the player subbing: ")
                namesHelp = searchPlayer(champTable, playerToAdd)
                if(len(namesHelp)!=1):
                    print(Fore.YELLOW + "Sorry we do not have that player in our database" + Style.RESET_ALL)
                    namesHelp = []
                else:
                    while(1):
                        role = input("What role will " + namesHelp[0] + " be playing? 1 for top, 2 for jungle.... 5 for support: ")
                        if("1" in role):
                            names[0] = namesHelp[0]
                            break
                        elif("2" in role):
                            names[1] = namesHelp[0]
                            break
                        elif("3" in role):
                            names[2] = namesHelp[0]
                            break
                        elif("4" in role):
                            names[3] = namesHelp[0]
                            break
                        elif("5" in role):
                            names[4] = namesHelp[0]
                            break
                        else:
                            print("We do not recognize that role")
    elif(preSet == "C" or preSet == "c"):
        names = ["Clayton", "Praveen", "Alex", "Micheal", "Lim"]
        while(1):
            indicator = input("Will anybody else be subbing in? If not, type done, otherwise type anything: ")
            if(indicator == "done" or indicator == "Done"):
                return names
            else:
                playerToAdd = input("Please enter the name of the player subbing: ")
                namesHelp = searchPlayer(champTable, playerToAdd)
                if(len(namesHelp)!=1):
                    print(Fore.YELLOW + "Sorry we do not have that player in our database" + Style.RESET_ALL)
                    namesHelp = []
                else:
                    while(1):
                        role = input("What role will " + namesHelp[0] + " be playing? 1 for top, 2 for jungle.... 5 for support: ")
                        if("1" in role):
                            names[0] = namesHelp[0]
                            break
                        elif("2" in role):
                            names[1] = namesHelp[0]
                            break
                        elif("3" in role):
                            names[2] = namesHelp[0]
                            break
                        elif("4" in role):
                            names[3] = namesHelp[0]
                            break
                        elif("5" in role):
                            names[4] = namesHelp[0]
                            break
                        else:
                            print("We do not recognize that role")
    elif(preSet == "U" or preSet == "u"):
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
