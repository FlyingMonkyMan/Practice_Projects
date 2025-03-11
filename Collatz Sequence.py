# for any number entered: if even: //2, if odd: (3*num) +1
# continue until  "1"

def collatz_sequence(number):
    while number > 1:
        if number % 2 == 0:
            number = number // 2
            print(number)
        elif number % 2 != 0:
            number = (number * 3) + 1
            print(number)
    
    
while True:    
    try:
        number = int(input("Please enter a number: "))
    except ValueError:
        print("Value entered must be a number!")
        continue

    collatz_sequence(number)
    break