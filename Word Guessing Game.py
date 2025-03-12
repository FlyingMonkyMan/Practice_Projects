import random
import urllib.request

def get_random_word():
    url = "https://www.mit.edu/~ecprice/wordlist.10000"
    with urllib.request.urlopen(url) as r:
        word_list = r.read().decode('utf=8')
        word_list = word_list.replace('\n', ' ')
        word_list = word_list.split()
        
    random_word = random.randint(1,len(word_list))
    return word_list[random_word]
    
def guessing_game():
    word = get_random_word()  #add if loop for minimum word length or change turn length depending on word length?
    word_print = ['_' for _ in word] 
    
    turns = 12
    guesses = []
    while turns > 0:
        print(' '.join(word_print)) 
        try:
            guess = input("Please enter a letter: ").lower()
            if len(guess) != 1:
                print("Please enter a single letter!")
                continue
            elif guess.isdigit():
                raise TypeError("Please enter a letter!")
        except Exception as e:
            print(e)
            continue
        
        if guess in guesses:
            print("You have already guessed that letter! Try again.")
            continue

        guesses.append(guess)

        if guess in word:
            for index,letter in enumerate(word):
                if guess == letter:
                    word_print[index] = guess                
                    turns -= 1
        else:
            print(f'"{guess}" is not in the word!')
            turns -= 1
        
        if turns >0 and ''.join(word_print) != word:
            print(f"{turns} turns left.")
            print(f"You have guessed: {guesses}")
        elif ''.join(word_print) == word:
            print(''.join(word_print))
            print('Congratulations! You guessed the word!')
            break
        else:
            print(f'The word to guess was "{word}". Better luck next time!')    


name = input("What is your name? ")
print(f'You will have 12 tries to guess the word using individual letters. Good luck, {name}!')
guessing_game()
while True:
    yes = ['y', 'yes']
    no = ['n','no']

    answer = input('Would you like to play again? (y/n) ').lower()
    if answer in yes:
        guessing_game()
        continue
    elif answer in no:
        break
    else:
        print("That is not an answer!")
        continue

