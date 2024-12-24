import re
from collections import defaultdict

# Function to parse the input file
def parse_input(file_path):
    initial_values = {}
    gates = []

    with open(file_path, "r") as file:
        lines = file.readlines()
    
    # Split initial values and gates
    split_index = lines.index("\n")  # Find the blank line separating the sections
    initial_lines = lines[:split_index]
    gate_lines = lines[split_index + 1:]
    
    # Parse initial values
    for line in initial_lines:
        wire, value = line.strip().split(": ")
        initial_values[wire] = int(value)
    
    # Parse gates
    for line in gate_lines:
        parts = line.strip().split(" -> ")
        gates.append((parts[0], parts[1]))
    
    return initial_values, gates

# Evaluate expressions
def evaluate(expression, wire_values):
    """Evaluate the value of an expression based on the current wire values."""
    tokens = expression.split()
    if "AND" in tokens:
        return wire_values[tokens[0]] & wire_values[tokens[2]]
    elif "OR" in tokens:
        return wire_values[tokens[0]] | wire_values[tokens[2]]
    elif "XOR" in tokens:
        return wire_values[tokens[0]] ^ wire_values[tokens[2]]
    else:
        raise ValueError(f"Unknown gate type in expression: {expression}")

# Simulate the system
def simulate_system(initial_values, gates):
    wire_values = defaultdict(lambda: None)
    wire_values.update(initial_values)
    pending_gates = gates[:]
    processed_gates = set()

    while pending_gates:
        for i, (expression, output_wire) in enumerate(pending_gates):
            tokens = re.split(r"\s+", expression)
            inputs_ready = all(
                token.isdigit() or wire_values[token] is not None
                for token in tokens if token not in {"AND", "OR", "XOR"}
            )

            if inputs_ready:
                values = [
                    int(token) if token.isdigit() else wire_values[token]
                    for token in tokens if token not in {"AND", "OR", "XOR"}
                ]
                if "AND" in tokens:
                    result = values[0] & values[1]
                elif "OR" in tokens:
                    result = values[0] | values[1]
                elif "XOR" in tokens:
                    result = values[0] ^ values[1]
                else:
                    raise ValueError(f"Unexpected operator in: {expression}")

                wire_values[output_wire] = result
                processed_gates.add((expression, output_wire))
        
        # Remove processed gates
        pending_gates = [
            gate for gate in pending_gates if gate not in processed_gates
        ]

    return wire_values

# Convert binary to decimal
def binary_to_decimal(wire_values):
    output_bits = [wire_values[f"z{str(i).zfill(2)}"] for i in range(len(wire_values)) if f"z{str(i).zfill(2)}" in wire_values]
    binary_number = "".join(map(str, output_bits[::-1]))  # Reverse bits (LSB to MSB)
    return int(binary_number, 2)

# Main function
def main(file_path):
    initial_values, gates = parse_input(file_path)
    wire_values = simulate_system(initial_values, gates)
    result = binary_to_decimal(wire_values)
    print("Decimal output:", result)

# Run the program
file_path = "gates.txt"  
main(file_path)
