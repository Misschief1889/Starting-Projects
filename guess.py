# This is a guess the number game.
import random

print('Hello. What is your name?')
name = input()

print('Well, ' + name + ', I am thinking of a number between one and 20.')
secretNumber = random.randint(1, 20)

for guessesTaken in range(1, 7):
    print('Take a guess!')
    
    try:
        guess = int(input())
    except:
        print('Please enter a number!')
        
    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break # This condition is a correct guess.

if guess == secretNumber:
    print('Good job, ' + name + '! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking was ' + str(secretNumber) + '.')
