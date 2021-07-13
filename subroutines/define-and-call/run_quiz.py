# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0
# https://isaaccomputerscience.org/concepts/prog_sub_define_and_call

def run_quiz():
    """Ask a quiz question"""
    print("What is the capital city of Botswana?")
    answer = input()


def main():
    name = input("What is your name? ")
    run_quiz() 
    print("End of the quiz")


if __name__ == '__main__':
    main()