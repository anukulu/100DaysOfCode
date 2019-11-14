import random

class Card:
    def __init__(self, name, color):
        self.name = name
        self.color = color

class Deck:
    def __init__(self):
        self.newDeck = []
        self.colors = ['C', 'D', 'H', 'S']
        self.numbers = [i for i in range(1,14)]
    
    def MakeDeck(self):
        for color in self.colors:
            for number in self.numbers:
                self.newDeck.append(Card(number, color))

    def ShuffleDeck(self, deck):
        random.shuffle(deck)
        return deck

    def ShowDeck(self):
        for card in self.newDeck:
            print(str(card.name) + card.color)
    

class Player:
    def __init__(self):
        self.cards = []

    def ReceiveCards(self, card):
        self.cards.append(card)

deckOfCards = Deck()
deckOfCards.MakeDeck()
deckOfCards.ShuffleDeck(deckOfCards.newDeck)
deckOfCards.ShowDeck()

players = []
numberOfPLayers = int(input('Enter the number of players'))
if (numberOfPLayers > 1 and numberOfPLayers < 6):
    for i  in range(numberOfPLayers):
        newPlayer = Player()
        players.append(newPlayer)
    for i in range(5):
        for player in players:
            player.ReceiveCards(deckOfCards.newDeck.pop())
    
    for player in players:
        for card in player.cards:
            print(str(card.name) + card.color)
        print('\n')
else:
    print('The game is not possible')
