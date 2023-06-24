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
        # Input:
            # n: some arbitrary integer, larger number = slower function
        # Output:
            # primes: a list of prime numbers between 1 and n.
            # count: how many prime numbers there are between 1 and n.
    
    if type(n) != int:
        raise ValueError('Input {} is not a whole number... Please provide an integer.'.format(n))
        
    nums = np.arange(1,n+1,1)
    
    count = 0
    results = []
    primes = []
    for value in nums:
        result = check_prime(int(value))
        if '!' in result:
            count += 1
            primes.append(value) 
                   
    return primes, count
