# test.py
# Demonstrating variables, functions, and user input

# 1 - Sum
def add_numbers(a, b):
    return a + b

# 2 - Subtract
def subtract_numbers(a, b):
    return a - b

# 3 - Multiplication
def multiply_numbers(a, b):
    return a * b

# 4 - Division
def divide_numbers(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

# 5 - Guess my age
def guess_my_age():
    secret_age = 24  # you can change this
    guess = int(input("Guess my age: "))
    if guess == secret_age:
        print("Correct! 🎉")
    elif guess < secret_age:
        print("Too low, try again!")
    else:
        print("Too high, try again!")

# ---- Main Program ----
if __name__ == "__main__":
    # Demo math functions
    x = int(input("Enter the first number: "))
    y = int(input("Enter the second number: "))

    print(f"Sum: {add_numbers(x, y)}")
    print(f"Subtract: {subtract_numbers(x, y)}")
    print(f"Multiply: {multiply_numbers(x, y)}")
    print(f"Divide: {divide_numbers(x, y)}")

    # Run age guessing game
    guess_my_age()
