import deck
import hand


class Player:
    def __init__(self, money=100):
        self.hand = hand.Hand()
        self.split = hand.Hand()
        self.wallet = money

    def bet(self):
        print('Current Balance: ${}'.format(self.wallet))
        while True:
            amt = input('Place your bet or walk(w): ')
            if amt == 'w':
                self.outcome()
                # if self.wallet > 100:
                #     print('Net winnings: ${}'.format(self.wallet - 100))
                # elif self.wallet < 100:
                #     print('You lost ${}.\nMaybe Blackjack isn\'t your game.'.format(100 - self.wallet))
                # else:
                #     print('You broke even.')
                quit()
            if int(amt) > self.wallet:
                print('You do not have enough to place that bet.')
            else:
                self.wallet -= int(amt)
                break
        return int(amt)

    def split_hand(self):
        self.split.hand.append(self.hand.hand.pop())

    def outcome(self):
        if self.wallet > 100:
            win = self.wallet - 100
            if win < 50:
                print( '\nWalking so soon? You only won ${}'.format(win))
            elif win > 100:
                print('\nYou made ${}. That\'s more than you came in with'.format(win))
            else:
                print('You gained ${} over-all'.format(win))
        elif self.wallet < 100:
            print('\nYou lost ${}.\nMaybe Blackjack isn\'t your game.'.format(100 - self.wallet))
        else:
            print('\nYou broke even. Lucky you')



if __name__ == '__main__':
    user = Player()
    d = deck.Deck()
    user.hand.draw(d.hopper, 2)
    user.hand.display()
    user.split_hand()
    # user.hand.display()
    user.split.display()