import random

randomNumber = random.randrange(1,11,2)
print("Guess a number between 1-10")
chances=0

while(chances < 5):
    chances = chances+1
    guess = int(input("Guess a number: "))
    guessed = str(guess) 

    if (guess == randomNumber):
        chances = 5
        print("You win")
    elif(guess < randomNumber):
        print("Guess a higher number than " + guessed)
    elif(guess > randomNumber):
        print("Guess a lower number than " + guessed)