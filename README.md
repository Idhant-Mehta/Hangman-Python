# Hangman Game

## Overview
This project is a graphical implementation of the classic **Hangman game** using Python's **Tkinter** library. The game randomly selects a word, and players must guess the word by entering letters or the entire word. Players have a limited number of attempts to guess correctly.

---

## Features
- **Graphical User Interface (GUI):** An interactive interface built with Tkinter.
- **Letter and Word Guesses:** Players can guess single letters or attempt to guess the full word.
- **Real-Time Feedback:** Displays the current progress of the word and remaining attempts.
- **Reset Button:** Allows restarting the game with a new word.

---

## How to Play
1. The game displays the word as underscores (`_`) representing unguessed letters.
2. Enter a single letter or the full word in the input box and click **Submit**.
3. Correct guesses reveal the letters in the word.
4. Incorrect guesses reduce the number of attempts.
5. Win the game by guessing the full word within the given attempts. Lose if attempts reach zero.

---

## Requirements
- **Python 3.6 or later**
- **Tkinter library** (comes pre-installed with Python)

---

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/hangman-game
   ```
2. Navigate to the project directory:
   ```bash
   cd hangman-game
   ```
3. Run the Python script:
   ```bash
   python hangman_game.py
   ```

---

## File Details
- **`hangman_game.py`**: Main script for the Hangman game.
- **`README.md`**: Documentation for the project.

---

## Example Gameplay
1. The game starts with a randomly selected word (e.g., `apple`).
2. Players see the word as `_ _ _ _ _`.
3. Guess letters (e.g., `a`, `p`) to reveal parts of the word:
   - Correct guesses update the display: `a p p _ _`.
   - Incorrect guesses reduce attempts: `Attempts Left: 5`.
4. Guess the full word to win or run out of attempts to lose.

---

## Future Enhancements
- Add difficulty levels (easy, medium, hard).
- Include a scoring system.
- Provide hints for the selected word

