'''
Python code for ICS hash function examples
Written by Di - December 2020

includes function to generate some collisions
'''

import random

def hash_it_v1(hash_key, number_of_slots):
    '''first example'''
    hash_value = hash_key % number_of_slots
    return hash_value


def hash_it_v2(hash_key, number_of_slots):
    '''second example'''
    my_sum = 0
    for i in range(len(hash_key)):
        ascii_code = ord(hash_key[i])
        my_sum = my_sum + ascii_code
    hash_value = my_sum % number_of_slots
    return hash_value

def find_a_key(value_sought, n):
    '''finds n keys that collide on a specific value for the platform scenario'''
    number_found = 0
    iterations = 0
    while number_found < n and iterations < 10000:
        n1 = random.randint(65, 90)
        n2 = random.randint(49, 57)
        n3 = random.randint(65, 90)
        n4 = random.randint(65, 90)
        total = n1 + n2 +n3 + n4
        hash_value = total % 97
        if hash_value == value_sought:
            number_found += 1
            print ('{}{}{}{}'.format(chr(n1),chr(n2),chr(n3),chr(n4)))
        iterations +=1
    
        
    
    


if __name__ == '__main__':
    key = 12345
    value = hash_it_v1(key, 97)
    print ('Value for {} is {}'.format(key, value))
    key = 'R2YJ'
    value = hash_it_v2(key, 97)
    print ('Value for {} is {}'.format(key, value))
    print ('Keys are: ')
    find_a_key(75, 13)
    
        
    
