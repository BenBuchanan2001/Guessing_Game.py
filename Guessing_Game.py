import random

ComGuess = random.randint(0,1000)
print("I'm thinking of a number between 0 and 1000.")

while True:
    UserGuess = int(input("Try guessing the number: "))
    if UserGuess > ComGuess:
        print("nope too high! Try again.")
    elif UserGuess < ComGuess:
        print("nope too low! Try again.")
    else:
        print("Aye! You got it right")
        break