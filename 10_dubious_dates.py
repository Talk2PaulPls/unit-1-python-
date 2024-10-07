from datetime import datetime

# Exercise 1
# Get the current date and time
now = datetime.now()
# Print the current date and time
print("Current date and time:", now)

# Exercise 2
# Format the date in MM/DD/YYYY
formatted_date = now.strftime("%m/%d/%Y")
print("Current date in U.S. format:", formatted_date)

# Exercise 3
# Define two date strings
date_string1 = "2023-10-01"
date_string2 = "2024-01-01"
# Convert strings to date objects
date1 = datetime.strptime(date_string1, "%Y-%m-%d")
date2 = datetime.strptime(date_string2, "%Y-%m-%d")
# Calculate the difference in days
difference = (date2 - date1).days
print("Difference in days:", difference)

# Exercise 4
# Ask the user for their birthdate
birthdate_input = input("Enter your birthdate (YYYY-MM-DD): ")

try:
    # Convert the input string to a date object
    birthdate = datetime.strptime(birthdate_input, "%Y-%m-%d")
    # Get the current date
    today = datetime.now()
    # Calculate age
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    print("Your current age is:", age)
except ValueError:
    print("Invalid date format. Please use YYYY-MM-DD.")
