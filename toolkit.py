# Personal Mini-Toolkit
# This program gives the user three simple tools through a menu.

import random

# This list stores the user's to-do tasks while the program is running.
tasks = []

# Welcome message
print("Welcome to your Personal Mini-Toolkit!")
print("Choose a tool to get started.\n")


# This tool lets the user add, view, and remove tasks from a list.
def todo_list():
    print("\n--- TO-DO LIST ---")

    while True:
        print("\n1. Add a task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. Back to main menu")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            task = input("Enter a task: ")
            tasks.append(task)
            print(f"Added task: {task}")

        elif choice == "2":
            if len(tasks) == 0:
                print("Your to-do list is empty.")
            else:
                print("\nYour tasks:")
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")

        elif choice == "3":
            if len(tasks) == 0:
                print("There are no tasks to remove.")
            else:
                number = int(input("Enter the task number to remove: "))

                if number >= 1 and number <= len(tasks):
                    removed_task = tasks.pop(number - 1)
                    print(f"Removed task: {removed_task}")
                else:
                    print("That task number does not exist.")

        elif choice == "4":
            print("Returning to the main menu.")
            break

        else:
            print("Please choose a number from 1 to 4.")


# This tool performs basic calculations using two numbers.
def calculator():
    print("\n--- SIMPLE CALCULATOR ---")

    try:
        number1 = float(input("Enter the first number: "))
        number2 = float(input("Enter the second number: "))

        print("\nChoose an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")

        operation = input("Enter your choice (1-4): ")

        if operation == "1":
            result = number1 + number2
            print(f"{number1} + {number2} = {result}")

        elif operation == "2":
            result = number1 - number2
            print(f"{number1} - {number2} = {result}")

        elif operation == "3":
            result = number1 * number2
            print(f"{number1} * {number2} = {result}")

        elif operation == "4":
            if number2 == 0:
                print("Sorry, you cannot divide by zero.")
            else:
                result = number1 / number2
                print(f"{number1} / {number2} = {result}")

        else:
            print("Please choose a number from 1 to 4.")

    except ValueError:
        print("Please enter valid numbers.")


# This tool lets the user guess a secret number between 1 and 10.
def guessing_game():
    print("\n--- NUMBER GUESSING GAME ---")
    print("I am thinking of a number between 1 and 10.")

    secret_number = random.randint(1, 10)
    guesses = 0

    while True:
        try:
            guess = int(input("Enter your guess: "))
            guesses += 1

            if guess < secret_number:
                print("Too low. Try again.")
            elif guess > secret_number:
                print("Too high. Try again.")
            else:
                print(f"Congratulations! You guessed the number in {guesses} tries.")
                break

        except ValueError:
            print("Please enter a whole number.")


# Main menu loop
while True:
    print("==============================")
    print("   PERSONAL MINI-TOOLKIT")
    print("==============================")
    print("1. To-Do List")
    print("2. Simple Calculator")
    print("3. Number Guessing Game")
    print("4. Quit")
    print("==============================")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        todo_list()

    elif choice == "2":
        calculator()

    elif choice == "3":
        guessing_game()

    elif choice == "4":
        print("Thank you for using the Personal Mini-Toolkit. Goodbye!")
        break

    else:
        print("Sorry, that is not a valid choice. Please choose 1, 2, 3, or 4.")