import os
from itertools import product

def evaluate_left_to_right(numbers, operators):
    """Evaluate the expression left-to-right, including concatenation."""
    result = numbers[0]
    for i, op in enumerate(operators):
        if op == '+':
            result += numbers[i + 1]
        elif op == '*':
            result *= numbers[i + 1]
        elif op == '||':
            # Concatenate the digits as a number
            result = int(str(result) + str(numbers[i + 1]))
    return result

def solve_calibration(file_path):
    total_calibration_result = 0

    with open(file_path, "r") as file:
        puzzle_input = file.read()

    for line in puzzle_input.strip().split("\n"):
        target, nums = line.split(":")
        target = int(target.strip())
        numbers = list(map(int, nums.strip().split()))
        
        num_operators = len(numbers) - 1
        valid = False

        # Generate all possible operator combinations
        for operators in product("+-*||", repeat=num_operators):
            if evaluate_left_to_right(numbers, operators) == target:
                valid = True
                break
        
        if valid:
            total_calibration_result += target

    return total_calibration_result

if __name__ == "__main__":
    # Ensure the input file is in the same folder as this script
    file_name = "pattern.txt"
    file_path = os.path.join(os.path.dirname(__file__), file_name)

    result = solve_calibration(file_path)
    print("Total Calibration Result (with concatenation):", result)

