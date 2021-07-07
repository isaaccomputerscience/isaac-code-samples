def demonstrate_nulls():
    """Demonstrates the difference between a null and a space"""
    null_string = ""
    print(len(null_string))
    string_with_space = " "
    print(len(string_with_space))
    if null_string == string_with_space:
        print("We are the same")
    else:
        print("We are different")

        
if __name__ == "__main__":
    demonstrate_nulls()
