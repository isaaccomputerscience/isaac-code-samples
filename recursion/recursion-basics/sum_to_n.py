def sum_to_n(n):
    '''returns the sum of all natural numbers from 1 to n inclusive'''
    if n == 1:
        return 1
    else:
        return n + sum_to_n(n-1)
    
if __name__ =='__main__':
    n = 6
    result = sum_to_n(n)
    print ('The sum of 1 to {} is: {}'.format(n, result))
