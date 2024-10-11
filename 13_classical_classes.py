# Task 1: People
class Person:
    def __init__(self, name, age):

        self.name = name
        self.age = age

    def hi(self):
    
        print(f"Hello, my name is {self.name} and I am {self.age} years old")

personA = Person("Paulina", 114)
personA.hi() 

personB = Person("Ensley", 131)
personB.hi()

# Task 2: Animal Talking 
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Hello Im a dog and I can speak "

class Cat(Animal):
    def speak(self):
        return "Hello Im a cat and I can also speak"

dog = Dog()
cat = Cat()

print(dog.speak())
print(cat.speak())

# Task 3: Banking
class Bankaccount:
    def __init__(self, owner, balance=0):

        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraws money from the account and updates the balance."""
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance:.2f}")
        else:
            print("Invalid withdrawal amount.")
