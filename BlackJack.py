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