def check_prime2(x):
        # Input:
            # x: some arbitrary whole number.
        # Output:
            # is_prime: returns either True or False.
        
    if type(n) != int:
        raise ValueError('Input {} is not a whole number... Please provide an integer.'.format(n))
        
    rng = np.arange(1, x + 1, 1)
    c = 0
    for num in rng:
        if x % num == 0: 
            c += 1
            if c >= 3:
                break
    if c == 2:
        is_prime = True
    else: 
        is_prime = False
    return is_prime
