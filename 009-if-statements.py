# If statement -> a block of code that will execute if it's condition
# is true

# The order of if-statements matters for code to execute correctly

age = int(input("Enter your age: "))

if age == 100:
    print("Congratulations on being 100 years old!")

elif age >= 18:
    print("You are an adult!")

elif age < 0:
    print("You haven't been born yet!")

else:
    print("You are a child!")