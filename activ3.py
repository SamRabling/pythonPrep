# class Card(object):
#     def __init__(self, suit, value):
#         self.suit = suit
#         self.value = value
# def makeCards():
#     cards = []
#     suits = ['hearts', 'spades', 'clubs', 'diamond']
#     for s in suits:
#         print s
#         for v in range(1, 14):
#             car= ('{}'+ '{}').format(v, s)
#             cards.append(car)
# makeCards()

class Card(object):
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    def printCard(self):
        print "Suit: {}, Value: {}".format(self.suit, self.value)

class Deck(object):
    def __init__(self):
        self.cards = []
        for s in ("hearts", "diamond", "clubs", "spades"):
            for v in range(1,14):
                self.cards.append(Card(s, v))
    print self.cards
# hearts = []   
# spades = []
# cloves = []
# diamonds = []    
# for i in range(1, 14):

#     hearts.append(['card'+ str(i)+': [{'value: '+str(i)+', 'suit':'hearts''}])
# print hearts

# class Deck(object):
#     def __init__(self, cards):
#         self.suit = suit
#         self.value = value

#     def createDeck(self):

#     def shuffleDeck(self):

#     def dealDeck(self):

#     def retireDeck(self):