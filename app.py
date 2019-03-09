from cards import questions, answers, Card
from deck import Deck, Player
import json






p1 = Player(deck, size=5)
p2 = Player(deck, size=5)
p3 = Player(deck, size=5)

print(p1.display_hand())
print(p2.display_hand())
print(p3.display_hand())
print()
print(deck.draw_question()['text'])
p1.play_card(1)
print(len(p1))


class Game:
    def __init__(self, numPlayers = 3, handSize = 5, expantions = ['Base']):
        self.deck = Deck(questions, answers)
        self.players = [Player(self.deck, size=handSize) for _ in range(numPlayers)]
    
    def run(self):
        pass


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
