import random
import json
from cards import Card

class Deck():
    """Deck object to hold cards and do deck operations like dealing and shuffling.

    Attributes:
        file (str): path to json file with card data
        type (str): 'Q' or 'A' depending on the type of deck you want to make
        expansions

    """
    def __init__(self, file, type, expansions = ['Base']):
        with open(file) as f:
            cards = json.load(f)

        self.deck = []
        self.spent_pile = []

        for card in cards:
            if card['expansion'] not in expansions:
                continue                
            if card['cardType'] == type:
                self.deck.append(
                    Card(
                        card['id'],
                        card['cardType'],
                        card['text'],
                        card['numAnswers'],
                        card['expansion'],
                        )
                    )
    
    def __str__(self):
        deck = [str(card) for card in self.deck]
        return f"{deck}"
    
    def draw_card(self):
        return self.deck.pop()

    def shuffle_deck(self):
        random.shuffle(self.deck)
    
    def reset_deck(self):
        self.deck += self.spent_pile
        self.shuffle_deck()
    
    def deal(self, players, num_cards=5):
        num_players = len(players)
        for i in range(num_cards*num_players):
            if len(self.deck) <= 0: break      # break if out of cards
            card = self.draw_card()            # take the top card
            player = players[i % num_players]  # whose turn is next?
            player.add_card(card)              # add the card to the hand
    


