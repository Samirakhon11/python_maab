import random

while True:
    number = random.randint(1, 100)

    for i in range(1, 10):
        guess = int(input(f"Enter your guess {i}: "))

        if guess != number:
            print("Incorrect guess!")
        else:
            print("You won! Want to play again?")
    else:
        print(f"You lost! The correct number is - {number} \nWant to play again?")
        answer = input("Your answer: ")

        if answer not in ['Y', 'YES', 'y', 'yes', 'ok']:
            break
