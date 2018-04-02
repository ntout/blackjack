import card
import random


class Deck:
    RANK_VALUE = {
        'Ace':1, '2':2, '3':3, '4':4, '5':5, '6':6,
        '7':7, '8':8, '9':9, '10':10, 'Jack':10, 'Queen':10, 'King':10
        }
    SUIT = ['♥', '♠', '♣', '♦']
    # SUIT = ['Hearts','Spades','Clubs','Diamonds']

    def __init__(self, number=1):
        self.hopper = self.create_cards(number)

    def create_cards(self, number=1):
        deck = []
        for i in range(number):
            for s in self.SUIT:
                for r, v in self.RANK_VALUE.items():  # [('Ace',1),('2',2)...]
                    deck.append(card.Card(r, s, v))
        return deck

    def shuffle(self):
        random.shuffle(self.hopper)

    def deal_card(self, number=1):
        hand = []
        for i in range(number):
            hand.append(self.hopper.pop())
        return hand


if __name__ == '__main__':
    deck = Deck()
    # print(deck.hopper)
    deck.shuffle()
    # print(deck.hopper)
    player = deck.deal_card()

    print(player)
