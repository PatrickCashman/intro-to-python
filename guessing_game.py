#Guessing game
import random

secret_number = random.randint(1,10)
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input('Guess a numer from 1 - 10: '))
    guess_count += 1

    if guess == secret_number:
        print("you win!")
        break
    elif guess != secret_number:
        print("try again!")
else:
   print("you lose! the number was ", secret_number) 


