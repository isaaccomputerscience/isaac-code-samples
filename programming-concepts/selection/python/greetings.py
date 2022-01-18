
print("What hour is it?")
user_input = input()
hour = int(user_input)

if hour < 12:
    print("Good morning")
elif hour < 18:
    print("Good afternoon")
elif hour < 22:
    print("Good evening")
else:
    print("Good night")
