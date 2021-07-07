def show_password_length():
    """Prompts for a password and displays length"""
    password = input("Please enter a password ")
    print(len(password))

if __name__ == "__main__":
    show_password_length()
