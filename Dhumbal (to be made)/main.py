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
    
    def MakeNewDeck(self):
        for color in self.colors:
            for number in self.numbers:
                self.newDeck.append(Card(number, color))

    def ShuffleDeck(self, deck):
        random.shuffle(deck)
        return deck

    def MakeDeck(self, randomDeck):
        smallerDeck = self.ShuffleDeck(randomDeck)
        self.newDeck = smallerDeck

    def ShowDeck(self):
        for card in self.newDeck:
            print(str(card.name) + card.color)
    

class Player:
    def __init__(self):
        self.cards = []

    def ReceiveCards(self, card):
        self.cards.append(card)
    
    def PickCard(self, singleCard):
        pass

    def Throw(self):
        pass
          


deckOfCards = Deck()
deckOfCards.MakeNewDeck()
deckOfCards.ShuffleDeck(deckOfCards.newDeck)

players = []
numberOfPLayers = int(input('Enter the number of players : '))
if (numberOfPLayers > 1 and numberOfPLayers < 6):
    for i  in range(numberOfPLayers):
        newPlayer = Player()
        players.append(newPlayer)
    for i in range(5):
        for player in players:
            player.ReceiveCards(deckOfCards.newDeck.pop())
    
    # beginning the game
    show = False
    playerIndex = 0
    throwncards = []
    rounds = 0
    while(not show):
        currentPlayer = players[playerIndex]
        # The player needs to throw a card first and then pick a card
        if(rounds == 0):
            # just throw the cards and pick one from deck
            newCard = deckOfCards.newDeck.pop()
            

            

        playerIndex += 1
        playerIndex = playerIndex % numberOfPLayers
        

    

    # for player in players:
    #     for card in player.cards:
    #         print(str(card.name) + card.color)
    #     print('\n')
else:
    print('The game is not possible')
