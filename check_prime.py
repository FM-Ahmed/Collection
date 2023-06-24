import numpy as np

def check_prime(n):
    if type(n) != int:
        raise ValueError('Input {} is not a whole number... Please provide an integer.'.format(n))
        
    nums = np.arange(1,n+1,1)
    frac_list = []
    
    for value in nums:
        if value <= n:
            frac = float(n/value)
            frac_list.append(frac)
    
    count = 0
    for number in frac_list:
        if str(number).endswith('.0'):
            count += 1
            if count >= 3:
                break
    if count == 2:
        statement = '{} is a prime!'.format(n)
    else:
        statement = '{} is not a prime...'.format(n)  
    return statement
