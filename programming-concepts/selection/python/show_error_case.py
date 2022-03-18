# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0

def show_error():
    """Example of a match/case statement to match the error code"""
    error_code = input("Enter the error code: ")
    
    match error_code:
        case "400":
            print("Bad request")
        case "401":
            print("Unauthorised request")
        case "403":
            print("Forbidden request")
        case "404":
            print("Page not found")
        case "408":
            print("Timeout error")
        case _:
            print("Unknown error")


# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == '__main__':
    show_error()
