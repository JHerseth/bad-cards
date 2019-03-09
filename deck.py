import random
import json
from cards import Card

class Deck():
    def __init__(self, file, expantions):
        with open(file) as f:
            cards = json.load(f)

        self.questions = []
        self.answers = []

        for card in cards:
            if card['expansion'] not in expantions:
                continue                
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
    
    def __str__(self):
        q = [card.text for card in self.questions]
        a = [card.text for card in self.questions]
        deck = q + a
        return str(deck)
    
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


