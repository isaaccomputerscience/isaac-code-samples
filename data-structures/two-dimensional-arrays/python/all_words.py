# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0

def main():
    spelling_words = [
        ["school", "pull", "where"],
        ["path", "floor", "sugar"],
        ["accident", "answer", "eight"]]
  
    for level in range(3):
        for word in range(3):
            print(spelling_words[level][word])


# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == '__main__':
    main()
