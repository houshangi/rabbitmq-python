import json


class Payment:
    def __init__(self, amount, card_number, name):
        self.amount = amount
        self.card_number = card_number
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        self._amount = amount

    @property
    def card_number(self):
        return self._card_number

    @card_number.setter
    def card_number(self, card_number):
        self._card_number = card_number

    def __hash__(self):
        return hash((self.card_number, self.amount, self.name))

