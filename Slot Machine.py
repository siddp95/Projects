#!/usr/bin/env python
# coding: utf-8

# # Slot Machine


import random


#Constants
MAX_LINES = 3
MAX_BET = 1000
MIN_BET = 1

ROWS = 3
COLS = 3

#Number of each symbol
symbol_count = {
    "A": 5,
    "B": 10,
    "C": 20,
    "D": 30
}

#Value of each symbol
symbol_value = {
    "A": 30,
    "B": 20,
    "C": 10,
    "D": 5
}


#Input function to accept deposit amount
def deposit():
    while True:
        amount = input("How much do you want to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Must be more than 0.")
        else:
            print("Please enter a number.")
    return amount


#Number of lines player wants to play
def get_number_of_lines():
    while True:
        lines = input("Enter number of lines to bet on (1-" + str(MAX_LINES) + "): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Must be between 1-" + str(MAX_LINES))
        else:
            print("Please enter a number.")
    return lines


#Amount to bet per line
def get_bet():
    while True:
        amount = input("How much do you want to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Must be between ${MIN_BET}-${MAX_BET}.")
        else:
            print("Please enter a number.")
    return amount


#Generate column reel of slot machine spin
def get_slot_machine_spin(rows, cols, symbols):
    #List out all symbols
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
            
    #Generate random columns with given symbols
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns


#Transpose the rows
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end = "|")
            else:
                print(column[row], end = "")
        print() #Go next line


#Function to calculate winnings based on number of lines bet on
def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines): 
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check: #When user loses bet
                break
        else: #When user wins bet
            winnings += values[symbol] * bet #Amount won
            winning_lines.append(line + 1) #Lines that were won
    return winnings, winning_lines


def spin(balance):
    lines = get_number_of_lines()
    #Run while bet amount is less than balance
    while True:
        bet = get_bet()
        total_bet = bet * lines
        
        if total_bet > balance:
            print(f"You don't have enough money for that bet! Current balance ${balance}")
        else:
            break
    
    print(f"You are betting ${bet} on {lines}. Total bet equals {total_bet}")
    
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You win on lines: ", *winning_lines)
    return winnings - total_bet


#Main function
def main():
    balance = deposit() #Starting balance/initial deposit
    while True:
        print(f"Current balance is: ${balance}")
        answer = input("Press enter to spin (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)
    print(f"You left with ${balance}")


#Run game!
main()

