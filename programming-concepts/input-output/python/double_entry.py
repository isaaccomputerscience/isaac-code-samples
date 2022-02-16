# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0

def main():
    email = input("Enter your email address: ")
    verify_email = input("Re-type your email address: ")

    if email == verify_email:
        print("The emails match")
    else:
        print("Error: the email addresses did not match")


# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == '__main__':
    main()
