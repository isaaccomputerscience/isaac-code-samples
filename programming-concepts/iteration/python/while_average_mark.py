
sum = 0
num_values = 0

user_input = input("Enter a mark or -1 to end ")
mark = int(user_input)

while mark != -1:
    sum = sum + mark
    num_values = num_values + 1
    user_input = input("Enter a mark or -1 to end ")
    mark = int(user_input)

average = sum / num_values
print(f"The average mark was {average}")
