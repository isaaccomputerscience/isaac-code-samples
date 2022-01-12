
email = input("Enter your email address: ")
verify_email = input("Re-type your email address: ")

if email == verify_email:
    print("The emails match")
else:
    print("Error: the email addresses did not match")
