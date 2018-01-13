from Deck import Deck
import random

playerHand = list()
playerMatches = 0
computerHand = list()
computerMatches = 0
deck=Deck()
Deck.shufDeck(deck)
gameOn=""

def reinitialize():
    global playerMatches
    global computerMatches
    playerHand.clear()
    playerMatches = 0
    computerHand.clear()
    computerMatches = 0

def isNum(s): #Check if the input is an integer
    try:
        int(s)
        print ("I'm an int!")
        return True
    except:
        print ("I'm not an int!")
        return False

def incrementPlayerMatches(): #Keeps track of how many matches the player has made
    global playerMatches
    playerMatches=playerMatches+1

def incrementComputerMatches(): #Keeps track of how many matches the computer has made
    global computerMatches
    computerMatches=computerMatches+1

def dealHands():
    for i in range(0, 5):  ##five cards in starting hand
        playerHand.append(deck.getCard())
        computerHand.append(deck.getCard())

def displayHand():
    for card in playerHand:
        print(playerHand.index(card)+1,'\t',card)

def win():
    global gameOn
    if computerMatches>playerMatches:
        print("The computer won. Better luck next time.")
    else:
        print("Congratulations, you won!")
    print("Good bye!")
    #i =input("Type y if you would like to play again and anything else to quit.")
    #if i=='y':
    #    reinitialize()
    #    return
    #else:
    #    gameOn='n'
    #    return

def isMatch(hand):
    for card in hand:
        for cardB in hand:
            if (deck.getCardNumber(card)==deck.getCardNumber(cardB)) & (card != cardB):
                return deck.getCardNumber(card)
    return 0

def checkMatch (hand, card):
    cards=0
    for i in hand:
        if deck.getCardNumber(i)==deck.getCardNumber(card):
            cards=cards+1
    if cards <2:
        print("That card does not have a match.")
        return False
    else:
        return True

def checkMatchNum (hand, number):
    cards=0
    for i in hand:
        if deck.getCardNumber(i)==int(number):
            cards=cards+1
    if cards ==0:
        return False
    else:
        return True
def choice1():
    cardIndex = int(input("Please the number to the left of one of the cards in your pair."))
    cardIndex = cardIndex - 1  # allow for starting with 0
    print (playerHand[cardIndex]) #prints correct card
    #print (deck.getCardNumber(playerHand[cardIndex])) #prints number of card
    matchNum = int(deck.getCardNumber(playerHand[cardIndex]))  # get the value of that card (eg. 13 for king)
    #print (matchNum+"= what we send to checkMatch function")
    if checkMatch(playerHand, playerHand[cardIndex]):
        # for card in playerHand: #check each card in the hand for matches with the specified number THIS SHOULD BE IT's OWN FUNCTION, could pass hand in question and use for both player and computer? then call if wrong card selected (see comment on line 110)
        #    if (deck.getCardNumber(card)==matchNum) & (card !=playerHand[cardIndex]):
        #        playerHand.remove(playerHand[cardIndex]) #remove this card first, because I have the index, which might change if you remove something else from the list
        #        playerHand.remove(card)
        makeMatch(playerHand, matchNum)
        incrementPlayerMatches()
        if (len(playerHand) == 0) | (len(computerHand) == 0) | (deck.getLength() == 0) | (computerMatches > 14):
            win()
        else:
            displayHand()
            input("Type any key to end your turn.")
            return
    elif not checkMatch(playerHand, matchNum): #if no match for chosen card, try again.
        ch=input("If you meant to select option 2, type 2 now.")
        if ch=='2':
            choice2()
        else:
            choice1()

def choice2():
    print("Cards can be requested by typing a number, 1-13.  An Ace is 1, a King is 13.")
    choice = input("Type in the number of the card you want.")

    if (isNum(choice)):
        cardRequest(choice)

    else:
        choice = input("Please enter a number between 1 and 13.")
        cardRequest(choice)


def makeMatch (hand, card):
    removed = 0
    while removed <2:
        for i in hand:
            if deck.getCardNumber(i) == int(card):
                hand.remove(i)
                removed= removed + 1

