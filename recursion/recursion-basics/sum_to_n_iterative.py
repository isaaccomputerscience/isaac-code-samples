def sum_to_n_iterative(n):
    '''returns the sum of all natural numbers from 1 to n inclusive'''
    total = 0
    for i in range (1, n + 1):
        total = total + i
    return total

    
if __name__ =='__main__':
    n = 6
    result = sum_to_n_iterative(n)
    print ('The sum of 1 to {} is: {}'.format(n, result))
