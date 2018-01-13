class Deck:
    """tracks cards left in deck and deals cards"""

    def __init__(self):
        """Create new deck of cards and shuffle it"""
        self.cards = {'A \u2660': 1, 'A \u2661': 1, 'A \u2662': 1, 'A \u2663': 1, '2 \u2660': 2, '2 \u2661': 2,'2 \u2662': 2,
                 '2 \u2663': 2, '3 \u2660': 3, '3 \u2661': 3, '3 \u2662': 3, '3 \u2663': 3, '4 \u2660': 4,'4 \u2661': 4,
                 '4 \u2662': 4, '4 \u2663': 4, '5 \u2660': 5, '5 \u2661': 5, '5 \u2662': 5, '5 \u2663': 5,'6 \u2660': 6,
                 '6 \u2661': 6, '6 \u2662': 6, '6 \u2663': 6, '7 \u2660': 7, '7 \u2661': 7, '7 \u2662': 7,'7 \u2663': 7,
                 '8 \u2660': 8, '8 \u2661': 8, '8 \u2662': 8, '8 \u2663': 8, '9 \u2660': 9, '9 \u2661': 9,'9 \u2662': 9,
                 '9 \u2663': 9, '10 \u2660': 10, '10 \u2661': 10, '10 \u2662': 10, '10 \u2663': 10, 'Jack \u2660': 11,
                 'Jack \u2661': 11, 'Jack \u2662': 11, 'Jack \u2663': 11, 'Queen \u2660': 12, 'Queen \u2661': 12,
                 'Queen \u2662': 12, 'Queen \u2663': 12, 'King \u2660': 13, 'King \u2661': 13, 'King \u2662': 13,
                 'King \u2663': 13}

        possibleCards = list(self.cards.keys())
        print(possibleCards)
        import random
        shuffledDeck = list()
        # while len(possibleCards)!=0:
        for a in self.cards:
            y = random.randint(0, (len(possibleCards) - 1))  ##generating numbers higher than expected range
            shuffledDeck.append(possibleCards[y])
            possibleCards.remove(possibleCards[y])

        self.deck= shuffledDeck

    def pDeck(self):
        for i in self.deck:
            print(i)

    def getCard(self):
        #self.pDeck()
        card=self.deck.pop(0)
        return card

    def getCardNumber(self, card):
        #print(self.cards.get(card)," should be the number of this card")
        return int(self.cards.get(card))

    def shufDeck(self):
        possibleCards=list(self.cards.keys())
        print(possibleCards)
        import random
        shuffledDeck = list()
        # while len(possibleCards)!=0:
        y = random.randint(0, (len(self.cards.keys()) - 1))  ##generating numbers higher than expected range
        shuffledDeck.append(possibleCards[y])
        possibleCards.remove(possibleCards[y])
        return shuffledDeck

    def getLength(self):
        return len(self.deck)