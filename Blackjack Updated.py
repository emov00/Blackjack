import random

class Blackjack():
    def __init__(self):
        self.cards = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
        self.balance = 100
        self.replay = True

    def initial_draw(self):
        self.player_cards = list(random.choices(list(self.cards.keys()), k=2))
        self.player_value = self.cards[self.player_cards[0]] + self.cards[self.player_cards[1]]
    
        self.dealer_cards = list(random.choices(list(self.cards.keys()), k=2))
        self.dealer_value = self.cards[self.dealer_cards[0]] + self.cards[self.dealer_cards[1]]
    
    def player_draw(self):
        self.player_draw_cards = random.choice(list(self.cards.keys()))
    
    def dealer_draw(self):
        self.dealer_draw_cards = random.choice(list(self.cards.keys()))

    def play_again(self, text=''):
        text = str(input('\nWant to play again? y for yes, n for no. '))
        while True:
            if text == 'y':
                self.replay = True
                break
            elif text == 'n':
                self.replay = False
                print(f'Your final balance is {self.balance}. Thanks for playing!')
                break
            else:
                print('Not recognized. Try again.')
                text = str(input('Want to play again? y for yes, n for no. '))


    def win(self,text=''):
        self.balance += self.bet
        print(f'\nYou win! Current balance is {self.balance}.')
        game.play_again()

    def lose(self, text=''):
        self.balance -= self.bet
        if self.balance == 0:
            print(f"You're balance is {self.balance}! Looks like you're out of money! Thanks for playing!")
            self.replay = False
        else:
            print(f'You lose! Current balance is {self.balance}.')
            return game.play_again()

    def tie(self, text=''):
        print(f"It's a tie! Current balance is {self.balance}.")
        return game.play_again()

    def Ace_init(self, val=''):
        if 'Ace' in self.player_cards:
            print(f'The dealer has {self.dealer_cards[0]} and {self.dealer_cards[1]} for a value of {self.dealer_value}')
            print(f'Your cards are {self.player_cards[0]} and {self.player_cards[1]}.')
            print('\nYou drew an Ace. Do you want it to be 1 or 11? ')
            print(f'If you choose 1 you have {self.player_value-10}. If you choose 11 you have {self.player_value}.')
            
            val = int(input('1 or 11? '))
            if val == 1:
                self.player_value -= 10
            elif val == 11:
                pass
            else:
                print('Not recognized. Try Again.')
                val = int(input('1 or 11? '))

    def Ace_player_draw(self):
        if self.player_draw_cards == 'Ace':
            if self.player_value > 21:
                self.player_value -= 10
            elif self.player_value == 21:
                pass
            else:
                pass

    def Ace_dealer_draw(self):
        if self.dealer_draw_cards == 'Ace':
            if self.dealer_value > 21:
                self.dealer_value -= 10
            elif self.dealer_value == 21:
                pass
            else:
                pass

    def player_bet(self):
        print(f'\nYour balance is {self.balance}.')
        self.bet = input('\nHow much would you like to bet? ')
        while True:
            try:
                self.bet = int(self.bet)
                if self.bet > self.balance:
                    print('Insufficeint funds. Try again.')
                    self.bet = input('\nHow much would you like to bet? ')
                elif self.bet <= 0:
                    print('Not possible. Try Again.')
                    self.bet = input('\nHow much would you like to bet? ')
                else:
                    print('')
                    break
            except:
                print('Please enter a number!')
                self.bet = input('\nHow much would you like to bet? ')
        
            
game = Blackjack()

while game.replay == True:
    
    game.player_bet()
    game.initial_draw()
    game.Ace_init()

    print(f'The dealer has {game.dealer_cards[0]} and {game.dealer_cards[1]} for a value of {game.dealer_value}')
    print('')
    print(f'Your cards are {game.player_cards[0]} and {game.player_cards[1]} for a value of {game.player_value}')

    if game.player_value == 21 and game.dealer_value == 21:
        print('You both have 21.')
        game.tie()
    elif game.player_value == 21:
        print('You have 21.')
        game.win()
    elif game.dealer_value == 21:
        print('The dealer has 21.')
        game.lose()

    if game.player_value != 21 and game.dealer_value !=21:
        ans = str(input('Would you like to hit or stay? ')).strip().lower()

    player = True
    while player == True:
        if ans == 'hit':
            player = False
            game.player_draw()
            game.player_value += game.cards[game.player_draw_cards]
            game.Ace_player_draw()
            print('')
            print(f'You drew a {game.player_draw_cards}. You now have {game.player_value}.')

            if game.player_value < 21: 
                ans = str(input('Would you like to hit or stay? '))
                player = True
            elif game.player_value == 21:
                print('You have 21.')
                game.win()
            else:
                print("You're over 21.")
                game.lose()

        elif ans == 'stay':
            player = False
            print(f'\nYou stayed with {game.player_value}')
            if game.dealer_value in range(18,22):
                if game.player_value > game.dealer_value:
                    print(f'You have {game.player_value}, the dealer has {game.dealer_value}.')
                    game.win()
                
                elif game.player_value < game.dealer_value:
                    print(f'You have {game.player_value}, the dealer has {game.dealer_value}.')
                    game.lose()
                
                else:
                    game.tie() 

            while game.dealer_value not in range(18,22):
                game.dealer_draw()
                game.dealer_value += game.cards[game.dealer_draw_cards] 
                game.Ace_dealer_draw()
                print('')
                print(f'The dealer drew a {game.dealer_draw_cards}. They now have {game.dealer_value}.')
                
                if game.dealer_value > 21:
                    print('The dealer is over 21.')
                    game.win()
                    break

                elif 0 < game.dealer_value < 18:
                    continue
                else:
                    if game.player_value > game.dealer_value:
                        print(f'You have {game.player_value}, the dealer has {game.dealer_value}.')
                        game.win()
                    elif game.player_value < game.dealer_value:
                        print(f'You have {game.player_value}, the dealer has {game.dealer_value}.')
                        game.lose()
                    else:
                        game.tie()
        
        elif ans == False:
            break
    
        else:
            print('')
            print('Not recognized. Try again.')
            ans = str(input('Do you want to hit or stay? '))