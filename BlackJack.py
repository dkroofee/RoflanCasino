class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def card_value(self):
        if self.rank in "TJQK":    # ценность карты
            return 10
        else:
            return " A23456789".index(self.rank)

    def get_rank(self):
        return self.rank

    def __str__(self):
        return "%s%s" % (self.rank, self.suit)


class Deck:
    def __init__(self):
        ranks = "23456789TJQKA"   # ранги
        suits = "♥♦♣♠"   # масти
        self.cards = [Card(r, s) for r in ranks for s in suits] * 4   # создает 4 колоды из 52 карт
        shuffle(self.cards)   # перетасовываем колоды

    def deal_card(self):   # выдать карту
        return self.cards.pop()