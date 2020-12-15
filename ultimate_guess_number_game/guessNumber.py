import random

counter = 0
name = input('Hello. What is your name?\n')

print('Well, {}, I am thinking a number between 1 and 20.'.format(name))
print('Take a guess..')

secretNumber = random.randint(1, 20)

for guessNumber in range(1, 7):
    chance = 6
    try:
        guess = int(input())
        
    except:
        print('Dude supply a valid number'); continue
        
    if guess not in range(1, 20): print('Out of scope [1-20]'); continue
    
    if guess > secretNumber:
        counter += 1
        print('Your guess is too high. You have {} chance/s'.format(chance - guessNumber))
    elif guess < secretNumber:
        counter += 1
        print('Your guess is too low. You have {} chance/s'.format(chance - guessNumber))
    else:
        print('Good job, {}, you guessed my number in {} tries'.format(name, counter))
        break

if guess != secretNumber:
    print('\nNope, the number that I was thinking of was: {}'.format(secretNumber))
