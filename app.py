from cards import Card
from deck import Deck
from player import Player
import json



class Game:
    def __init__(self, cardfile, numPlayers = 3, handSize = 5, expantions = ['Base']):
        self.deck = Deck(cardfile, expantions)
        self.players = [Player(self.deck, size=handSize) for _ in range(numPlayers)]
        self.players[0].cardmaster = True
    
    def run(self):
        for player in self.players:
            print(player.display_hand())
            print(player.cardmaster)
            print(self.deck)
    
    
            

game = Game("cards.json")
game.run()


'''
Game Loop:
    Deal cards
    Delegate cardmaster
    draw question card
        loop through players except CM
        players play card
    cardmaster chooses winner
    increase winner points



'''
