import json

class Card:
    def __init__(self, ident, cardType, text, numAnswers, expansion):
        self.ident = ident
        self.cardType = cardType
        self.text = text
        self.numAnswers = numAnswers
        self.expansion = expansion

