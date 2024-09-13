# GAME: Hangman Game or Fruit Guessing Game

import random

fruits = '''watermelon apple banana grapes orange pineapple '''
fruits = fruits.split(" ")

Selectedrandom = random.choice(fruits)

chances = len(Selectedrandom)+2

guesses = []

print()
print("************WELCOME TO THE HANGMAN GAME !!!************")
print()
print("You have to guess the fruit name.")
print("HINT: The selected random fruit have",len(Selectedrandom),"characters in it.")
print("You have",chances,"chances to guess the fruit name.")

print("_ "*len(Selectedrandom))

#Game Loop
while chances > 0:
    guess = input("Enter the guess letter/character: ").lower()
    if not guess.isalpha():
        print("You haven't entered any letter/character.") 
        continue
    if guess in Selectedrandom:
        guesses.append(guess)
    elif guess in guesses:
        print("You already guessed that letter.")  
        chances-=1
        print("Chances left = ",chances)
    else:
        guesses.append(guess)
        chances-=1
        print("Incorrect Guess.")
        print("Now, you have only",chances,"left.")

    current_state = "".join([guess if guess in guesses else "_" for guess in Selectedrandom])
    print(" ".join(current_state))

    if '_' not in current_state:
        print("Congratulations! You've guessed the word:",Selectedrandom)
        break
else:
    print("Sorry, you've run out of chances. The word was:", Selectedrandom)


