import random
import json
from cards import Card

class Deck():
    def __init__(self, file):
        with open(file) as f:
            cards = json.load(f)

        self.questions = []
        self.answers = []

        for card in cards:
            if card['cardType'] == 'Q':
                self.questions.append(
                    Card(
                        card['id'],
                        card['cardType'],
                        card['text'],
                        card['numAnswers'],
                        card['expansion'],
                        )
                    )
            elif card['cardType'] == 'A':
                self.answers.append(
                    Card(
                        card['id'],
                        card['cardType'],
                        card['text'],
                        card['numAnswers'],
                        card['expansion'],
                        )
                    )


        random.shuffle(self.questions)
        random.shuffle(self.answers)
        
        self.questions_pile = []
        self.answers_pile = []
    
    def draw_question(self):
        return self.questions.pop()

    def draw_answer(self):
        return self.answers.pop()

    def shuffle_questions(self):
        self.questions += self.questions_pile
        random.shuffle(self.questions)
    
    def shuffle_answers(self):
        self.answers += self.answers_pile
        random.shuffle(self.answers)

class Player():
    def __init__(self, deck, size = 5, cardmaster = False):
        self.score = 0
        self.deck = deck
        self.hand = []
        for _ in range(size):
            self.hand.append(deck.draw_answer())
    
    def __len__(self):
        return len(self.hand)
    
    def display_hand(self):
        hand = []
        for idx, card in enumerate(self.hand):
            hand.append((idx, card['text']))
        return hand

    def play_card(self, card):
        selected = self.hand.pop(card)
        self.deck.answers_pile.append(selected)
        return selected
    
    def draw_card(self):
        self.hand.append(self.deck.draw_answer())
