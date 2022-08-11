from random import randint

for i in range(3):
    guess = int(input("Guess a number between 1 and 10. "))
    randNum = randint(1, 10)
    if guess == randNum:
        print("You found the match")
        break
    else:
        print("You didn't find the match!")

print("Game over!")

