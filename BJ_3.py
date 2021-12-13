# Import Section
import Print_Card
from random import choice

# Deck Creation
Deck_Suits = [ '♠', '♦', '♣', '♥']
Deck_Cards_Value = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
Deck_Values = {'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10,}

# Player Class
class player():
    def __init__( self, name, BJB = 0, Condition = 0):
        self.cards = []
        self.name = name
        self.BJB = BJB
        self.money = 0
        self.Condition = Condition
    
    def Hit( self):
        global Deck
        a = choice(Deck)
        (self.cards).append(a)
        Deck.remove(a)
    
    def Show_Cards( self):
        if self.name != 'Dealer':
            try:
                for x in range(13):
                    Print_Card.Card( (self.cards)[x][0], (self.cards)[x][1])
            except:
                pass
        else:
            Print_Card.Face_Down_Card()
            try:
                for x in range( 1, 13):
                    Print_Card.Card( (self.cards)[x][0], (self.cards)[x][1])
            except:
                pass
    
    def Bet_Money( self, bet):
        self.money -= bet
        self.bet = bet
        print(self.name + ' has ' + str(self.money) + '$ left!')
        pass
    
    def Points( self):
        self.points = 0
        for x, y in self.cards:
            for z in Deck_Values.keys():
                if x == z:
                    self.points += Deck_Values[z]
            if x == 'A' and self.points > 21:
                self.points -= 10
    
    def Print_Points( self):
        print( self.points, '\n\n')
    
# Functions
def Show_Cards_And_Points( player_list, name_list):
    print('Here are the Dealer\'s cards: ')
    Dealer.Show_Cards()
    Dealer.Points()
    print('\n\n')
    for i, j in  list(zip( player_list, name_list)):
        print('Here are ' + j + '\'s cards: ')
        i.Show_Cards()
        i.Points()
        i.Print_Points()

def H_or_S( name_list, player_list):
    for m, n in list(zip( name_list, player_list)):
        if n.Condition == 0:
            if n.points > 21:
                print(m + ' has a BUST!')
                n.BJB = 1
                n.Condition = 1
                continue
            elif n.points == 21:
                print(m + ' has a BLACKJACK!')
                n.BJB = 2
                n.Condition = 1
                continue
            while True:
                ans_2 = (input(m + ', do you want to HIT or STAY: ')).upper()
                print('\n\n\n')
                if ans_2 == 'H' or ans_2 ==  'HIT':
                    n.Hit()
                    Show_Cards_And_Points( player_list, name_list)
                    if n.points > 21:
                        print(m + ' has a BUST!')
                        n.BJB = 1
                        n.Condition = 1
                        break
                    elif n.points == 21:
                        print(m + ' has a BLACKJACK!')
                        n.BJB = 2
                        n.Condition = 1
                        break
                elif ans_2 == 'S' or ans_2 ==  'STAY':
                    n.Condition = 1
                    break
                else:
                    print('Please enter a valid answer\n!')
                    continue

#----------------------------------------------------------------------------#
print('Welcome to the BlackJack game!')
name_1 = input('Tell me, what\'s your name, PLAYER 1: ')
name_2 = input('And what\'s your name, PLAYER 2: ')
name_3 = input('And what\'s your name, PLAYER 3: ')
print('\n\n')

money_1 = money_2 = money_3 = 1000



while True:
    # Place Holder
    Deck = []

    # Create Deck
    for b in Deck_Suits:
        for a in Deck_Cards_Value:
            Deck += [( a, b)]
    
    # Create Players and Dealer
    Player_1 = player(name_1)
    Player_2 = player(name_2)
    Player_3 = player(name_3)
    Dealer = player('Dealer')
    
    # Initialize Money
    Player_1.money = money_1
    Player_2.money = money_2
    Player_3.money = money_3

    money_list = [ Player_1.money, Player_2.money, Player_3.money]
    name_list = [ name_1, name_2, name_3]
    player_list = [ Player_1, Player_2, Player_3]
    condition_list = [ Player_1.Condition, Player_2.Condition, Player_3.Condition]
    try:
        x = 0
        for i in [ money_1, money_2, money_3]:
            x += 1
            if i <= 0:
                if x == 1:
                    money_list.remove(Player_1.money)
                    name_list.remove(name_1)
                    player_list.remove(Player_1)
                    condition_list.remove(Player_1.Condition)
                elif x == 2:
                    money_list.remove(Player_2.money)
                    name_list.remove(name_2)
                    player_list.remove(Player_2)
                    condition_list.remove(Player_2.Condition)
                elif x == 3:
                    money_list.remove(Player_3.money)
                    name_list.remove(name_3)
                    player_list.remove(Player_3)
                    condition_list.remove(Player_3.Condition)
    except:
        pass
    
    
    for i, j in list(zip( name_list, money_list)):
        print(i + ', you have ' + str(j) + '$ in your hand at the beginning of the game!\n')

    for i in name_list:
        while True:
            bet = input('How much money do you want to bet, ' + i + ': ')
            if bet.isdigit():
                print(i + ' bet ' + bet + '$!')
                if i == name_1:
                    Player_1.Bet_Money(int(bet))
                    break
                elif i == name_2:
                    Player_2.Bet_Money(int(bet))
                    break
                elif i == name_3:
                    Player_3.Bet_Money(int(bet))
                    break
            else:
                print('Please enter a valid answer\n!')
                continue
    
    # First Cards of Dealer and Player
    for x in range(2):
        Player_1.Hit()
        Player_2.Hit()
        Player_3.Hit()
        Dealer.Hit()
    
    # Show Cards
    Show_Cards_And_Points( player_list, name_list)
    
    # Ask for Hit or Stay
    if len(condition_list) == 3:
        while not Player_1.Condition == Player_2.Condition == Player_3.Condition == 1:
            H_or_S( name_list, player_list)
    elif len(condition_list) == 2:
        while not condition_list[0] == condition_list[1] == 1:
            H_or_S( name_list, player_list)
    elif len(condition_list) == 1:
        while not condition_list[0] == 1:
            H_or_S( name_list, player_list)
        
    while Dealer.points < 17:
        Dealer.Hit()
        Dealer.Points()

    print('Here are the Dealer\'s cards: ')
    try:
        for x in range(13):
            Print_Card.Card( (Dealer.cards)[x][0], (Dealer.cards)[x][1])
    except:
        pass
    Dealer.Print_Points()
    
    if Dealer.points > 21:
        print('Dealer has a BUST!')
        Dealer.BJB = 1
    elif Dealer.points == 21:
        print('Dealer has a BLACKJACK!')
        Dealer.BJB = 2
    
    # Check Result
    for m, n in list(zip( name_list, player_list)):
        if (n.BJB == Dealer.BJB == 1) or (n.BJB == 0 and Dealer.BJB == 2) or (n.BJB == 1 and Dealer.BJB == 2) or (n.BJB == 1 and Dealer.BJB == 0):
            print(m + ' lose and lost money!\n')
            if m == name_1:
                money_1 = n.money
            elif m == name_2:
                money_2 = n.money
            elif m == name_3:
                money_3 = n.money
        elif (n.BJB == Dealer.BJB == 2):
            print('The result is draw, ' + m + ' keep his money!\n')
        elif (n.BJB == 0 and Dealer.BJB == 1) or (n.BJB == 2 and Dealer.BJB == 0) or (n.BJB == 2 and Dealer.BJB == 1):
            print(m + ' win and earn 1.5 of the bet!\n')
            if m == name_1:
                money_1 = n.money +  (int(n.bet) * 2.5)
            elif m == name_2:
                money_2 = n.money +  (int(n.bet) * 2.5)
            elif m == name_3:
                money_3 = n.money +  (int(n.bet) * 2.5)
        elif (n.BJB == Dealer.BJB == 0):
            if n.points > Dealer.points:
                print(m + ' win and earn 1.5 of the bet!\n')
                if m == name_1:
                    money_1 = n.money +  (int(n.bet) * 2.5)
                elif m == name_2:
                    money_2 = n.money +  (int(n.bet) * 2.5)
                elif m == name_3:
                    money_3 = n.money +  (int(n.bet) * 2.5)
            elif n.points < Dealer.points:
                print(m + ' lose and lost money!\n')
                if m == name_1:
                    money_1 = n.money
                elif m == name_2:
                    money_2 = n.money
                elif m == name_3:
                    money_3 = n.money
            elif n.points == Dealer.points:
                print('The result is draw, ' + m + ' keep his money!\n')
                if m == name_1:
                    money_1 = n.money + int(n.bet)
                elif m == name_2:
                    money_2 = n.money + int(n.bet)
                elif m == name_3:
                    money_3 = n.money + int(n.bet)
    
    if money_1 == money_2 == money_3 == 0:
        print('You all lose!')
        break

    # Ask if player want to play again?
    while True:
        ans_3 = (input('Do you want to play again: ')).upper()
        if ans_3 == 'Y' or ans_3 == 'YES':
            print('\n\n\n\n\n\n\n\n')
            break
        elif ans_3 == 'N' or ans_3 == 'NO':
            break
        else:
            print('Please enter a valid answer!\n')
            continue
    if ans_3 == 'Y' or ans_3 == 'YES':
        continue
    else:
        break