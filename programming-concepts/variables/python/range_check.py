
user_input = input("Enter a week of the year: ")
week = int(user_input)

if week > 0 and week <= 52:
    print(f"You have chosen week {week}")
else:
    print("A week must be between 1-52")
