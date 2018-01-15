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
        #print ("I'm an int!")
        return True
    except:
        print ("Please enter an integer")
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

def displayPHand():
    print("")
    print("Your hand is:")
    for card in playerHand:
        print(playerHand.index(card)+1,'\t',card)

def displayCHand():
    print("")
    print("My hand is:")
    for a in computerHand:
        print(computerHand.index(a)+1, '\t',a)

def win():
    global gameOn
    if computerMatches>playerMatches:
        print("The computer won. Better luck next time.")
    elif playerMatches>computerMatches:
        print("Congratulations, you won!")
    elif playerMatches==computerMatches:
        print("We tied!  Good job.")
    print("Good bye!")
    gameOn='n'

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
    cardIndex = int(input("Please enter the number to the left of one of the cards in your pair."))
    cardIndex = cardIndex - 1  # shift for index starting at 0
    matchNum = int(deck.getCardNumber(playerHand[cardIndex]))  # get the value of that card (eg. 13 for king)
    if checkMatch(playerHand, playerHand[cardIndex]):
        makeMatch(playerHand, matchNum)
        incrementPlayerMatches()
        if (len(playerHand)==0) | (len(computerHand)==0) | (deck.getLength()==0) | (computerMatches>14 | (playerMatches>14)):
            win()
        else:
            displayPHand()
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
    #choice = input("Type in the number of the card you want.")

    while True:
        choice = input("Type in the number of the card you want.")
        if ((isNum(choice)) & (int(choice)>0) & (int(choice)<14)):
            cardRequest(int(choice))
            break
        elif isNum(choice)==False | (int(choice)<1) | (int(choice)>13):
            print("Please enter an integer between 1 and 13.")

def makeMatch (hand, card):  #Only use after verifying that match exists
    removed = 0
    c=list()
    while removed <2:
        for i in hand:
            if deck.getCardNumber(i) == int(card):
                c.append(i)
                hand.remove(i)
                removed= removed + 1
    #TODO Check if this works or makes trouble.
    if removed !=2: #in case there isn't a match (this should never happen, but who knows?)
        print("no match found.")
        for a in c:
            hand.append(a)

def cardRequest(choice): #choice is an integer entered by player representing the number of the card they hope to receive
     choice=int(choice)
     #print("choice is ",choice)
     if checkMatchNum(computerHand,choice):
         print("I have that card.  Here you go.")
         removed=0
         while removed < 1:
             for a in computerHand:
                 if deck.getCardNumber(a)== choice:
                     playerHand.append(a)
                     computerHand.remove(a)
                     m=isMatch(playerHand)
                     if m>0:
                         makeMatch(playerHand,m)
                         incrementPlayerMatches()
                         print("You made a match!")
                         if (len(playerHand)==0) | (len(computerHand)==0) | (deck.getLength()==0) | (computerMatches>14 | (playerMatches>14)):
                             win()
                     removed=removed+1
             break
     else:
         input("I do not have that card. Type any key to Go Fish.")
         c=deck.getCard()
         playerHand.append(c)
         print ("\nYou drew a "+c)


     input("Type any key to end your turn.")
     return


def computerTurn():
    print(" ")
    print('The computer has ', computerMatches, ' matches so far.')
    print('You have ', playerMatches, ' matches so far.')
    print("Now it's the computer's turn.")

    if (len(playerHand)==0) | (len(computerHand)==0) | (deck.getLength()==0) | (computerMatches>14 | (playerMatches>14)):
        win()
    else:
        #TODO Turn off displayCHand for final version.  Useful for debugging.
        displayCHand()
        card=isMatch(computerHand)
        if card >0:
            makeMatch(computerHand, card)
            incrementComputerMatches()
            if (len(playerHand)==0) | (len(computerHand)==0) | (deck.getLength()==0) | (computerMatches>14 | (playerMatches>14)):
                win()
            else:
                print("The computer made a match! Now it's your turn.")
            return
        else: #no match
            reqInd=random.randint (0,(len(computerHand)-1))#get random index for card request
            #print("there are ",len(computerHand), " cards in the computer's hand. Index for reqInd is ", reqInd)
            request=deck.getCardNumber(computerHand[reqInd])
            #TODO: test the following to see if it produces the desired output (ie names face cards.)Maybe make into seperate function?
            requestCard=''
            if request==11:
                requestCard=' Jack'
            elif request==12:
                requestCard=' Queen'
            elif request==13:
                requestCard=' King'
            elif request==1:
                requestCard='n Ace'
            else:
                requestCard=" "+str(request)
            ans=input("Do you have a"+ requestCard +"? Type y if you do, anything else if you don't.") #ask about a random card from hand
            if ans=='y': #if player does have requested card
                print("Thank you!")
                for c in playerHand:
                    #print("current card is ",c)
                    if deck.getCardNumber(c)==request:
                        computerHand.append(c)
                        playerHand.remove(c)
                        makeMatch(computerHand,deck.getCardNumber(c))
                        incrementComputerMatches()
                        if (len(playerHand)==0) | (len(computerHand)==0) | (deck.getLength()==0) | (computerMatches>14 | (playerMatches>14)):
                            win()
                        else:
                            return
            else: #draw card if player says they don't have requested card
                computerHand.append(deck.getCard())
                return

def playerTurn():
    global gameOn
    if (len(playerHand)==0) | (len(computerHand)==0) | (deck.getLength()==0) | (computerMatches>14 | (playerMatches>14)):
        win()
    else:
    #while (len(playerHand) !=0) & (len(deck) !=0) & (playerMatches <27):#if 27 or greater, there is no possibility of player loosing
        print(" ")
        print('The computer has ',computerMatches, ' matches so far.')
        print('You have ',playerMatches,' matches so far.')
        displayPHand()
        action=''
        while (action !='1') & (action !='2') & (action !='EXIT'):
            action = input("To play a matching pair, type 1.  To request a card from the computer, type 2. To end game, type EXIT.")

            if (action == '1'):
                choice1()

            elif (action == '2'):
                choice2()

            elif (action == 'EXIT'):
                gameOn='n'

def main ():
    global gameOn
    gameOn=input("Would you like to play Go Fish? Type y to play.")
    if gameOn=='y':
        dealHands()
    while gameOn=='y':
        playerTurn()
        computerTurn()


main()
