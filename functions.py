import numpy as np

# Function uses the following definition of prime numbers:
# It is a prime IF it can be divided by EXACTLY two numbers.
# I.e. 1 is not a prime.

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

def number_of_primes(n):
    if type(n) != int:
        raise ValueError('Input {} is not a whole number... Please provide an integer.'.format(n))
        
    nums = np.arange(1,n+1,1)
    
    results = []
    for value in nums:
        result = check_prime(int(value))
        results.append(result)

    count = 0
    for item in results:
        if '!' in item:
            count += 1
            
    primes = []
    for val in nums:
        is_prime = check_prime(int(val))
        if '!' in is_prime:
            primes.append(val)  
            
    return primes, count
