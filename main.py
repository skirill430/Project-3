from mtgsdk import Card
from array import array
import time 
import string
import collections
import mergeSort
from randomCards import randomCards

print("------------------------------------------------")
print("Welcome to the Magic the Gathering card library!")
print("------------------------------------------------")
print("Choose cards:")
print("1. Normal cards")
print("2. Exclusive cards")
print(" ")
#set deck flag to either 1 or 2
deckSel = input("Select: ")
if(deckSel == '1' or deckSel == '2'):
    print(" ")
else:
    exit()
print("Select from options below: ")
print("1. Display all cards")
print("2. Display cards of a certain amount")
print("3. Sort cards with different algorithms")
print(" ")
#set the menu selection 
menuSelect = input ("Select: ")
print("------------------------------------------------")
#Display all normal cards
if(menuSelect == '1' and deckSel == '1'): 
    print("You've selected to display all cards!")
    print("The cards: ")
    pageNum = 0
    count1 = 0
    for x in range(650):
        #checkpoints to stop the count
        if(count1 == 1000):
            checkContinue = input("Continue? Y/N:")
            if(checkContinue == 'Y'):
                continue
            else:
                exit()
        count1 = count1 + 1
        cards1 = Card.where(page=x).where(pageSize=100).all()
        #display the cards
        for i in cards1:
            print(i.name)

#Display all exclusive cards
elif(menuSelect == '1' and deckSel == '2'): 
    print("You've selected to display all cards!")
    print("The cards: ")
    count = 0
    #loop through 100,000 data points
    for i in range(100000):
        count = count + 1
        #checkpoints to stop the count
        if(count == 500):
            checkContinue = input("Continue? Y/N:")
            if(checkContinue == 'Y'):
                continue
            else:
                exit()
        elif(count == 1000):
            checkContinue = input("Continue? Y/N:")
            if(checkContinue == 'Y'):
                continue
            else:
                exit()
        elif(count == 2000):
            checkContinue = input("Continue? Y/N:")
            if(checkContinue == 'Y'):
                continue
            else:
                exit()
        #display the cards
        print(randomCards.name())

#Display normal cards of a certain page 
elif(menuSelect == '2' and deckSel == '1'):
    print("You've selected to display a page of cards!")
    print(" ")
    pageNum = input("Select a page number between 1 and 1310: ")
    cards2 = Card.where(page=pageNum).where(pageSize=50).all()
    print(" ")
    #print the card names
    print("The cards: ")
    for x in cards2:
        print(x.name)
    #display more features
    print(" ")
    displayFeature = input("Would you like to display additional features of the cards? Y/N: ")
    if(displayFeature == 'N'or displayFeature == 'n'):
        exit()
    elif(displayFeature == 'Y' or displayFeature == 'y'):
        print("------------------------------------------------")
        print("Choose a feature from the following categories: ")
        print("1. Mana Cost")
        print("2. Type")
        print("3. Supertype")
        print("4. Subtype")
        print("5. Rarity") 
        print("6. Number")
        print("7. ID")
        print(" ")
        displayOption = input("Select: ")
        #print out the specified information with the card's name
        if(displayOption == '1'):
            print(" ")
            print("Cards and their mana cost: ")
            for x in cards2:
                res = collections.ChainMap(x.name, x.mana_cost)
                print(res.maps,'\n')
        elif(displayOption == '2'):
            print(" ")
            print("Cards and their type: ")
            for x in cards2:
                res = collections.ChainMap(x.name, x.type)
                print(res.maps,'\n')
        elif(displayOption == '3'):
            print(" ")
            print("Cards and their supertypes: ")
            for x in cards2:
                res = collections.ChainMap(x.name, x.supertypes)
                print(res.maps,'\n')
        elif(displayOption == '4'):
            print(" ")
            print("Cards and their subtypes: ")
            for x in cards2:
                res = collections.ChainMap(x.name, x.subtypes)
                print(res.maps,'\n')
        elif(displayOption == '5'):
            print(" ")
            print("Cards and their rarity: ")
            for x in cards2:
                res = collections.ChainMap(x.name, x.rarity)
                print(res.maps,'\n')
        elif(displayOption == '6'):
            print(" ")
            print("Cards and their number: ")
            for x in cards2:
                res = collections.ChainMap(x.name, x.number)
                print(res.maps,'\n')
        elif(displayOption == '7'):
            print(" ")
            print("Cards and their ID: ")
            for x in cards2:
                res = collections.ChainMap(x.name, x.id)
                print(res.maps,'\n')
        else:
            print("Invalid input")
            exit()   
    else:
        print("Invalid Input")
        exit()
