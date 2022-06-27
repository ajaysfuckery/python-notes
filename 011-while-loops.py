# While loop -> executes while a condition is true

name = ""

while len(name) == 0:
    name = input("Enter your name?: ")

print("Hello", name)

name = None

while not None:
    name = input("Enter a name?: ")

print("Hello", name)