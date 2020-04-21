class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def card_value(self):
        if self.rank in "TJQK":    # ценность карты
            return 10
        else:
            return " A23456789".index(self.rank)