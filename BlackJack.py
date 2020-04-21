class Hand:
    def __init__(self, name):
        self.name = name
        self.cards = []    # пустая рука

    def add_card(self, card):
        self.cards.append(card)    # добавить карту в руку