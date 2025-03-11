import random

yes = ['YyEeSs']
no = ['NnOo']

def Magic_8_ball():
    response = random.randint(1,21)
    if response == 1:
        return "It is certain"
    elif response == 2:
        return "It is decidedly so."
    elif response == 3:
        return "Without a doubt."
    elif response == 4:
        return "Yes, definitely."
    elif response == 5:
        return "You may rely on it."
    elif response == 6:
        return "As I see it, yes."
    elif response == 7:
        return "Most likely."
    elif response == 8:
        return "Outlook good."
    elif response == 9:
        return "Yes."
    elif response == 10:
        return "Signs point to yes."
    elif response == 11:
        return "Don't count on it."
    elif response == 12:
        return "My reply is no."
    elif response == 13:
        return "My sources say no."
    elif response == 14:
        return "Outlook not so good."
    elif response == 15:
        return "Very doubtful."
    elif response == 16:
        return "Reply hazy, try again."
    elif response == 17:
        return "Concentrate and ask again."
    elif response == 18:
        return "Better not tell you now."
    elif response == 19:
        return "Cannot predict now."
    elif response == 20:
        return "Ask again later."

answer = input("Would you like to ask a question? ")   

# create loop for: 1) asking if they want to ask a question, 2) exiting if they do not
# 3) a means for responding to incorrect inputs, 4) "thinking" message (with progress bar?)

while answer in yes:
    input("Ask the Oracle your question: ")
    Magic_8_ball()
    if answer in no:
        print("May fortune favor you.")
        break
    else:
        print("That is not an answer.")
        continue
    continue
        