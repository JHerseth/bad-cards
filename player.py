class Player():
    def __init__(self, deck, size = 5, cardmaster = False):
        self.score = 0
        self.deck = deck
        self.hand = []
        self.cardmaster = cardmaster
        for _ in range(size):
            self.hand.append(deck.draw_answer())
    
    def __len__(self):
        return len(self.hand)
    
    def display_hand(self):
        hand = []
        for idx, card in enumerate(self.hand):
            hand.append((idx, card.text))
        return hand

    def play_card(self, card):
        selected = self.hand.pop(card)
        self.deck.answers_pile.append(selected)
        return selected
    
    def draw_card(self):
        self.hand.append(self.deck.draw_answer())