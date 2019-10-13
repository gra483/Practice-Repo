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

def printPlayer(players, playerIndex, availableS, availableA, availableB, allPicksP2, allPicksP3, allPicksP4, allPicksP5):
    print("\u0332".join(players[playerIndex]))
    print("S Tier: ", end = "")
    for x in availableS["Champion"]:
        if(allPicksP2["Champion"].str.contains(x).any() or allPicksP3["Champion"].str.contains(x).any() or allPicksP4["Champion"].str.contains(x).any() or allPicksP5["Champion"].str.contains(x).any()):
            print(Fore.CYAN + x + Style.RESET_ALL, end = " ")
        else:
            print(x, end = " ")
    print("\nA Tier: ", end = "")
    for x in availableA["Champion"]:
        if(allPicksP2["Champion"].str.contains(x).any() or allPicksP3["Champion"].str.contains(x).any() or allPicksP4["Champion"].str.contains(x).any() or allPicksP5["Champion"].str.contains(x).any()):
            print(Fore.CYAN + x + Style.RESET_ALL, end = " ")
        else:
            print(x, end = " ")
    print("\nB Tier: ", end = "")
    for x in availableB["Champion"]:
        if(allPicksP2["Champion"].str.contains(x).any() or allPicksP3["Champion"].str.contains(x).any() or allPicksP4["Champion"].str.contains(x).any() or allPicksP5["Champion"].str.contains(x).any()):
            print(Fore.CYAN + x + Style.RESET_ALL, end = " ")
        else:
            print(x, end = " ")    
    print()
    print()

        
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
        printPlayer(players, 0, availableSP1, availableAP1, availableBP1, allPicksP2, allPicksP3, allPicksP4, allPicksP5)
    if(not unique(pickList[0], poolP2, poolP1, poolP3, poolP4, poolP5)):
        printPlayer(players, 1, availableSP2, availableAP2, availableBP2, allPicksP1, allPicksP3, allPicksP4, allPicksP5)
    if(not unique(pickList[0], poolP3, poolP2, poolP1, poolP4, poolP5)):
        printPlayer(players, 2, availableSP3, availableAP3, availableBP3, allPicksP1, allPicksP2, allPicksP4, allPicksP5)
    if(not unique(pickList[0], poolP4, poolP2, poolP3, poolP1, poolP5)):
        printPlayer(players, 3, availableSP4, availableAP4, availableBP4, allPicksP1, allPicksP2, allPicksP3, allPicksP5)
    if(not unique(pickList[0], poolP5, poolP2, poolP3, poolP4, poolP1)):
        printPlayer(players, 4, availableSP5, availableAP5, availableBP5, allPicksP1, allPicksP2, allPicksP3, allPicksP4)
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

def getPick(partition, champTable, pickList, banList, players, youOrEnemy, number):
    while (len(partition.Champion) != 1):
            displayPotentialPicks(champTable,pickList,banList,players)
            pick = input("Please enter " + youOrEnemy + " " + number + " pick: ").capitalize()
            partition = partition[searchTable(champTable,pick)]
            if(len(partition.Champion) != 1):
                print(Fore.YELLOW+ "Sorry that champion name was not recognized" +Style.RESET_ALL)
                partition = champTable
            elif(pickedOrBanned(pickList,banList,pick)):
                print(Fore.YELLOW + "Sorry that champion has been picked or banned already" +Style.RESET_ALL)
                partition = champTable
            else:
                if(youOrEnemy == "your"):
                    pickList[0].append(pick)   
                else:
                    pickList[1].append(pick)
    return pickList

def getBan(partition, champTable, pickList, banList, youOrEnemy, number):
    while (len(partition.Champion) != 1):
            pick = input("Please enter " + youOrEnemy + " " + number + " ban: ").capitalize()
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
        
def readPicksPart2(champTable, side, pickList, banList, players):
    partition = champTable
    if (side == "Blue"):           
        pickList = getPick(partition, champTable, pickList, banList, players, "enemy", "fourth")        
        partition = champTable
        
        pickList = getPick(partition, champTable, pickList, banList, players, "your" , "fourth")
        partition = champTable
        
        pickList = getPick(partition, champTable, pickList, banList, players, "your" , "fifth")
        partition = champTable
        
        pickList = getPick(partition, champTable, pickList, banList, players, "enemy" , "fifth")

    elif (side == "Red"): 
        pickList = getPick(partition, champTable, pickList, banList, players, "your", "fourth")        
        partition = champTable
        
        pickList = getPick(partition, champTable, pickList, banList, players, "enemy" , "fourth")
        partition = champTable
        
        pickList = getPick(partition, champTable, pickList, banList, players, "enemy" , "fifth")
        partition = champTable
        
        pickList = getPick(partition, champTable, pickList, banList, players, "your" , "fifth")
                
    return pickList

def readBansPart2(champTable, side, pickList, banList):
    partition = champTable
    if (side == "Blue"): 
        
        banList = getBan(partition, champTable, pickList, banList, "enemy", "fourth")
        partition = champTable
        
        banList = getBan(partition, champTable, pickList, banList, "your", "fourth")
        partition = champTable
        
        banList = getBan(partition, champTable, pickList, banList, "enemy", "fifth")
        partition = champTable
        
        banList = getBan(partition, champTable, pickList, banList, "your", "fifth")
        partition = champTable
    
    if (side == "Red"): 
        
        banList = getBan(partition, champTable, pickList, banList, "your", "fourth")
        partition = champTable
        
        banList = getBan(partition, champTable, pickList, banList, "enemy", "fourth")
        partition = champTable
        
        banList = getBan(partition, champTable, pickList, banList, "your", "fifth")
        partition = champTable
        
        banList = getBan(partition, champTable, pickList, banList, "enemy", "fifth")
        partition = champTable
    
    return banList

