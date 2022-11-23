# Raspberry Pi Foundation
# Developed to be used alongside Isaac Computer Science,
# part of the National Centre for Computing Education
# Usage licensed under CC BY-SA 4
# https://isaaccomputerscience.org/concepts/prog_sub_define_and_call

def run_quiz():
    """A very simple quiz"""
    answer = input("What is the capital city of Botswana? ")
    if answer == "Gaborone":
        print("Well done!")
    else:
        print("Sorry! That is the wrong answer")

def main():
    name = input("What is your name? ")
    print(f"Welcome {name}")
    run_quiz() 
    print("End of the quiz")   
    
# This code will run if this file is executed directly (i.e. not called by another program)
if __name__ == '__main__':
    main()
