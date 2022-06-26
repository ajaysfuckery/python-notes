# String methods - A string method performs an operation on
# or gives us information about our strings

name = "Bro Code"

# Print the amount of chars in a string
print(len(name))

# Find the first index of the specified character
print(name.find("B"))

# Captialize the string
print(name.capitalize())

# Convert string to upper case 
print(name.upper())

# Convert string to lowercase
print(name.lower())

# Check if name is a number
print(name.isdigit())

# Checks if name is an alphabet (doesn't include spaces)
print(name.isalpha())

# Count the amount of times a character is found in string
print(name.count("o"))

# Replace all instances of "o" with "a"
print(name.replace("o", "a"))

# NOTE-: This is not a string method
# Prints name 10 times
print(name*10)