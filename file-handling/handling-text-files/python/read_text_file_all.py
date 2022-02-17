# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0
     

def read_all():
    """Read all the data from a file"""
    with open("playlist.txt", mode = "r") as playlist:
        data = playlist.read()
    return data


def main():
    data = read_all()
    print(data)
    print(type(data))  # So that you can see it is a single string


# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == "__main__":
    main()   
