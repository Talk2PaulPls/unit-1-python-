#Code 2
text = "Hello, world, my name is"
count = 0

for char in text:
    if char == ' ': # Add space between ("")
        count += 1

print(count)


#Code 3 
print("give me a number:")
n = int(input())  # Convert input to an integer

for num in range(1, n + 1):  # Include n by using n + 1
    if num % 2 == 0:  
        print(num, "is even.")
    else:
        print(num, "is odd.")


#Code 4 
num = int(input("Enter an integer: "))

if num < 0:  # Check for negative numbers
    print("No negative numbers.")
else:
    result = 1
    for i in range(1, num + 1):  # Include the number itself
        result *= i   

    print("Factorial of " + str(num) + " is " + str(result))  # Convert to string for concatenation

#Code 5 
attempts = 0
correct_password = "secret"

while True:
    password = input("Enter your password: ")
    attempts += 1

    if password == correct_password:  # Check against the correct password
        print("Correct password!")
        break  # Exit the loop if the password is correct
    else:
        print("Incorrect password")

    if attempts >= 3:  # Allow 3 attempts
        print("Too many attempts")
        break