# Exercise 1
def check_integer(num):
    return num > 10 and num % 2 == 0

number = 12
result = check_integer(number)
print(f"Is {number} even and greater than 10? {result}")

# Exercise 2 
def determine_ticket_price(age, is_student):
    return 10 if age < 25 or is_student else 20 

age = 18  
is_student = True  
ticket_price = determine_ticket_price(age, is_student)
print(f"Ticket price: ${ticket_price}")

# Exercise 3
fruit_list = ["apple", "banana", "orange", "grape", "mango"]

user_fruit = input("Enter a fruit name: ").strip().lower()  
if user_fruit in fruit_list:
    print("Yes, that fruit is in the list.")
else:
    print("No, that fruit is not in the list.")

# Exercise 4
def is_century_leap_year(year):
    if year % 100 == 0:  
        return year % 400 == 0 
    return year % 4 == 0 

year = 2000  
if is_century_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

# Exercise 5
def calculate_shipping_cost(weight, zone):
    if weight < 0:
        return "Error: Weight cannot be negative."
    
    if zone == "A":
        cost_per_kg = 5
    elif zone == "B":
        cost_per_kg = 7
    else:
        return "Error: Invalid zone. Please enter 'A' or 'B'."
    
    total_cost = weight * cost_per_kg
    return total_cost

weight = 10  
zone = "A"   
shipping_cost = calculate_shipping_cost(weight, zone)

if isinstance(shipping_cost, str):
    print(shipping_cost) 
else:
    print(f"The shipping cost for {weight} kg to Zone {zone} is: ${shipping_cost}")

# Exercise 6 
def triangle_type(a, b, c):
    if a <= 0 or b <= 0 or c <= 0 or (a + b <= c) or (a + c <= b) or (b + c <= a):
        return "Not a triangle"
    if a == b == c:
        return "Equilateral"
    elif a == b or b == c or a == c:
        return "Isosceles"
    else:
        return "Scalene"

side1 = 3
side2 = 4
side3 = 5
print(triangle_type(side1, side2, side3))
