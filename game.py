import deck
import player
import hand

# Less than 17, advise to “Hit”
# Greater than or equal to 17, but less than 21, advise to “Stay”
# Exactly 21, advise “Blackjack!”
# Over 21, advise “Already Busted”


def advice(value):
    if value < 17:
        print('I advise that you "Hit"\n')
    elif 21 > value >= 17:
        print('I advise you to "Stay"\n')
    elif value == 21:
        print('BLACK-JACK!!!\n')
    elif value > 21:
        print('Busted\n')


def winner(player, bet, dealer):
    if player.hand.value() > 21:
        print('You lose')
    elif dealer.hand.value() > 21 and player.hand.value() == 21:
        player.wallet += bet + bet * 3/2
        print('You win ${}'.format(bet + bet * 3/2))
    elif dealer.hand.value() > 21:
        player.wallet += bet * 2
        print('You win ${}'.format(bet * 2))
    elif player.hand.value() == 21 and player.hand.value() != dealer.hand.value():
        player.wallet += bet + bet * 3/2
        print('You win ${}'.format(bet + bet * 3/2))
    elif player.hand.value() > dealer.hand.value():
        player.wallet += bet * 2
        print('You win ${}'.format(bet * 2))
    elif dealer.hand.value() > player.hand.value():
        print('You lose')
    elif player.hand.value() == dealer.hand.value():
        player.wallet += bet
        print('Tie. You receive ${} back'.format(bet))


d = deck.Deck()
nate = player.Player()
dealer = player.Player()
nate.hand = hand.Hand()
dealer.hand = hand.Hand()


while True:
    d.shuffle()
    bet = nate.bet()
    nate.hand.draw(d.hopper, 2)
    dealer.hand.draw(d.hopper, 2)
    while True:
        print('\nplayers hand: {}'.format(nate.hand.value()))
        nate.hand.display()
        advice(nate.hand.value())
        choice = input('HIT or STAY (h/s):')
        if choice != 'h' and choice != 's':
            print('That\'s not a valid response.')
        elif choice == 'h':
            nate.hand.draw(d.hopper, 1)
            if nate.hand.value() > 21:
                print('\nplayers hand: {}'.format(nate.hand.value()))
                nate.hand.display()
                winner(nate, bet, dealer)
                break
        elif choice == 's':
            if dealer.hand.value() < 16:
                while dealer.hand.value() < 16:
                    dealer.hand.draw(d.hopper, 1)
            print('Dealers hand: {}'.format(dealer.hand.value()))
            dealer.hand.display()
            print('\nplayers hand: {}'.format(nate.hand.value()))
            nate.hand.display()
            winner(nate, bet, dealer)
            break
    nate.hand.return_card(d.hopper)
    dealer.hand.return_card(d.hopper)

player.outcome(nate)

