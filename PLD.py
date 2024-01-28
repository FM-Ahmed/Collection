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
    
    def is_a_prime(self, binary_string):
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
