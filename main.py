# Function Name: roll2Dice
# Purpose: Use random numbers to simulate the results of rolling 2 six-sided dice.
# Output the result of the roll by printing the number on each die as well as the sum of the two dice.
#
# eg. Rolling a 5 and a 2 should be outputted as: “5,2 (sum: 7)”
#
# Also return the sum of the two dice.
# Parameters:
# No Parameters
# Return Value:
# The sum of rolling the two dice.#


import random

def main():
    print("DICE ROLL SIMIULATER MENU")
    print("1. Roll Dice Once \n2. Roll Dice 5 times \n3. Roll Dice n times \n4. Roll Dice until snake Eyes \n5. Exit")
    menu_choice = int(input("Select an option(1-5): "))
    if menu_choice == 1:
        roll2Dice()
    if menu_choice == 2:
        for i in range(5):
            roll2Dice()
    if menu_choice == 3:
        n = input("Please input the number of times of dices you want to toss:")
        for i in range(n):
            roll2Dice()
    if menu_choice == 4:
        #Roll Dice until snake Eyes
    else:
        #Exit
def roll2Dice():
    dice_1 = random.randrange(1,6)
    dice_2 = random.randrange(1, 6)
    sum_of_dice = dice_1 + dice_2
    print("Dice 1:" + dice_1 + "\nDice 2:" + dice_2 + "\nSum of Dice:" + sum_of_dice)
