class Card:
    def __init__(self, rank, suit, value=0):
        self.rank = rank
        self.suit = suit
        self.value = value

    @property
    def __str__(self):
        card = ('┌─────────┐\n'
                '│{}       │\n'
                '│         │\n'
                '│         │\n'
                '│    {}   │\n'
                '│         │\n'
                '│         │\n'
                '│       {}│\n'
                '└─────────┘ \n'
                ).format(
                    format(self.rank[:1], ' <2'),
                    format(self.suit, ' <2'),
                    format(self.rank[:1], ' >2')
        )
        return card
        # return '{} of {}'.format(self.rank, self.suit)

    def __repr__(self):
        return '{}-{}'.format(self.rank[:1], self.suit[:1])


if __name__ == '__main__':
    c1 = Card('Ace', 'Clubs', 1)
    c2 = Card('Two', 'Spades', 2)
    print(c1)
    print(c2)
