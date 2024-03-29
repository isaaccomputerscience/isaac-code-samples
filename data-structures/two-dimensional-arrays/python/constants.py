# Raspberry Pi Foundation
# Developed to be used alongside Isaac Computer Science,
# part of the National Centre for Computing Education
# Usage licensed under CC BY-SA 4

LEVEL1 = 0
LEVEL2 = 1
LEVEL3 = 2

def main():
    spelling_words = [
        ["school", "pull", "where"],
        ["path", "floor", "sugar"],
        ["accident", "answer", "eight"]]
  
    for word in range (3):
        print(spelling_words[LEVEL2][word])


# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == '__main__':
    main()
