# Raspberry Pi Foundation
# Developed to be used alongside Isaac Computer Science,
# part of the National Centre for Computing Education
# Usage licensed under CC BY-SA 4
# https://isaaccomputerscience.org/concepts/prog_softeng_debug

with open("highscores.txt", "r") as file_object:
    lines = file_object.readlines()
    print(lines)
    