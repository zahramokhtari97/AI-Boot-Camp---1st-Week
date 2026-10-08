import random

number = random.randint(1, 100)

for attempt in range(5):
    guess = int(input("Guess the number: "))

    if guess < number:
        print("Guess higher")
    elif guess > number:
        print("Guess lower")
    else:
        print("Correct!")
        break
else:
    print("You lost!")
    print("The number was:", number)