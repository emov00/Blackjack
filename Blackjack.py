import random
cards = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

balance = 100
replay = True

def play_again(text=''):
    global replay, balance
    text = str(input('\nWant to play again? y for yes, n for no. '))
    if text == 'y':
        replay = True
    elif text == 'n':
        print(f'\nYou finished with {balance}. Thanks for playing!')
        replay = False
    else:
        print('Not recognized. Try again.')
        text = str(input('Want to play again? y for yes, n for no. '))


def win(text=''):
    global replay, balance
    balance += bet
    print(f'\nYou win! Current balance is {balance}.')
    play_again()


def lose(text=''):
    global replay, balance
    balance -= bet
    if balance == 0:
        replay = False
        print(f"You're balance is {balance}! Looks like you're out of money! Thanks for playing!")
    else:
        print(f'You lose! Current balance is {balance}.')
        play_again()

def tie(text=''):
    global replay, balance
    print(f"It's a tie! Current balance is {balance}.")
    play_again()

def Ace_init(val=''):
    global player_value, player_cards, dealer_cards, dealer_value
    if 'Ace' in player_cards:
        print(f'The dealer has {dealer_cards[0]} and {dealer_cards[1]} for a value of {dealer_value}')
        print(f'Your cards are {player_cards[0]} and {player_cards[1]}.')
        print('\nYou drew an Ace. Do you want it to be 1 or 11? ')
        print(f'If you choose 1 you have {player_value-10}. If you choose 11 you have {player_value}.')
        
        val = int(input('1 or 11? '))
        if val == 1:
            player_value -= 10
        elif val == 11:
            pass
        else:
            print('Not recognized. Try Again.')
            val = int(input('1 or 11? '))

def Ace_player_draw():
    global player_value, player_cards, player_draw
    if player_draw == 'Ace':
        if player_value > 21:
            player_value -= 10
        elif player_value == 21:
            pass
        else:
            pass

def Ace_dealer_draw():
    global dealer_value, dealer_cards, dealer_draw
    if dealer_draw == 'Ace':
        if dealer_value > 21:
            dealer_value -= 10
        elif dealer_value == 21:
            pass
        else:
            pass
            

while replay == True:
    print(f'\nYour balance is {balance}.')
    bet = int(input('\nHow much would you like to bet? '))
    print('')
    if bet > balance:
        print('Insufficeint funds. Try again.')
        bet = int(input('\nHow much would you like to bet? '))
    elif bet <= 0:
        print('Not possible. Try Again.')
        bet = int(input('\nHow much would you like to bet? '))
    else:
        print('')
        pass
    
    player_cards = list(random.choices(list(cards.keys()), k=2))
    player_value = cards[player_cards[0]] + cards[player_cards[1]]
    

    dealer_cards = list(random.choices(list(cards.keys()), k=2))
    dealer_value = cards[dealer_cards[0]] + cards[dealer_cards[1]]
    Ace_init()

    print(f'The dealer has {dealer_cards[0]} and {dealer_cards[1]} for a value of {dealer_value}')
    print('')
    print(f'Your cards are {player_cards[0]} and {player_cards[1]} for a value of {player_value}')

    if player_value == 21 and dealer_value == 21:
        print('You both have 21.')
        ans = False
        tie()
    elif player_value == 21:
        print('You have 21.')
        ans = False
        win()
    elif dealer_value == 21:
        print('The dealer has 21.')
        ans = False
        lose()

    if player_value != 21 and dealer_value !=21:
        ans = str(input('Would you like to hit or stay? '))

    player = True
    while player == True:
        if ans == 'hit':
            player = False
            player_draw = random.choice(list(cards.keys()))
            player_value += cards[player_draw]
            Ace_player_draw()
            print('')
            print(f'You drew a {player_draw}. You now have {player_value}.')

            if player_value < 21: 
                ans = str(input('Would you like to hit or stay? '))
                player = True
            elif player_value == 21:
                print('You have 21.')
                win()
            else:
                print("You're over 21.")
                lose()

        elif ans == 'stay':
            player = False
            print(f'\nYou stayed with {player_value}')
            if dealer_value in range(18,22):
                if player_value > dealer_value:
                    print(f'You have {player_value}, the dealer has {dealer_value}.')
                    win()
                
                elif player_value < dealer_value:
                    print(f'You have {player_value}, the dealer has {dealer_value}.')
                    lose()
                
                else:
                    tie() 

            while dealer_value not in range(18,22):
                dealer_draw = random.choice(list(cards.keys()))
                dealer_value += cards[dealer_draw] 
                Ace_dealer_draw()
                print('')
                print(f'The dealer drew a {dealer_draw}. They now have {dealer_value}.')
                
                if dealer_value > 21:
                    print('The dealer is over 21.')
                    win()
                    break

                elif 0 < dealer_value < 18:
                    continue
                else:
                    if player_value > dealer_value:
                        print(f'You have {player_value}, the dealer has {dealer_value}.')
                        win()
                    elif player_value < dealer_value:
                        print(f'You have {player_value}, the dealer has {dealer_value}.')
                        lose()
                    else:
                        tie()
        
        elif ans == False:
            break
    
        else:
            print('')
            print('Not recognized. Try again.')
            ans = str(input('Do you want to hit or stay? '))