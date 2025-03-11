import random
import math

def Number_Guessing_Game(Lower_Bound, Upper_Bound):
    random_number = random.randint(Lower_Bound,Upper_Bound)
    number_guesses = math.ceil(math.log2(Upper_Bound - Lower_Bound +1))
    guess_count = 0

    print(f"\nYou will have {number_guesses} guesses to try and guess the correct number. Good luck! \n")

    while guess_count < number_guesses:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a number!\n")
            continue

        if guess < Lower_Bound or guess > Upper_Bound:
            print("Your guess is out of set bounds! Please try again.\n")
                                  
        elif guess < random_number:
            print("Your guess is too low!\n")
            guess_count += 1
        elif guess > random_number:
            print("Your guess is too high!\n")
            guess_count += 1
        elif guess == random_number:
            print("Congratulations! You guess the number!")
            break   

        if guess_count >= number_guesses: # need to solve too many counts
            print(f"You tried too many times! The number was {random_number}. Better luck next time.")
            break 


print("Welcome to the Number Guessing Game!\n")

while True:
    try:
        Lower_Bound = int(input("Please enter the lower bound: "))
        Upper_Bound = int(input("Please enter the upper bound: "))
        if Lower_Bound >= Upper_Bound:
            raise ValueError("Lower bound must be less than the upper bound!\n")
        break
    except ValueError as e:
        if "invalid literal for int()" in str(e):
            print("Please enter a number!")
        else:
            print(e)
    
Number_Guessing_Game(Lower_Bound,Upper_Bound)


