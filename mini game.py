import random

def choose_word():
    words = ["apple", "banana", "orange", "strawberry", "grape", "pineapple"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print(display_word(word, guessed_letters))

    while attempts > 0:
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word:
            guessed_letters.append(guess)
            print("Good guess!")
        else:
            attempts -= 1
            print(f"Wrong! You have {attempts} attempts left.")

        print(display_word(word, guessed_letters))

        if all(letter in guessed_letters for letter in word):
            print("Congratulations! You guessed the word:", word)
            break

    if attempts == 0:
        print("Sorry, you ran out of attempts. The word was:", word)

if __name__ == "__main__":
    hangman()
