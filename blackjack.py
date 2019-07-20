import Chip
import Deck
import Hand
import blackjack_functions
import variables
while True:
    balance = Chip.Chip()
    while True:
        blackjack_functions.clear()
        print 'Your balance is {}$'.format(balance.total)
        while True:
            try:
                bet = int(input('The game begins!\nPlease take a bet '))
                if bet > balance.total or bet < 0:
                    raise ValueError
            except:
                print 'Bad betting, try again: '
                continue
            else:
                break

        blackjack_functions.clear()
        player = Hand.Hand()
        dealer = Hand.Hand()
        deck = Deck.Deck()
        deck.shuffle()
        dealer.add_card(deck.deal())
        dealer.add_card(deck.deal())
        player.add_card(deck.deal())
        player.add_card(deck.deal())
        blackjack_functions.show_some(player, dealer)
        while variables.playing:
            print '\n'
            res = blackjack_functions.hit_or_stand(deck,player)
            if res == 'h':
                blackjack_functions.clear()
                blackjack_functions.show_some(player, dealer)
            if player.value > 21:
                print "\n"
                blackjack_functions.player_busts(balance, bet)
                break
            if res == 's':
                while dealer.value < 17:
                    blackjack_functions.hit(deck, dealer)
                blackjack_functions.clear()
                blackjack_functions.show_all(player, dealer)
                print "\n"
                if 21 - player.value < 21 - dealer.value:
                    blackjack_functions.player_wins(balance, bet)
                    break
                elif dealer.value > 21:
                    blackjack_functions.dealer_busts(balance, bet)
                    break
                elif 21 - dealer.value < 21 - player.value:
                    blackjack_functions.dealer_wins(balance, bet)
                    break
                elif dealer.value == player.value:
                    blackjack_functions.push()
                    break
        if balance.total <= 0:
            break
        repl = blackjack_functions.replay(balance)
        if repl == 'y':
            continue
        else:
            break
    print 'You are out of money'
    new = blackjack_functions.new_game()
    if new == 'y':
        continue
    else:
        break