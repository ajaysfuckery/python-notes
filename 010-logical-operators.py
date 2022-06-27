# Logical Operators -> used to check if 2 or more conditional statements
# are true

# LOGICAL OPERATORS
# -> and
# -> or
# -> not

temp = int(input("Temperature outside: "))

# if temp >= 0 and temp <= 30:                    # both conditions must be true for code to execute
#     print("The temperature is good today!")

# elif temp < 0 or temp > 30:                     # one or more conditions must be true for code to execute
#     print("The temperature is bad today!")
#     print("Stay inside!")

# else:
#     pass

if not(temp >= 0 and temp > 30):
    print("The temperature is bad today!")
    print("Stay inside!")

elif not(temp < 0 or temp > 30):
    print("The temperature is good today!")

# The  not operator flips the conditions meaning that if a
# condition is true it will become false and vice versa