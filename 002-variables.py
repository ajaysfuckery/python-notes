# Variables - Container for data
# We can use variables later in our program
# Variables behave as the value we assign to it

# STRINGS - A collection of characters
firstName = "Bro"
lastName = "Code"

print("Hello", firstName)

# Check the data type of a variable
print(type(firstName))

# We have 3 different ways of combining variables
# - Concatenation (works with strings only)
# - F-Strings (works with any data type)
# - Commas following variable names (works with any data type)
# - Combining variables of the same data type within a new variable

# Examples below
print("Hello " + firstName)
print(f"Hello {firstName}")
print(firstName, lastName)

fullName = firstName + " " + lastName
print(fullName)

# INTs - Integer
# When assigning int's do not use quotes
# or they will become a string
age = 21

print(age)

# Adding 1 to the value of age
age = age + 1
print(age)

# Short way of doing the code above
age += 1
print(age)

# Check the type of age
print(type(age))

# Combining age with string literal
print("You are " + str(age))
print("You are", age)
print(f"You are {age}")

# Float - A float is a decimal number
height = 250.5

print(height)

# Check for type of height
print(type(height))

print("Your height is " + str(height) + " cm")
print("Your height is", height, "cm")
print(f"Your height is {height} cm")

# Booleans - True or False
isHuman = True

print(isHuman)

# Check for type
print(type(isHuman))

print("Are you a human?: " + str(isHuman))
print("Are you a human?:", isHuman)
print(f"Are you a human?: {isHuman}")