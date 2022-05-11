# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0

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
