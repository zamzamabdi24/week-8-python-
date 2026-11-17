# Personal Mini-Toolkit

This is a menu-driven Python program with three simple tools: a to-do list, a simple calculator, and a number-guessing game.

## How to run it

1. Download or clone this repository.
2. Open the folder in VS Code.
3. Run this command in the terminal:

```bash
python toolkit.py
```

## What the toolkit does

- The **To-Do List** lets users add, view, and remove tasks.
- The **Simple Calculator** adds, subtracts, multiplies, or divides two numbers.
- The **Number Guessing Game** asks the user to guess a secret number between 1 and 10.
- The main menu keeps returning until the user chooses **Quit**.
- Invalid menu choices are handled politely without crashing the program.

## Reflection

The hardest part was making sure the menu kept returning after each tool finished. I also had to handle invalid choices so the program would not crash when a user typed the wrong number. The bug that took the longest to fix was making the to-do list remove the correct task, because list positions start at 0 while task numbers start at 1. I fixed it by subtracting 1 from the user’s chosen number. I tested every menu option, including an invalid choice and quitting. With one more week, I would add a tool that saves the to-do list to a file so tasks remain after the program closes.
