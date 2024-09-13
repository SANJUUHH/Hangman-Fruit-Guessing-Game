# Hangman Fruit Guessing Game

## Description
This is a Python implementation of the classic Hangman game, where the player has to guess the name of a randomly selected fruit within a limited number of guesses. The game gives the player a number of chances to guess each letter of the fruit's name. The player wins if they guess the fruit name correctly before running out of chances.

## Features
- Randomly selects a fruit from a predefined list.
- Provides hints by showing the number of characters in the fruit's name.
- Tracks the number of guesses and displays remaining chances.
- Displays the current state of the fruit name with guessed letters revealed and unguessed letters as underscores.
- Informs the player if they guess a letter more than once.

## How to Play
1. The game will select a random fruit from a list and give you the number of characters in that fruit.
2. You have a limited number of chances (length of the fruit name + 2) to guess the letters.
3. Type a letter and press Enter. The game will check if the letter exists in the fruit name.
4. If you guess all the letters correctly, you win. If you run out of chances, the game will end and reveal the correct word.

## Example Gameplay

```plaintext
************WELCOME TO THE HANGMAN GAME !!!************

You have to guess the fruit name.
HINT: The selected random fruit has 5 characters in it.
You have 7 chances to guess the fruit name.
_ _ _ _ _ 

Enter the guess letter/character: a
_ a _ a _ 

Enter the guess letter/character: p
Incorrect Guess.
Now, you have only 6 chances left.
_ a _ a _ 

Enter the guess letter/character: b
Incorrect Guess.
Now, you have only 5 chances left.
_ a _ a _ 

Enter the guess letter/character: n
_ a n a _ 

Enter the guess letter/character: r
_ a n a _ 

Enter the guess letter/character: g
Correct! You guessed the word: banana
