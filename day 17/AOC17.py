def run_program(initial_A, initial_B, initial_C, program):
    # Initialize registers
    A = initial_A
    B = initial_B
    C = initial_C
    
    # Instruction pointer starts at 0
    ip = 0
    output = []

    # Define the program length
    program_length = len(program)

    # Helper function to calculate combo operands
    def combo_value(operand):
        if operand == 0: return 0
        if operand == 1: return 1
        if operand == 2: return 2
        if operand == 3: return 3
        if operand == 4: return A
        if operand == 5: return B
        if operand == 6: return C
        return None  # Operand 7 is invalid

    # Run the program
    while ip < program_length:
        opcode = program[ip]       # Current instruction opcode
        operand = program[ip + 1]  # Operand for the instruction

        if opcode == 0:  # adv: A //= 2 ^ combo_operand
            combo = combo_value(operand)
            A //= 2 ** combo
        
        elif opcode == 1:  # bxl: B ^= literal_operand
            B ^= operand
        
        elif opcode == 2:  # bst: B = combo_operand % 8
            combo = combo_value(operand)
            B = combo % 8
        
        elif opcode == 3:  # jnz: If A != 0, jump to literal_operand
            if A != 0:
                ip = operand
                continue  # Do not increment ip
        
        elif opcode == 4:  # bxc: B ^= C (ignores operand)
            B ^= C
        
        elif opcode == 5:  # out: Output combo_operand % 8
            combo = combo_value(operand)
            output.append(combo % 8)
        
        elif opcode == 6:  # bdv: B = A // 2 ^ combo_operand
            combo = combo_value(operand)
            B = A // (2 ** combo)
        
        elif opcode == 7:  # cdv: C = A // 2 ^ combo_operand
            combo = combo_value(operand)
            C = A // (2 ** combo)
        
        # Move to the next instruction
        ip += 2

    # Return the output as a comma-separated string
    return ",".join(map(str, output))


# Initial values for registers
initial_A = 47792830
initial_B = 0
initial_C = 0

# Program provided in the puzzle
program = [2,4,1,5,7,5,1,6,4,3,5,5,0,3,3,0]

# Run the program and print the output
output = run_program(initial_A, initial_B, initial_C, program)
print("Final output:", output)