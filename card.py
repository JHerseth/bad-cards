class Card:
    """Card object to hold induvidual cards.

    Attributes:
        ident (int): unique ID (probably not needed)
        cardType (str): Q for question cards, A for answer cards
        text (str): Card main text
        numAnswers (int): Number of answers needed for question card
        expansion (str): Expansion set the card is found in

    """
    def __init__(self, ident, cardType, text, numAnswers, expansion):
        self.ident = ident
        self.cardType = cardType
        self.text = text
        self.numAnswers = numAnswers
        self.expansion = expansion
    
    def __str__(self):
        return f"{self.cardType}: {self.text}"

    def __repl__(self):
        return f"{self.cardType}: {self.text}"

