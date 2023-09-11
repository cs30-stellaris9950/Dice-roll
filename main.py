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

    loop = True
    while loop:
        print("DICE ROLL SIMIULATER MENU")
        print(
            "1. Roll Dice Once \n2. Roll Dice 5 times \n3. Roll Dice n times \n4. Roll Dice until snake Eyes \n5. Exit")
        menu_choice = int(input("Select an option(1-5): "))

        # roll dice once
        if menu_choice == 1:
            roll2Dice()
        # roll dice 5 times
        elif menu_choice == 2:
            for i in range(5):
                print(f"Roll {i+1}")
                roll2Dice()
        # roll dice for n times
        elif menu_choice == 3:
            n_times = int(input("Please input the number of times of dices you want to toss:"))
            for i in range(n_times):
                print(f"Roll {i + 1}")
                roll2Dice()
        # roll dice until snake eye
        elif menu_choice == 4:
            # snake_eye = 2
            result = 0
            rolls = 0
            while not result == 2:
                rolls += 1
                print(f"Roll {rolls}")
                result = roll2Dice()
            print(f"Looks like it took {rolls} rolls to get to snake eye")
        # Exit
        elif menu_choice == 5:
            loop = False



def roll2Dice():
    dice_1 = random.randrange(1,6)
    dice_2 = random.randrange(1, 6)
    sum_of_dice = dice_1 + dice_2
    print(f"Dice one:{dice_1} \nDice two:{dice_2} \nSum of Dice:{sum_of_dice}")
    return sum_of_dice


def exit():
    exit = int(input("Press 1 to return to menu, Press 2 to quit simiulator:"))
    if exit == 1:
        main()
    elif exit == 2:
        quit()

# run the code
main()