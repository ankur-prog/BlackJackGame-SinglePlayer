import deck
import chips
import hand


# method to take amount from player

def amount_to_chips():
    try:
        amount = int(input("Please enter amount you want to play "))
    except TypeError:
        print("Please enter number ")
    finally:
        print("Integer amount should be entered .")

    chips1 = chips.Chips(amount)
    return chips1


# method to take bet from player
def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("Please enter your bet:  "))
        except ValueError:
            print("Please Enter an Integer value.")
        else:
            if chips.bet > chips.total or chips.bet <= 0:
                print(
                    f"Sorry . Your bet amount is either less then zero  or more than your available balance . Available Balance :{chips.total}")
            else:
                break


# method if player chooses extra cards
def hit(deck, hand):
    next_card = deck.deal()
    hand.add_card(next_card)
    hand.adjust_for_ace()
    print(f"card after hit : {next_card}")


# method if player wants to hit a new card or want to stand and pass the dealer to continue
def hit_or_stand(deck, hand):
    global playing
    while True:
        x = input("Would you like to Hit or Stand? Enter 'h' or 's' ")
        if x[0].lower() == 'h':
            hit(deck, hand)
        elif x[0].lower() == 's':
            print("Player Stands . Dealer is playing")
            playing = False
        else:
            print("Sorry Please try again . ")
            continue
        break


# function to display the card with dealer's one hidden card
def display_some_cards(dealer, player):
    print("\n Dealer hand : ")
    print(dealer.cards[0])
    print("<card hidden>")
    print("\n Player hand : ")
    print(*player.cards, sep='\n')
    print(f"Player value : {player.values}")


# function to display all cards including dealer's card
def display_all_cards(dealer, player):
    print("\n Dealer hand : ")
    print(*dealer.cards, sep='\n')
    print(f"\n Dealer value {dealer.values}")
    print("\n Player hand : ")
    print(*player.cards, sep='\n')
    print(f"\n Player value {player.values}")


# function if player bust
def player_bust(dealer, player, chips):
    print("Player bust . Dealer wins ")
    chips.lose_bet()


# function if player wins
def player_win(dealer, player, chips):
    print("Player wins")
    chips.win_bet()


# function if dealer bust
def dealer_bust(dealer, player, chips):
    print("Dealer burst , Player wins. ")
    chips.win_bet()


# function if dealer win
def dealer_win(dealer, player, chips):
    chips.lose_bet()
    print("Dealers win")


# function if its a tie (Push)
def push(dealer, player):
    print("Its tie . ")


# now its time to  play the black jack game :)
if __name__ == '__main__':

    chips = amount_to_chips()
    while True:
        # Print an opening statement
        print('Welcome to BlackJack! Get as close to 21 as you can without going over!\n\
            Dealer hits until she reaches 17. Aces count as 1 or 11.')
        deck1 = deck.Deck()
        deck1.card_shuffle()
        # create player hand object
        player = hand.Hand()
        # create dealer hand object
        dealer = hand.Hand()
        # take bet from player
        take_bet(chips)
        # distribute equal cards and hide the dealer's second card
        for x in range(2):
            player.add_card(deck1.deal())
            player.adjust_for_ace()
            dealer.add_card(deck1.deal())
            dealer.adjust_for_ace()
        # display cards excluding dealer card
        display_some_cards(dealer, player)
        # ask for hit or stay
        playing = True
        while playing:
            hit_or_stand(deck1, player)
            print(f'player value after hit or stand : {player.values}')
            if player.values == 21:
                break
            if player.values > 21:
                player_bust(dealer, player, chips)
                break

        if player.values <= 21:
            while dealer.values < 17:
                hit(deck1, dealer)

            # show all cards now
            display_all_cards(dealer, player)
            # run different winning scenarios
            if dealer.values > 21:
                dealer_bust(dealer, player, chips)

            elif dealer.values < player.values <= 21:
                player_win(dealer, player, chips)

            elif dealer.values > player.values:
                dealer_win(dealer, player, chips)

            else:
                push(dealer, player)

        # inform player about  total chips
        print(f"Total chips available : {chips.total}")

        # ask to play again
        new_game = input("Would you like to play another hand ? Enter 'y' or 'n'")
        if new_game[0].lower() == 'y':
            playing = True
            continue

        else:
            print(" Thanks for playing")
            break
