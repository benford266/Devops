import random, sys
randomnumbergen = random.randint(1,30)
def numberguess(randomnumber, attemptnumber):
    userGuess = input("guess the number ! ")
    userGuess = int(userGuess)
    if randomnumber > userGuess:
        print("Higher")
    elif randomnumber < userGuess:
        print("Lower")
    else:
        print("You guessed correct!")
        print("It took you {} attempts".format(attemptnumber))
        sys.exit()
for guess in range(1,7):
    numberguess(int(randomnumbergen), guess)