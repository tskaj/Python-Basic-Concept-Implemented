# Defining a class
class division:
    def __init__ (self, x,y):
        self.x= 5
        self.y = 10
        
# Addition & multiplication functions
def mul(x,y):
    return x*y
def add(x,y):
    return x+y
# Hello World in a method
def helloworld(): 
    print("Hello world")
    return 0
# Taking input from the user and printing it out in a function
x= int(input("Emter your first number: "))
y= int(input("Enter your second number: "))
print(f"Multiplication of your numbers are {mul(x,y)}")
print(f"Addition of your numbers are {add(x,y)}")

# Calling a class and printing out the values:
z= division(x,y)
print(z.x)
print(z.y)

# Implementing loops
for i in range(5):
    print(i)

# Looping through the list
names = ["Abdullah", "Ali", "Zainab"]
for name in names:
    print(name)

# Implementing decorators
def announce(f):
    def wrapper():
        print("About to run the function...")
        f()
        print("Done running the function.")
    return wrapper

@announce
def hello():
    print("Hello, Abdullah!")
hello()

# Looping through the dictionary
ages = {"Abdullah": 20, "Maryam": 19}
for age in ages:
    print (age)

# Implementing Exception Handling
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
try:
    print(f"{a} / {b} = {a / b}")
except ZeroDivisionError:
    print("Cannnot divide by 0")

# Implementing Conditions    
x = -1

if x > 0:
    print("x is positive")
elif x < 0:
    print("x is negative")
else:
    print("x is 0")

# Implementing Sets
t = set()
t.add(1)
t.add(3)
t.add(5)
t.add(3)
print(t)

# Implementing 
from functions import square
print(square(10))
