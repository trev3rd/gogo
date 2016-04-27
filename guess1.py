import random


guessesTaken = 0 #this represents how many times the user has tried guessing the right number starting from zero

number = random.randint(1, 10)
print(number) #this shows the random number the computer picked good for seeing if code works properly


print(' I am thinking of a number between 1 and 10.')
while guessesTaken < 3:  #this says while the user has tried less than 3 times the follwoing shall happen

    print('Take a guess.')

    guess = input() # this basically allows the user to input a response from the above print statement

    guess = int(guess)# this makes sure that its a integer that should be guessed

    guessesTaken = guessesTaken + 1 # the "count" basically that you had in your code for the increments


    #this is where the if statements come in
    if guess == number +1 or guess == number -1: #as i said in class to give output hot if its 1 higher or lower

        print('Your guess is hot')

    if guess == number +2 or guess == number -2:#if its 2 higher or lower from random number

        print('Your guess is warm.')

    elif guess > number +2 or guess < number -2:#if greater than 2(3 or more/3 or less) it will say cold

        print('your guess is cold')

    if guess == number: # if the user gets the right number the following happends

        print('Good job! You guessed my number in ', guessesTaken)#outputs how many times it took user to guess
        break
if guess != number: # this is outside of loop to avoid a paradox and confusion with the top 3 ifs in the while statement

    print('Nope. The number I was thinking of was ', number)









