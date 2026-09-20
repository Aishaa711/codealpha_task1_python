# Hangman Game 🎮

A simple Python console-based Hangman game where the player tries to guess a randomly selected word one letter at a time.

## Features

* Randomly selects a word from a predefined word list.
* Provides a hint after 4 incorrect guesses.
* Allows up to 7 incorrect guesses.
* Displays correctly guessed letters and hides the remaining letters.
* Preserves spaces and hyphens in words.
* Prevents repeated letter guesses.
* Validates the input to allow only one character at a time.
* Shows the final result when the game ends.

## How to Play

1. Run the Python program.
2. Enter one letter at a time when prompted.
3. Correct guesses reveal the letters in the word.
4. You receive a hint after 4 incorrect guesses.
5. You lose after 7 incorrect guesses.
6. Guess all the letters before reaching the limit to win.

## Example

```text
Welcome to the Hangman game!

Guess a letter: a
You guessed the letter correctly
_a___

Guess a letter: z
You guessed the letter incorrectly
_a___

...

You won!
```

## Technologies

* Python
* `random` module
* Dictionaries
* Loops
* Conditional statements
* Lists
* Input validation
* Exception-free input handling

## How to Run

Make sure Python is installed, then run:

```bash
python main.py
```

Enjoy the game! 🎮
