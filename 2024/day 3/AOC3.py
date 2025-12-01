import re

def calculate_sum_from_memory(memory):
    # Regular expression to match valid mul instructions
    pattern = r"mul\((\d+),(\d+)\)"
    
    # Find all matches in the memory
    matches = re.findall(pattern, memory)
    
    # Calculate the sum of the results of valid mul instructions
    total_sum = sum(int(x) * int(y) for x, y in matches)
    
    return total_sum

def calculate_sum_with_conditions(memory):
    # Regular expressions to match the instructions
    mul_pattern = r"mul\((\d+),(\d+)\)"
    do_pattern = r"do\(\)"
    dont_pattern = r"don't\(\)"
    
    # Initial state: mul instructions are enabled
    is_mul_enabled = True
    total_sum = 0
    
    # Scan the memory for instructions in order
    instructions = re.finditer(f"{mul_pattern}|{do_pattern}|{dont_pattern}", memory)
    
    for match in instructions:
        # Check which instruction is matched
        if match.group(1) and match.group(2):  # This is a mul(X,Y)
            if is_mul_enabled:
                x, y = int(match.group(1)), int(match.group(2))
                total_sum += x * y
        elif match.group(0) == "do()":
            is_mul_enabled = True
        elif match.group(0) == "don't()":
            is_mul_enabled = False
    
    return total_sum

# Read the input from a file
def read_input_file(file_name):
    try:
        with open(file_name, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found in the current directory.")
        return None

# Main program
if __name__ == "__main__":
    file_name = "scrambled.txt"  # Replace with your actual file name if different
    memory_input = read_input_file(file_name)
    
    if memory_input:
        result = calculate_sum_with_conditions(memory_input)
        print(f"The sum of all valid mul instructions is: {result}")
