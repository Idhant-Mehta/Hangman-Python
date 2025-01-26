import random
import tkinter as tk
from tkinter import messagebox

def choose_word():
    words = ["apple", "banana", "orange", "strawberry", "grape", "pineapple"]
    return random.choice(words)

def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def reset_game():
    global word, guessed_letters, attempts, word_label, attempts_label
    word = choose_word()
    guessed_letters = set()
    attempts = 6
    word_label.config(text=display_word(word, guessed_letters))
    attempts_label.config(text=f"Attempts Left: {attempts}")

def check_guess():
    global attempts
    guess = guess_entry.get().lower().strip()
    guess_entry.delete(0, tk.END)

    if len(guess) == 1:  # Single letter guess
        if guess in guessed_letters:
            messagebox.showinfo("Info", "You already guessed that letter. Try a different one.")
        elif guess in word:
            guessed_letters.add(guess)
            word_label.config(text=display_word(word, guessed_letters))
            if all(letter in guessed_letters for letter in word):
                messagebox.showinfo("Congratulations!", f"You guessed the word: {word}")
                reset_game()
        else:
            attempts -= 1
            attempts_label.config(text=f"Attempts Left: {attempts}")
            if attempts == 0:
                messagebox.showinfo("Game Over", f"Sorry, you ran out of attempts. The word was: {word}")
                reset_game()
    elif len(guess) == len(word):  # Full word guess
        if guess == word:
            messagebox.showinfo("Congratulations!", f"You guessed the word: {word}")
            reset_game()
        else:
            attempts -= 1
            attempts_label.config(text=f"Attempts Left: {attempts}")
            if attempts == 0:
                messagebox.showinfo("Game Over", f"Sorry, you ran out of attempts. The word was: {word}")
                reset_game()
    else:
        messagebox.showinfo("Invalid Input", "Please guess a single letter or the full word.")

# Initialize the game
word = choose_word()
guessed_letters = set()
attempts = 6

# Create the GUI
root = tk.Tk()
root.title("Hangman Game")

# Word display
word_label = tk.Label(root, text=display_word(word, guessed_letters), font=("Helvetica", 18))
word_label.pack(pady=20)

# Attempts left
attempts_label = tk.Label(root, text=f"Attempts Left: {attempts}", font=("Helvetica", 14))
attempts_label.pack(pady=10)

# Guess input
guess_frame = tk.Frame(root)
guess_frame.pack(pady=10)

guess_label = tk.Label(guess_frame, text="Enter your guess: ", font=("Helvetica", 12))
guess_label.pack(side=tk.LEFT)

guess_entry = tk.Entry(guess_frame, font=("Helvetica", 12))
guess_entry.pack(side=tk.LEFT)

submit_button = tk.Button(guess_frame, text="Submit", command=check_guess, font=("Helvetica", 12))
submit_button.pack(side=tk.LEFT, padx=5)

# Reset button
reset_button = tk.Button(root, text="Reset Game", command=reset_game, font=("Helvetica", 12))
reset_button.pack(pady=20)

# Start the GUI loop
root.mainloop()
