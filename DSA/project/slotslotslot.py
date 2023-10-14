import random
import time
from os import system, name


def clear():
    """This function will be used to clear the screen"""
    if name == 'nt':  # Windows
        system('cls')
    else:  # Unix/Linux/macOS
        system('clear')

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0

class Cash:
    def __init__(self, credit=200, bet=2):
        self.credit = credit
        self.bet = bet
        self.bets = [2, 5, 10, 20]
        self.bet_stack = Stack()

    def change_bet(self):
        self.bets.append(self.bets.pop(0))
        self.bet = self.bets[0]
        self.bet_stack.push(self.bet)

    def undo_bet(self):
        last_bet = self.bet_stack.pop()
        if last_bet is not None:
            self.bet = last_bet

    def charge(self):
        if self.bet <= self.credit:
            self.credit -= self.bet
            return False
        else:
            print('\n\t     Not enough credit to place a bet')
            time.sleep(2)
            return True

class SlotMachine:
    def __init__(self, slot_one, slot_two, slot_three):
        self.reels = [slot_one, slot_two, slot_three]

    def spin(self):
        #clear()
        return [random.choices(reel, k=1)[0] for reel in self.reels]

    def play(self, cash):
        result = self.spin()
        print("Result: ", [res[0] for res in result])
        if len(set([res[0] for res in result])) == 1:
            symbol = result[0][0]
            multiplier = result[0][1]
            win_amount = multiplier
            print(f"Congratulations! You won ${win_amount * multiplier}!")
            cash.credit += win_amount * multiplier
        else:
            print("Sorry, you lost. Try again!")
            
# Define the symbols and multipliers
strawberry = ("🍓", 2)
banana = ("🍌", 10)
plum = ("🍑", 3)
raspberry = ("🍇", 5)
orange = ("🍊", 8)
seven = ("💎", 15)

# Define the probabilities for each symbol
probabilities = [0.8, 0.6, 0.5, 0.3, 0.2, 0.1]
symbols = [strawberry, plum, raspberry, orange, banana, seven]
slot_one = random.choices(symbols, weights=probabilities, k=100)

probabilities = [0.8, 0.6, 0.5, 0.3, 0.2, 0.1]
symbols = [strawberry, plum, raspberry, orange, banana, seven]
slot_two = random.choices(symbols, weights=probabilities, k=100)

probabilities = [0.8, 0.6, 0.5, 0.3, 0.2, 0.1]
symbols = [strawberry, plum, raspberry, orange, banana, seven]
slot_three = random.choices(symbols, weights=probabilities, k=100)

# Create a slot machine and cash with these symbols
slot_machine = SlotMachine(slot_one, slot_two, slot_three)
cash = Cash()

def welcome():
    welcome = ['\n\n\t #######    #######    #######',
               '\t########   ########   ########',
               '\t     ##         ##         ##',
               '\t    ##         ##         ##',
               '\t   ##         ##         ##',
               '\t  ##         ##         ##',
               '\t  ##         ##         ##',
               '\n\n'
               '\t##### ##    ####### ###### ',
               '\t##    ##    ##   ##   ##   ',
               '\t##### ##    ##   ##   ##   ',
               '\t   ## ##    ##   ##   ##   ',
               '\t##### ##### #######   ##   ']
    
    for c in welcome:
        print(c)
        time.sleep(0.1)
    time.sleep(1)
    clear()

# Play the game
if __name__ == '__main__':
    clear()
    welcome()
    
    while True:
        print(f"\nCurrent Bet: {cash.bet}, Current Credit: {cash.credit}")
        again = input("\nPress 'q' to quit or 'b' to change bet or any other key to spin: ")
        if again == 'q':
            
            break
        elif again == 'b':
            cash.change_bet()
        else:
            if not cash.charge():
                slot_machine.play(cash)
                
    time.sleep(1)
    clear()
