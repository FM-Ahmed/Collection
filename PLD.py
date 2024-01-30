class PLD:
    def __init__(self):
        self.gate = logic_gates()
    
    def process_inputs(self, binary_string):
        A = binary_string[0]
        not_A = self.gate.not_gate(binary_string[0])
        
        B = binary_string[1]
        not_B = self.gate.not_gate(binary_string[1])
        
        C = binary_string[2]
        not_C = self.gate.not_gate(binary_string[2])
        
        D = binary_string[3]
        not_D = self.gate.not_gate(binary_string[3])
        return A, not_A, B, not_B, C, not_C, D, not_D
    
    def is_4bit_prime(self, binary_string):
        self.gate.validate_binary(binary_string)
        if not len(binary_string) == 4:
            raise ValueError(f'Input must be a 4-bit binary number.')
        
        A, not_A, B, not_B, C, not_C, D, not_D = self.process_inputs(binary_string)
        
        t1 = self.gate.and_gate(not_A + not_B + C + not_D)
        t2 = self.gate.and_gate(not_A + not_B + C + D)
        t3 = self.gate.and_gate(not_A + B + not_C + D)
        t4 = self.gate.and_gate(not_A + B + C + D)
        t5 = self.gate.and_gate(A + not_B + C + D)
        t6 = self.gate.and_gate(A + B + not_C + D)
        
        p = self.gate.or_gate(t1 + t2 + t3 + t4 + t5 + t6)
        return int(p) == 1
    
    def add_two_binary(self, first_binary, second_binary):
        for inp in (first_binary, second_binary):
            if not isinstance(inp, str) or (not all(bit in '01' for bit in inp)) or (len(inp) < 1):
                raise ValueError(f'Input must be a n-bit binary number.') # check if the input is valid
        
            max_len = max(len(first_binary), len(second_binary))
            if max_len < 5:
                first_binary = first_binary.zfill(4)
                second_binary = second_binary.zfill(4)
            else:
                first_binary = first_binary.zfill(max_len)
                second_binary = second_binary.zfill(max_len)
    
        str_length = len(first_binary)
        carry_bit = '0'
        ans = []
            
        for i in range(str_length-1, -1, -1):
            if carry_bit == '0':
                if self.gate.nor_gate(first_binary[i] + second_binary[i]) == '1':
                    ans.append('0')
                    carry_bit = '0'
                elif self.gate.xor_gate(first_binary[i] + second_binary[i]) == '1':
                    ans.append('1')
                    carry_bit = '0'
                elif self.gate.and_gate(first_binary[i] + second_binary[i]) == '1':
                    ans.append('0')
                    carry_bit = '1'
            elif carry_bit == '1':
                if self.gate.nor_gate(first_binary[i] + second_binary[i]) == '1':
                    ans.append('1')
                    carry_bit = '0'
                elif self.gate.xor_gate(first_binary[i] + second_binary[i]) == '1':
                    ans.append('0')
                    carry_bit = '1'
                elif self.gate.and_gate(first_binary[i] + second_binary[i]) == '1':
                    ans.append('1')
                    carry_bit = '1'
            
        if carry_bit == '1':
            ans.append('1')
        return ''.join(ans[::-1])
