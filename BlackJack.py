'''     Card1 = "------\n|%n    |\n| %s |\n|    %n|\n------"
        Card2 = "------  ------\n|    |  |    |\n| %s |  | %s |\n|    |  |    |\n------  ------"
        Card3 = "------  ------  ------\n|    |  |    |  |    |\n| %s |  | %s |  | %s |\n|    |  |    |  |    |\n------  ------  ------"
        Card4 = "------  ------  ------  ------\n|    |  |    |  |    |  |    |\n| %s |  | %s |  | %s |  | %s |\n|    |  |    |  |    |  |    |\n------  ------  ------  ------"   '''


from random import shuffle


class Hand:
    def __init__(self, name):
        self.name = name
        self.cards = []    # пустая рука

    def add_card(self, card):
        self.cards.append(card)    # добавить карту в руку

    def get_value(self):   # начисление очков
        result = 0
        aces = 0   # количество тузов на руке
        for card in self.cards:
            result += card.card_value()
            if card.get_rank() == "A":   # если на руке есть туз - увеличиваем количество тузов
                aces += 1
        if result + aces * 10 <= 21:   # решаем считать тузы за 1 очко или за 11
            result += aces * 10
        return result

    def __str__(self):
        text = "Рука %sа:\n" % self.name
        for card in self.cards:
            text += str(card) + " "
        text += "\nКоличество очков: " + str(self.get_value())
        return text


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