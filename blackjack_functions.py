import os
def take_bet():
    global bet
    while True:
        try:
            bet = int(input("Enter a bet: "))
            if bet > player.total:
                raise ValueError
        except:
            print 'Bad input, try again: '
        else:
            break
def hit(deck,hand):
    hand.add_card(deck.deal())
def hit_or_stand(deck, hand):
    global playing
    while True:
        try:
            ask = raw_input("Hit or Stand? (h/s) ")
            if ask != 'h':
                if ask != 's':
                    raise TypeError
        except:
            print 'Bad input!'
            continue
        else:
            break
    if ask == 'h':
        hit(deck, hand)
        return 'h'
    else:
        return 's'

def show_some(player, dealer):
    print "Player's hand: "
    for card in player.cards:
        print '{} of {}'.format(card[1], card[0])
    print "{} points".format(player.value)
    print "\nDealer's hand: "
    for card in dealer.cards[1:]:
        print '{} of {}'.format(card[1], card[0])

def show_all(player, dealer):
    print "Player's hand: "
    for card in player.cards:
        print '{} of {}'.format(card[1], card[0])
    print "{} points".format(player.value)
    print "\nDealer's hand: "
    for card in dealer.cards:
        print '{} of {}'.format(card[1], card[0])
    print "{} points".format(dealer.value)

def player_busts(balance, bet):
    balance.lose_bet(bet)
    print 'You busted!'

def player_wins(balance, bet):
    balance.win_bet(bet)
    print 'You win!'

def dealer_busts(balance, bet):
    balance.win_bet(bet)
    print 'Dealer busted!'

def dealer_wins(balance, bet):
    balance.lose_bet(bet)
    print 'Dealer wins'

def push():
    print 'TIE'
def clear():
    os.system('clear')
def replay(balance):

    while True:
        try:
            asking = raw_input('Your balance is ${}\nPlay again? y/n: '.format(balance.total))
            if asking != 'y':
                if asking != 'n':
                    raise TypeError
            if asking == 'y':
                return 'y'
            elif asking == 'n':
                return 'n'

        except:
            clear()
            print 'Bad input!'
        else:
            break
def new_game():
    while True:
        try:
            ask = raw_input('You are out of money!\nPlay a new game? y/n ')
            if ask != 'y':
                if ask != 'n':
                    raise TypeError
            if ask == 'y':
                return 'y'
            else:
                return 'n'
        except:
            print 'Bad input!'
            continue
        else:
            break
