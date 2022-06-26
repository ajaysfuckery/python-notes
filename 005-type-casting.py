# Type casting - convert the data type of a value
# to another value

x = 1       # Int
y = 2.0     # Float
z = "3"     # String

print(x)
print(x)
print(x)

print(int(y))
print(int(z))

# To make the type cast permanent we must re-assign
# the value/variable
y = int(y)

# We cannot do math with strings
print(z*3)  # prints 333

z = int(z)
print(z*3)

x = float(x)
y = float(y)
z = float(z)

print(x)
print(y)
print(z)

x = str(x)
y = str(y)
z = str(z)

print('X is', x)
print('Y is', y)
print('Z is', z)