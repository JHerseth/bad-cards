import json

class Card:
    def __init__(self, ident, cardType, text, numAnswers, expansion):
        self.ident = ident
        self.cardType = cardType
        self.text = text
        self.numAnswers = numAnswers
        self.expansion = expansion

with open('cards.json') as f:
    cards = json.load(f)

questions = []
answers = []

for card in cards:
    if card['cardType'] == 'Q':
        questions.append(card)
    elif card['cardType'] == 'A':
        answers.append(card)

