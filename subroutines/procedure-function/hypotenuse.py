# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0
# https://isaaccomputerscience.org/concepts/prog_sub_proc_fun


def squared(length):
    area = length * length
    return area


def get_hypotenuse(a, b):
    import math
    hypotenuse = math.sqrt( squared(a) + squared(b) ) 
    return hypotenuse



def main():
    hyp = get_hypotenuse(3, 4)
    print(hyp)


if __name__ == '__main__':
    main() 