# Raspberry Pi Foundation
# Developed to be used alongside Isaac Computer Science,
# part of the National Centre for Computing Education
# Usage licensed under CC BY-SA 4


def read_file_with_exception_handler():
    """Use an exception handler to catch file not found error"""
    try:
        with open("twynkle.txt", mode = "r") as playlist:
            for track in playlist:
                print(track)
    except FileNotFoundError:
        print("The file could not be found")


# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == "__main__":
    read_file_with_exception_handler()
