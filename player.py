class Player():
    def __init__(self, name):
        self.score = 0
        self.hand = []
        self.name = name
    
    def __len__(self):
        return len(self.hand)
    
    def display_hand(self):
        hand = []
        for idx, card in enumerate(self.hand):
            hand.append((idx, card.text))
        return hand

    def play_card(self, cardidx):
        selected = self.hand.pop(cardidx)
        return selected
    
    def add_card(self, card):
        self.hand.append(card)