#Display random cards in certain amount
elif(menuSelect == '2' and deckSel == '2'):
    print("You've selected to display a page of cards!")
    print(" ")
    totalNum = input("Select an amount of cards: ")
    print(" ")
    randCards = []
    #print the card names
    print("The cards: ")
    for i in range(int(totalNum)):
        randCards.append(randomCards.name())
        print(randomCards.name())
    #display more features
    print(" ")
    displayFeature = input("Would you like to display additional features of the cards? Y/N: ")
    if(displayFeature == 'N' or displayFeature == 'n'):
        exit()
    elif(displayFeature == 'Y' or displayFeature == 'y'):
        print("------------------------------------------------")
        print("Choose a feature from the following categories: ")
        print("1. Mana Cost")
        print("2. Type")
        print("3. Supertype")
        print("4. Subtype")
        print("5. Rarity") 
        print("6. Number")
        print("7. ID")
        print(" ")
        displayOption = input("Select: ")    
        if(displayOption == '1'):
            print(" ")
            print("Cards and their mana cost: ")
            for x in randCards:
                res = collections.ChainMap(x, randomCards.manaCost())
                print(res.maps,'\n')

        if(displayOption == '2'):
            print(" ")
            print("Cards and their type: ")
            for x in randCards:
                res = collections.ChainMap(x, randomCards.type())
                print(res.maps,'\n')
        if(displayOption == '3'):
            print(" ")
            print("Cards and their supertype: ")
            for x in randCards:
                res = collections.ChainMap(x, randomCards.supertype())
                print(res.maps,'\n')
        if(displayOption == '4'):
            print(" ")
            print("Cards and their subtype: ")
            for x in randCards:
                res = collections.ChainMap(x, randomCards.subtype())
                print(res.maps,'\n')
        if(displayOption == '5'):
            print(" ")
            print("Cards and their rarity: ")
            for x in randCards:
                res = collections.ChainMap(x, randomCards.rarity())
                print(res.maps,'\n')
        if(displayOption == '6'):
            print(" ")
            print("Cards and their number: ")
            for x in randCards:
                res = collections.ChainMap(x, randomCards.number())
                print(res.maps,'\n')
        if(displayOption == '7'):
            print(" ")
            print("Cards and their ID: ")
            for x in randCards:
                res = collections.ChainMap(x, randomCards.id())
                print(res.maps,'\n')
        else:
            exit()
    else:
        print("Invalid Input")
        exit()

