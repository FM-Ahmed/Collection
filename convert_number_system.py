class convert_number_system:
    def __init__(self):
        pass
    
    def bin_to_dec(self, binary_string):   
        '''
        Convert a binary number to decimal number

        Args:
        - binary_string (str): binary number in string format

        Returns:
        - int: decimal equivalent of binary input 
        '''
        bits = len(binary_string) # determine number of bits
        if not all(bit in '01' for bit in binary_string):
            raise ValueError('Input must be a n-bit binary number.') # check if the input is valid

        # convert to binary and return in decimal form
        decimal_number = 0
        for i in range(0, len(binary_string)):
            decimal_number += int(binary_string[i]) * 2**((bits-1)-i)
        return decimal_number

    def dec_to_bin(self, decimal_number):
        '''
        Convert a decimal number to binary number

        Args:
        - dec_integer (int): decimal number

        Returns:
        - str: binary representation of decimal number
        '''
        if not isinstance(decimal_number, int):
            raise ValueError('Input must be an integer.') # check if the input is valid

        binary_digits = []
        while decimal_number > 0:
            mod = decimal_number % 2
            binary_digits.append(mod)
            decimal_number //= 2

        binary_number = ''.join(map(str, binary_digits[::-1]))
        return binary_number

    def dec_to_hex(self, decimal_number):
        '''
        Convert a decimal number to hex number

        Args:
        - decimal_number (integer): decimal number

        Returns:
        - (str): hex equivalent of decimal input
        '''
        if not isinstance(decimal_number, int):
            raise ValueError('Input must be an integer.') # check if the input is valid
        hex_values = {0: '0',
                      1: '1',
                      2 : '2',
                      3: '3',
                      4: '4',
                      5: '5',
                      6: '6',
                      7: '7',
                      8: '8',
                      9: '9',
                      10: 'A',
                      11: 'B',
                      12: 'C',
                      13: 'D',
                      14: 'E',
                      15: 'F'}

        ans = []
        floor = float('inf')
        while floor != 0:
            div = decimal_number / 16
            floor = decimal_number // 16
            remainder = div - floor
            ans.append(hex_values[int(remainder*16)])
            decimal_number = floor
        return ''.join(ans[::-1])
    
    def hex_to_dec(hex_string):
        '''
        Convert a hex number to decimal number

        Args:
        - hex_string (string): hexadecimal number

        Returns:
        - (int): decimal equivalent of hexadecimal input
        '''
        if not all(bit in '0123456789ABCDEF' for bit in hex_string):
            raise ValueError('Input must be a hex number.') # check if the input is valid
        hex_values = {0: '0',
                      1: '1',
                      2 : '2',
                      3: '3',
                      4: '4',
                      5: '5',
                      6: '6',
                      7: '7',
                      8: '8',
                      9: '9',
                      10: 'A',
                      11: 'B',
                      12: 'C',
                      13: 'D',
                      14: 'E',
                      15: 'F'}

        reversed_hex_values = dict((v, k) for (k, v) in hex_values.items())
        decimal_number = 0
        for i in range(0, len(hex_string), 1):
            decimal_number += reversed_hex_values[hex_string[i]]*16**(len(hex_string) - 1 - i)
        return decimal_number
