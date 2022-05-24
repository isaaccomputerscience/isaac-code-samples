# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0


def demonstrate_empty_string():
    """Demonstrates the difference between an empty string and a space"""
    empty_string = ""
    print(len(empty_string))
    
    string_with_space = " "
    print(len(string_with_space))
    
    if empty_string == string_with_space:
        print("We are the same")
    else:
        print("We are different")


# This code will run if this file is executed directly
# (i.e. not called by another program)       
if __name__ == "__main__":
    demonstrate_empty_string()
