import random

user_answer = ['Y', 'YES', 'y', 'yes', 'ok']

while True:
    number = random.randint(1, 100)
#   print(number)
    for i in range(1, 10):
        guess = int(input(f"Enter your guess {i}: "))

        if guess != number:
            print("Incorrect guess!")
        else:
            print("You won! Want to play again?")
            answer = input("Your answer: ")

            if answer not in user_answer:
                exit()
            break
    else:
        print(f"You lost! The correct number is: {number} \nWant to play again?")
        answer = input("Your answer: ")

        if answer not in user_answer:
            break
