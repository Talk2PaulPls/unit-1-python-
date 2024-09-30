# Task 1 (Simple Counter)
def simple_counter():
    counter = 1
    while counter <= 10:
        print(counter)
        counter += 1

simple_counter()

# Task 2 (Countdown)
def countdown():
    counter = 10
    while counter >= 1:
        print(counter)
        counter -= 1

countdown()

# Task 3 (Factorial Calculation)
def factorial_calculation():
    number = int(input("Enter a number to calculate it factorial: "))
    factorial = 1
    counter = 1
    
    while counter <= number:
        factorial *= counter
        counter += 1

    print(f"The factorial of {number} is {factorial}")

factorial_calculation()

# Task 4 (Password Guessing Game)
def password_guessing_game():
    correct_password = "python12345"
    attempts = 0
    max_attempts = 5
    
    print("Welcome to the Password Guessing Game!")
    print(f"You have {max_attempts} attempts to guess the password.")

    while attempts < max_attempts:
        guess = input("Enter your password guess: ")
        attempts += 1
        
        if guess == correct_password:
            print("Congratulations! You've guessed the password correctly!")
            break
        else:
            print("Incorrect guess. Try again.")
            print(f"Attempts left: {max_attempts - attempts}")

    if attempts == max_attempts:
        print(f"Sorry, you've used all your attempts. The correct password was '{correct_password}'.")
password_guessing_game()

# Task 6 (Fibonacci Series)
def fibonacci_series(n):
    a, b = 0, 1 
    count = 0    
    
    print("Fibonacci Series:")
    while count < n:
        print(a, end=" ")
        a, b = b, a + b  
        count += 1
        
n = int(input("Enter the number of Fibonacci numbers to print: "))
fibonacci_series(n)