def cardRequest(choice): #choice is an integer entered by player
    #used when the player requests a card from the computer.  Not working right now (3:44 pm 1/12/18)
    # TODO: does not return card that is actually present in computer hand.
     choice=int(choice)
     if checkMatchNum(computerHand,choice):
         removed=0
         while removed < 1:
             for a in computerHand:

                 if deck.getCardNumber(a)== choice:
                     playerHand.append(a)
                     computerHand.remove(a)
                     if checkMatchNum(playerHand,choice):
                         makeMatch(playerHand,choice)
                         incrementPlayerMatches()
                         print("You made a match!")
                         if (len(playerHand) == 0) | (len(computerHand) == 0) | (deck.getLength() == 0) | (
                             computerMatches > 14):
                             win()
                     removed=removed+1
     else:
         input("I do not have that card. Type any key to Go Fish.")
         playerHand.append(deck.getCard())

     displayHand()
     input("Type any key to end your turn.")
     return


def computerTurn():
    print(" ")
    print('The computer has ', computerMatches, ' matches so far.')
    print('You have ', playerMatches, ' matches so far.')
    print("Now it's the computer's turn.")


    for a in computerHand:
        print(a)
    if (len(playerHand)==0) | (len(computerHand)==0) | (deck.getLength()==0) | (computerMatches>14):
        win()
    else:
    #while (len(computerHand) !=0) & (len(deck) !=0) & (computerMatches <27):#if 27 or greater, there is no possibility of computer loosing
        #TODO: check matches with function
        #for card in computerHand:  # check each card in the hand for matches
        #    for c in computerHand:
        #        if (deck.getCardNumber(card)==deck.getCardNumber(c)) & (card !=c): #if you have a match
        #            computerHand.remove(card)
        #            computerHand.remove(c)
        card=isMatch(computerHand)
        if card >0:
            makeMatch(computerHand, card)
            incrementComputerMatches()
            if (len(computerHand) == 0) | (deck.getLength() == 0) | (computerMatches > 14):
                win()
            else:
                print("The computer made a match! Now it's your turn.")
            return
        else: #no match
            reqInd=random.randint (0,(len(computerHand)-1))#get random index for card request
            print("there are ",len(computerHand), " cards in the computer's hand. Index for req is ", reqInd)
            request=deck.getCardNumber(computerHand[reqInd])
            ans=input("Do you have a "+ str( request)+"? Type y if you do, anything else if you don't.") #ask about a random card from hand
            if ans=='y': #if player does have requested card
                computerHand.remove(computerHand[reqInd]) #changed from reqInd to computerHand[reqInd]
                for c in playerHand:
                    print("current card is ",c)
                    if deck.getCardNumber(c)==request:
                        playerHand.remove(c)
                        makeMatch(computerHand,deck.getCardNumber(c))
                        incrementComputerMatches()
                        if (len(computerHand) == 0) | (deck.getLength() == 0) | (computerMatches > 14):
                            win()
                        else:
                            return
            else: #draw card if player says they don't have requested card
                computerHand.append(deck.getCard())
                return

def playerTurn():
    if (len(playerHand)==0) | (len(computerHand)==0) | (deck.getLength()==0) | (playerMatches>14):
        win()
    else:
    #while (len(playerHand) !=0) & (len(deck) !=0) & (playerMatches <27):#if 27 or greater, there is no possibility of player loosing
        print(" ")
        print('The computer has ',computerMatches, ' matches so far.')
        print('You have ',playerMatches,' matches so far.')
        print("Your hand is: ")
        displayHand()
        action = input("To play a matching pair, type 1.  To request a card from the computer, type 2.")
        if (action == '1'):
            choice1()

        elif (action == '2'):
            choice2()

def main ():
    gameOn=input("Would you like to play Go Fish? Type y to play.")
    if gameOn=='y':
        dealHands()
    while gameOn=='y':
        playerTurn()
        computerTurn()

main()
