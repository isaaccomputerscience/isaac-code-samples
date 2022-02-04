# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0

def change_string(my_string):
    """Changes all lowercase a to lowercase b"""
    new_string = ""  # New empty string
    for char in my_string:
        if char == "a":
            new_string = new_string + "b"
        else:
            new_string = new_string + char
    return new_string


def test():
    """Test data"""
    my_string = "An aardvark is an animal"
    new_string = change_string(my_string)
    print(new_string)       

   
# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == '__main__':
    test()
