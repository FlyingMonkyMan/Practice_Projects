'''
The dice game is played with a single, six-sided die.
Players will take turns throwing the die.
Players throw the die as many times as they like, stopping voluntarily or until a "1" is shown.
Each die thow is added together and added to the player's total score. If a "1" was thrown, then the round is a bust and all points accumulated are lost.
After a player's turn, the die moves to the next player.
First person to reach a total score of "100" wins.
'''

import random

#list of die rolls for given number of throws and associated total
def die_toss(throws):
    die_result = []
    die_total = 0
    for _ in range(throws):
        die_throw = random.randint(1,6)
        die_result.append(die_throw)
        if die_throw == 1:
             print("Bust!")
             die_total = 0
             break
        else:
            die_total += die_throw
    return die_result, die_total

#the main line for each player turn: ask number of throws(?), present outstanding results
# if they decide to end their turn, total score and add to total score
# if a 1 is thrown, end turn and move to next player without totalling score
# return total score for player turn
def player_turn(player):
    yes = ['y','yes']
    no = ['n', 'no']
    
    print(f"\n{player}'s turn!")
    round_total = 0
    
    while True:
        try:
            throws = int(input("How many times would you like to throw the die? "))
        except ValueError:
            print("That is not a number!")
            continue

        die_result, die_total =  die_toss(throws)
        round_total += die_total

        print(f"You're results are: {die_result}. Round total: {die_total}.")

        if 1 in die_result:
            break
        
        while True:
            keep_playing = input("\nWould you like to throw again? (y/n) ").lower()
            if keep_playing in yes:
                continue
            elif keep_playing in no:
                break
            else:
                print("That is not an answer!")
    
    return round_total

#function for the dice game. Allows for new game to be played with clean slate, if new game is desired.    
def dice_game():
    player_scores = {}

    while True:
        try:
            number_players = int(input("How many players will be playing? ")) 
            for i in range (1, number_players+1):
                i = (f'Player {i}')
                player_scores[i] = 0
            break
        except ValueError:
            print("Please enter a number!")
            continue

    while all(score <100 for score in player_scores.values()): 
        for player in player_scores:
            round_total = player_turn(player)
            player_scores[player] += round_total
            print(f'{round_total} points earned this round! Total score: {player_scores[player]}!')
    
            if player_scores[player] >= 100:
                print(f"{player} wins with a score of {player_scores[player]}! Congratulations!")
                print(player_scores)
                break
        else:
            continue
        break

while True:
    dice_game()
    yes = ['y','yes']
    no = ['n', 'no']
    try:
        response = input("Would you like to play again? (y/n)" )
        if response in yes:
            continue
        elif response in no:
            break
    except TypeError:
        print("That is not an answer!")
        continue
    break
    



