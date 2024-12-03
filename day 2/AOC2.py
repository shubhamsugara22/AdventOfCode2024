import os

def check_row(row):
    """Checks if a row satisfies the conditions."""
    increasing = True
    decreasing = True

    for i in range(1, len(row)):
        diff = row[i] - row[i - 1]
        if abs(diff) < 1 or abs(diff) > 3:  # Check if difference is outside [1, 3]
            return "Unsafe"
        if diff <= 0:  # Not increasing
            increasing = False
        if diff >= 0:  # Not decreasing
            decreasing = False

    if increasing or decreasing:
        return "Safe"
    else:
        return "Unsafe"
    
def is_safe_with_tolerance(row):
    """Checks if a row can be safe by removing at most one level."""
    if check_row(row) == "Safe":
        return "Safe"

    # Test if removing one level makes the row safe
    for i in range(len(row)):
        modified_row = row[:i] + row[i + 1:]  # Remove the ith element
        if check_row(modified_row) == "Safe":
            return "Safe"
    return "Unsafe"

def main():
    # Ensure the input file exists
    file_name = "row.txt"
    file_path = os.path.join(os.getcwd(), file_name)
    
    if not os.path.exists(file_path):
        print(f"Error: '{file_name}' not found in the current directory ({os.getcwd()}).")
        return

    # Read rows from the file
    with open(file_path, "r") as file:
        matrix = [list(map(int, line.strip().split())) for line in file]

    safe_count = 0  # Counter for safe rows
    # Process each row
    print("\nResults:")
    for i, row in enumerate(matrix, 1):
        result = is_safe_with_tolerance(row)
        print(f"Row {i}: {result}")
        if result == "Safe":
            safe_count += 1

    print(f"\total safe rows :{safe_count}")
    

if __name__ == "__main__":
    main()
