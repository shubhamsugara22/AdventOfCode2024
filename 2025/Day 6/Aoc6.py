def solve_day6(filename):
    # Read input lines and pad to equal width
    with open(filename, "r") as f:
        rows = [line.rstrip("\n") for line in f]

    if not rows:
        return 0

    width = max(len(r) for r in rows)
    grid = [r.ljust(width) for r in rows]

    # Transpose into columns (each column is a string of characters from top to bottom)
    cols = ["".join(grid[y][x] for y in range(len(grid))) for x in range(width)]

    # Split contiguous non-blank columns into separate problems
    problems = []
    current = []
    for col in cols:
        if col.strip() == "":
            if current:
                problems.append(current)
                current = []
        else:
            current.append(col)
    if current:
        problems.append(current)

    total_sum = 0

    # Process each problem block
    for problem in problems:
        # Reconstruct the rows for this problem by joining the columns that belong to it
        block_rows = ["".join(col[row_idx] for col in problem) for row_idx in range(len(rows))]

        numbers = []
        op = None

        # Parse each line in the block. Lines may contain multiple tokens separated by whitespace.
        for line in block_rows:
            tokens = line.split()
            if not tokens:
                continue
            for tok in tokens:
                if tok in ("+", "*"):
                    op = tok
                else:
                    # Try to parse integer tokens; skip non-integer tokens silently
                    try:
                        numbers.append(int(tok))
                    except ValueError:
                        # If token is not an int and not an operator, ignore it
                        continue

        if op is None:
            raise ValueError("Operation not found in problem block; expected '+' or '*'.")

        # Compute the problem value depending on the operator
        if op == "+":
            value = sum(numbers)
        else:  # op == '*'
            value = 1
            for n in numbers:
                value *= n

        total_sum += value

    return total_sum


if __name__ == "__main__":
    # Run on local input file named `input_day_6` in the same directory
    try:
        result = solve_day6("input_day_6")
        print("Total sum for Day 6:", result)
    except FileNotFoundError:
        print("Input file 'input_day_6' not found in the current directory.")
