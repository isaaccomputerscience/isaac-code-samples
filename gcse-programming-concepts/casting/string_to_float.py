'''

version: 1.0
date: April 2021

'''

def double_it():
    '''prompts user for a number and doubles it'''
    number = input("Please enter a number ")
    float_number = float(number)
    answer = float_number * 2
    print('The answer is ',answer)
    print('{:.2f}'.format(answer))

if __name__ == '__main__':
    double_it()
