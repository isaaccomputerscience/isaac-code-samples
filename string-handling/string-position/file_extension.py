# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0

def extract_file_extention():
    """Demonstrates how to extract a file extension"""
    file_name = "monster.csv"
    dot_location = file_name.find(".")
    print(dot_location)
    position = dot_location + 1
    print(file_name[position:]) # Prints the remainder of the string
    

if __name__ == '__main__':
    extract_file_extention()