def readPicksPart1(champTable, side, pickList, banList, players):
    partition = champTable
    if (side == "Blue"):
        pickList = getPick(partition, champTable, pickList, banList, players, "your", "first")        
        partition = champTable
        
        pickList = getPick(partition, champTable, pickList, banList, players, "enemy" , "first")
        partition = champTable
        
        pickList = getPick(partition, champTable, pickList, banList, players, "enemy" , "second")
        partition = champTable
        
        pickList = getPick(partition, champTable, pickList, banList, players, "your" , "second")           
        partition = champTable
        
        pickList = getPick(partition, champTable, pickList, banList, players, "your" , "third")           
        partition = champTable
        
        pickList = getPick(partition, champTable, pickList, banList, players, "enemy" , "third")           
    
        
    if (side== "Red"):
        pickList = getPick(partition, champTable, pickList, banList, players, "enemy", "first")        
        partition = champTable
        
        pickList = getPick(partition, champTable, pickList, banList, players, "your" , "first")
        partition = champTable
        
        pickList = getPick(partition, champTable, pickList, banList, players, "your" , "second")
        partition = champTable
        
        pickList = getPick(partition, champTable, pickList, banList, players, "enemy" , "second")           
        partition = champTable
        
        pickList = getPick(partition, champTable, pickList, banList, players, "enemy" , "third")           
        partition = champTable
        
        pickList = getPick(partition, champTable, pickList, banList, players, "your" , "third")           
        
            
    return pickList
        

def readBansPart1(champTable, side, pickList, banList):
    partition = champTable
    if (side == "Blue"):
        banList = getBan(partition, champTable, pickList, banList, "your", "first")
        partition = champTable
        
        banList = getBan(partition, champTable, pickList, banList, "enemy", "first")
        partition = champTable
        
        banList = getBan(partition, champTable, pickList, banList, "your", "second")
        partition = champTable
        
        banList = getBan(partition, champTable, pickList, banList, "enemy", "second")
        partition = champTable       
        
        banList = getBan(partition, champTable, pickList, banList, "your", "third")
        partition = champTable 
        
        banList = getBan(partition, champTable, pickList, banList, "enemy", "third")
        partition = champTable 
        
     
    if (side == "Red"):
        banList = getBan(partition, champTable, pickList, banList, "enemy", "first")
        partition = champTable
        
        banList = getBan(partition, champTable, pickList, banList, "your", "first")
        partition = champTable
        
        banList = getBan(partition, champTable, pickList, banList, "enemy", "second")
        partition = champTable
        
        banList = getBan(partition, champTable, pickList, banList, "your", "second")
        partition = champTable       
        
        banList = getBan(partition, champTable, pickList, banList, "enemy", "third")
        partition = champTable 
        
        banList = getBan(partition, champTable, pickList, banList, "your", "third")
        partition = champTable  
        
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

def getSubs(names, champTable):
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

def getLaner(names, champTable, players, lane):
    while (len(names) != 1):
        playerToAdd = input("Please enter your " + lane + "'s name: ")
        names = searchPlayer(champTable, playerToAdd)
        if(len(names)!=1):
            print(Fore.YELLOW + "Sorry we do not have that player in our database" + Style.RESET_ALL)
            names = []
        else:
            players.append(names[0])
            return players

def readPlayers(champTable):
    players = []
    names = []
    preSet = ""
    while(not(preSet == "A" or preSet == "B" or preSet == "C" or preSet == "U" or preSet == "a" or preSet == "b" or preSet == "c" or preSet == "u") ):
        preSet = input("What team is playing? A for Premier, B for Academy, C for Ice Cream, U for unique (You can pick a preset then choose subs too): " )
        if(not(preSet == "A" or preSet == "B" or preSet == "C" or preSet == "U" or preSet == "a" or preSet == "b" or preSet == "c" or preSet == "u") ):
            print(Fore.YELLOW + "Sorry we do not recognize that team" + Style.RESET_ALL)

    if(preSet == "A" or preSet == "a"):
        names = ["Andy", "Jonathan", "Dustin", "Mason", "Hwang"]
        players = getSubs(names, champTable)
        
    elif(preSet == "B" or preSet == "b"):
        names = ["Kevin", "Denis", "Ben", "Tailer", "Tanner"]
        players = getSubs(names, champTable)
        
    elif(preSet == "C" or preSet == "c"):
        names = ["Clayton", "Praveen", "Alex", "Micheal", "Lim"]
        players = getSubs(names, champTable)
        
    elif(preSet == "U" or preSet == "u"):
        players = getLaner(names, champTable, players, "Top")
        names = []
        
        players = getLaner(names, champTable, players, "Jungle")
        names = []
        
        players = getLaner(names, champTable, players, "Mid")
        names = []
        
        players = getLaner(names, champTable, players, "ADC")
        names = []
        
        players = getLaner(names, champTable, players, "Support")
            
    return players
