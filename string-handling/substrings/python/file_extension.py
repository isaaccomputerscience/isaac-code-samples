# Raspberry Pi Foundation
# Developed to be used alongside Isaac Computer Science,
# part of the National Centre for Computing Education
# Usage licensed under CC BY-SA 4

def get_extension(file_name):
    """Extracts everything after dot in file name"""    
    dot_location = file_name.find(".")
    index = dot_location + 1
    extension = file_name[index:] # Gets the remainder of the string
    return extension


def test():
    file_name = "monster.csv"
    extension = get_extension(file_name)
    print(extension)

        
# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == '__main__':
    test()
