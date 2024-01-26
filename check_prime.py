import numpy as np

def check_prime(x):
    '''
        Input:
            x (int): some arbitrary whole number.
        Returns:
            bool: True if prime, False if not
    '''
    if not isinstance(x, int) or x <= 1:
        raise ValueError(f'Input {x} is invalid. Please provide a positive integer above 1.')
        
    if x % 2 == 0 and x != 2:
        return False
        
    rng = np.arange(1, np.sqrt(x) + 1, 1)
    c = 0
    for num in rng:
        if x % num == 0: 
            c += 1
            if c >= 3:
                break
    return c == 2
