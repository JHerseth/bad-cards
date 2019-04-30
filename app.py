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
        self.answers.deal(self.players, num_cards=8)
        question = self.questions.draw_card()
        print(question)
        print("------------")
        # playedCard = self.questions.draw_card()
        # print(f"{playedCard}")
        # print(f"Chose {playedCard.numAnswers} card{'s' if playedCard.numAnswers > 1 else ''}.")
        # for _ in range(playedCard.numAnswers):
        #     pass
        for player in self.players:
            self.turn(player, question)


    def turn(self, player, question):
        print(f"{player.name}'s turn")
        print("Your hand:")
        print(player.display_hand())

        if question.numAnswers > 1:
            print(f"Select {question.numAnswers} cards")
        else:
            print(f"Select card")

        i = 0
        while i < question.numAnswers:
            chosencard = input("Card no: ")
            i += 1
        print("")



game = Game("cards.json")
for name in names:
    game.addPlayer(name)
game.run()

p1 = Player("Mika")
p1.score = 2
p2 = Player("Jonas")
p2.score = 1
print(p1 > p2)
print(p1 == p2)
print(p1 < p2)
print(max(p1,p2).name)
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
