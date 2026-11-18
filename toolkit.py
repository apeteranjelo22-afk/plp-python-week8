
# ==========================================
# PERSONAL MINI-TOOLKIT
# Week 8 Final Python Project
# ==========================================

import random

# Store tasks in a list while the program runs
tasks = []


# TOOL 1: SIMPLE CALCULATOR
# Performs basic mathematical operations.
def calculator():
    print("\n--- SIMPLE CALCULATOR ---")

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        print("\nChoose an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")

        operation = input("Enter your choice (1-4): ")

        if operation == "1":
            result = num1 + num2
        elif operation == "2":
            result = num1 - num2
        elif operation == "3":
            result = num1 * num2
        elif operation == "4":
            if num2 == 0:
                print("Sorry, division by zero is not allowed.")
                return
            result = num1 / num2
        else:
            print("Invalid operation. Please try again.")
            return

        print(f"The answer is: {result}")

    except ValueError:
        print("Please enter valid numbers.")


# TOOL 2: TO-DO LIST MANAGER
# Allows users to add, view and remove tasks.
def todo_list():
    while True:
        print("\n--- TO-DO LIST MANAGER ---")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. Return to main menu")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            task = input("Enter a task: ")

            if task.strip():
                tasks.append(task)
                print(f"Task '{task}' added successfully!")
            else:
                print("Task cannot be empty.")

        elif choice == "2":
            print("\nYour Tasks:")

            if len(tasks) == 0:
                print("Your task list is empty.")
            else:
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")

        elif choice == "3":
            if len(tasks) == 0:
                print("There are no tasks to remove.")
            else:
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")

                try:
                    task_number = int(
                        input("Enter the task number to remove: ")
                    )

                    if 1 <= task_number <= len(tasks):
                        removed = tasks.pop(task_number - 1)
                        print(f"Task '{removed}' removed successfully!")
                    else:
                        print("Invalid task number.")

                except ValueError:
                    print("Please enter a valid number.")

        elif choice == "4":
            print("Returning to the main menu...")
            break

        else:
            print("Invalid choice. Please select 1, 2, 3 or 4.")


# TOOL 3: NUMBER GUESSING GAME
# Challenges users to guess a secret number.
def guessing_game():
    secret_number = random.randint(1, 10)
    attempts = 0

    print("\n--- NUMBER GUESSING GAME ---")
    print("I have chosen a number between 1 and 10.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < 1 or guess > 10:
                print("Please choose a number between 1 and 10.")
            elif guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(
                    f"Congratulations! You guessed correctly "
                    f"in {attempts} attempts."
                )
                break

        except ValueError:
            print("Please enter a whole number.")


# TOOL 4: GRADE CHECKER
# Calculates a grade based on the user's marks.
def grade_checker():
    print("\n--- GRADE CHECKER ---")

    try:
        marks = float(input("Enter your marks (0-100): "))

        if marks < 0 or marks > 100:
            print("Invalid marks. Enter a number between 0 and 100.")
        elif marks >= 80:
            grade = "A"
        elif marks >= 70:
            grade = "B"
        elif marks >= 60:
            grade = "C"
        elif marks >= 50:
            grade = "D"
        else:
            grade = "F"

        if 0 <= marks <= 100:
            print(f"Your marks are {marks}.")
            print(f"Your grade is: {grade}")

    except ValueError:
        print("Please enter a valid number.")


# MAIN PROGRAM
# Displays the menu and runs until the user chooses Quit.
def main():
    print("=" * 40)
    print("WELCOME TO MY PERSONAL MINI-TOOLKIT!")
    print("=" * 40)

    while True:
        print("\nPlease choose a tool:")
        print("1. Simple Calculator")
        print("2. To-Do List Manager")
        print("3. Number Guessing Game")
        print("4. Grade Checker")
        print("5. Quit")

        choice = input("\nEnter your choice (1-5): ")

        if choice == "1":
            calculator()
        elif choice == "2":
            todo_list()
        elif choice == "3":
            guessing_game()
        elif choice == "4":
            grade_checker()
        elif choice == "5":
            print("\nThank you for using my toolkit!")
            print("Goodbye! Have a wonderful day.")
            break
        else:
            print(
                f"Sorry, '{choice}' is not a valid choice. "
                "Please select a number from 1 to 5."
            )


# Start the program
if __name__ == "__main__":
    main()
