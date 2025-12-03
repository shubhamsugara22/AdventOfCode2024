def max_joltage_for_bank(bank):
    # Convert to list of ints for convenience
    digits = list(map(int, bank.strip()))

    best = 0
    n = len(digits)

    # Try every pair (i, j) with i < j
    for i in range(n - 1):
        for j in range(i + 1, n):
            val = digits[i] * 10 + digits[j]
            if val > best:
                best = val
    return best


def solve_day3(filename):
    total = 0
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            total += max_joltage_for_bank(line)
    return total


# Run on your input:
file_path = "input_day_3"   # change path if different
answer = solve_day3(file_path)
print("Total output joltage =", answer)
