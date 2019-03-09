# from cards import Card
import random
from deck import Deck
from player import Player
import json

names = ["Jack", "Joe", "Frederich", "Marcus"]

class Game:
    def __init__(self, cardfile, handSize = 5, expansions = ['Base']):
        self.questions  = Deck(cardfile, 'Q', expansions)
        self.answers    = Deck(cardfile, 'A', expansions)
        self.players    = []
        self.questions.shuffle_deck()
        self.answers.shuffle_deck()
    
    def addPlayer(self, name):
        self.players.append(Player(name))
    
    def run(self):
        self.answers.deal(self.players, num_cards=5)

        # playedCard = self.questions.draw_card()
        # print(f"{playedCard}")
        # print(f"Chose {playedCard.numAnswers} card{'s' if playedCard.numAnswers > 1 else ''}.")
        # for _ in range(playedCard.numAnswers):
        #     pass
        for player in self.players:
            print(player.display_hand())

            
    

            

game = Game("cards.json")
for name in names:
    game.addPlayer(name)
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
