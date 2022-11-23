# Raspberry Pi Foundation
# Developed to be used alongside Isaac Computer Science,
# part of the National Centre for Computing Education
# Usage licensed under CC BY-SA 4

def main():
    spelling_words = [
        ["school", "pull", "where"],
        ["path", "floor", "sugar"],
        ["accident", "eight", ""]]
  
    spelling_words[0][0] = "" 
    print(spelling_words)


# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == '__main__':
    main()