#Sort the normal cards
elif(menuSelect == '3' and deckSel == '1'):
    print("You've selected to sort cards by mana cost!")
    print(" ")
    print("Select which option to sort: ")
    print("1. All cards")
    print("2. Page of cards")
    print(" ")
    sizeSel = input("Select: ")
    cardList = []
    if sizeSel == '1':
        cards3 = []
        count = 0
        for x in range(1310):
            count = count + 1
            #checkpoints to stop the count
            if(count == 250):
                checkContinue = input("Continue? Y/N:")
                if(checkContinue == 'Y'):
                    continue
                else:
                    break
            elif(count == 500):
                checkContinue = input("Continue? Y/N:")
                if(checkContinue == 'Y'):
                    continue
                else:
                    break
            elif(count == 1000):
                checkContinue = input("Continue? Y/N:")
                if(checkContinue == 'Y'):
                    continue
                else:
                    break
            cards3 = cards3 + Card.where(page=x).where(pageSize=50).all() 
        #Add all the cards to a list// have to display every page
    elif sizeSel == '2':
        pageNum3 = input("Select which page of cards to sort between 1 and 650: ")
        print(" ")
        cards3 = Card.where(page=pageNum3).where(pageSize=100).all()
    else:
        print("Invalid Input")
        exit()
    
    print("Select which sorting algorithm: ")
    print("1. Merge Sort")
    print("2. Quick Sort")
    print("3. Time of both algorithms")
    print(" ")
    sortChoice = input("Select: ")
    print("------------------------------------------------")
    print(" ")
    if(sortChoice == '1'):
        #add the card info into an array
        cardsArr = []
        mapCards = {}
        cardTracker=[]
        breakFor = False
        for x in cards3: #for every card is list, get their mana cost
            cardsArr.append(x.cmc)
            mapCards[x.name] = x.cmc
            cardTracker.append(x.name)
        #perform merge sort and display
        print("Cards sorted with merge sort: ")
        mergedCards = mergeSort.mergeSortAlg(cardsArr)
        for i in mergedCards:
            for key, value in mapCards.items():#dict can't change size
                if(value == i):#equal to cmc1
                    breakFor = False
                    if (key in cardTracker):
                        tempKey = key
                        cardTracker.remove(key)
                        break
            res = collections.ChainMap(i ,tempKey)
            print(res.maps,'\n')  
    elif(sortChoice == '2'):
        #INSERT QUICK SORT CALL HERE
        print(" ")
    elif(sortChoice == '3'):
        #CALL MERGE AND TIME
        mergestart = time.time()
        cardsArr = []
        mapCards = {}
        cardTracker=[]
        breakFor = False
        for x in cards3: #for every card is list, get their mana cost
            cardsArr.append(x.cmc)
            mapCards[x.name] = x.cmc
            cardTracker.append(x.name)
        #perform merge sort and display
        print("Cards sorted with merge sort: ")
        mergedCards = mergeSort.mergeSortAlg(cardsArr)
        for i in mergedCards:
            for key, value in mapCards.items():#dict can't change size
                if(value == i):#equal to cmc1
                    breakFor = False
                    if (key in cardTracker):
                        tempKey = key
                        cardTracker.remove(key)
                        break
            res = collections.ChainMap(i ,tempKey)
            print(res.maps,'\n')
        mergeend = time.time()
        print("Merge sort computation: (in seconds)")
        print(round(mergeend - mergestart,5))
        #CALL QUICK AND TIME
        #PRINT THEIR TIMES
        print(" ")



#Sort the random cards
elif(menuSelect == '3' and deckSel == '2'):
    print("You've selected to sort cards by mana cost!")
    print(" ")
    print("Select which option to sort: ")
    print("1. All cards")
    print("2. Certain number of cards")
    print(" ")
    sizeSel = input("Select: ")
    print("------------------------------------------------")
    print(" ")
    randCardList = []
    cmcList = []
    if sizeSel == '1':
        for i in range(100000):
            randCardList.append(randomCards.name())
            cmcList.append(randomCards.cost())
    elif sizeSel == '2':
        numCardsSort = input("How many cards: ")
        for i in range(int(numCardsSort)):
            randCardList.append(randomCards.name())
            cmcList.append(randomCards.cost())
    else:
        print("Invalid Input")
        exit()
    print(" ")
    print("Select which sorting algorithm: ")
    print("1. Merge Sort")
    print("2. Quick Sort")
    print("3. Time of both algorithms")
    print(" ")
    sortChoice = input("Select: ")
    if(sortChoice == '1'):
        #perform merge sort and display
        print("Mana Cost sorted with merge sort: ")
        mergedCardsRand = mergeSort.mergeSortAlg(cmcList)
        for i in mergedCardsRand:
            for y in randCardList:
                res = collections.ChainMap(i, y)
                print(res.maps,'\n')
                #GET THESE TO PRINT ONE AT A TIME// fix all cards
    elif(sortChoice == '2'):
        #INSERT QUICK SORT CALL HERE
        print(" ")
    elif(sortChoice == '3'):
        #CALL MERGE AND TIME
        #CALL QUICK AND TIME
        #PRINT THEIR TIMES
        print(" ")
else:
    exit()
