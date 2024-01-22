def dec_to_bin(dec_integer):
    if not isinstance(dec_integer, int):
        raise ValueError(f'Input must be an integer.') # check if the input is valid
    
    '''
    Convert a decimal number to binary number
    
    Args:
    - dec_integer (int): decimal number
    
    Returns:
    - str: binary representation of decimal number
    '''
    binary_digits = []
    while dec_integer > 0:
        mod = dec_integer % 2
        binary_digits.append(mod)
        dec_integer //= 2
    
    binary_number = ''.join(map(str, binary_digits[::-1]))
    return binary_number
