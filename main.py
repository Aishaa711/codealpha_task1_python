import random

words = {
    "summer": "hot season",
    "glasses": "help you see",
    "blanket": "keeps you warm",
    "chicken": "a farm bird",
    "university": "place for higher education",
    "photosynthesis": "plants make food",
    "sister": "female sibling",
    "wizard": "magical person",
    "hip-hop": "urban dance",
    "ballet": "classical dance",
    "sand castle": "made on the beach",
    "popcorn": "movie snack",
    "hat": "worn on your head",
    "hygiene": "keeping yourself clean",
    "counting": "numbers in order",
    "video games": "played for fun",
    "hacking": "unauthorized computer access",
    "programming": "writing computer code",
    "password": "protects an account",
    "yes": "opposite of no",
    "funny": "makes you laugh",
    "question": "asks for information",
    "kangaroo": "Australian animal",
    "dinosaur": "extinct reptile",
    "intelligence": "IQ",
    "century": "100 years",
    "millennia": "1000 years",
    "pyramids": "Egypt",
    "cruise ship": "Titanic",
    "treasure": "map"
}
word = random.choice(list(words.keys()))
hint = words[word]
wrong_guesses = 0
guessed_letters = [" ", "-"]
won = False
while wrong_guesses < 7:
    guess = input("Guess a letter: ")
    if guess in word:
        print("You guessed the letter correctly")
        guessed_letters.append(guess)

    else:
        print("You guessed the letter incorrectly")
        wrong_guesses += 1
    for letter in word:
        if letter in guessed_letters:
            print(letter, end="")
        else:
            print("_", end="")

    print(" ")
    if wrong_guesses == 4:
        print("Hint:", hint)

    won = True

    for letter in word:
        if letter not in guessed_letters:
            won = False
            break

    if won:
        break
if won:
    print("You won!")
else:
    print("You lost!")
    print("The word was:", word)
