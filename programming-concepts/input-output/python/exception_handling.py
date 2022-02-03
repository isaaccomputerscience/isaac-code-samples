
print("Enter a number")
try:
    user_input = input()
    number = int(user_input)
except ValueError:
    print("You must enter a numeric value")
