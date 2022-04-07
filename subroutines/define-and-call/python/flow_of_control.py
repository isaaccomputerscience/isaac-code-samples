# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0
# https://isaaccomputerscience.org/concepts/prog_sub_define_and_call

def main():
    """Simple demonstration of flow of control"""
    minutes = 90
    seconds = minutes * 60
    milliseconds = seconds * 1000
    print(f"Seconds: {seconds}, Milliseconds: {milliseconds}")


# This code will run if this file is executed directly (i.e. not called by another program)
if __name__ == '__main__':
    main()
