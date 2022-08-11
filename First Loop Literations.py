capitalGuess = input("What is the Capital of Australia? ")
numberOfGuesses = 1

while capitalGuess != " Canberra":
    numberOfGuesses = numberOfGuesses + 1
    capitalGuess = input("Guess again I guess, can't believe you got that wrong")

print("You finally got it right!")
print("Canberra is correct. It took you " + str(numberOfGuesses) + " guesses. ")
