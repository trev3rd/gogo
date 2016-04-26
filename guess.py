import random


guessesTaken = 0

number = random.randint(1, 10)
print(number)


print(' I am thinking of a number between 1 and 10.')
while guessesTaken < 3:

    print('Take a guess.')

    guess = input()

    guess = int(guess)

    guessesTaken = guessesTaken + 1



    if guess == number +1 or guess == number -1:

        print('Your guess is hot')

    if guess == number +2 or guess == number -2:

        print('Your guess is warm.')

    elif guess > number +2 or guess < number -3:

        print('your guess is cold')

    if guess == number:

        break




if guess == number:

    guessesTaken = str(guessesTaken)

    print('Good job! You guessed my number in ' + guessesTaken )

if guess != number:

    number = str(number)

    print('Nope. The number I was thinking of was ' + number)









