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

def max_k_digits(num_str, k):
    """
    Returns the largest possible number (as string) formed by keeping exactly k digits
    in the same order using a monotonic stack.
    """
    remove = len(num_str) - k
    stack = []

    for ch in num_str:
        while remove > 0 and stack and stack[-1] < ch:
            stack.pop()
            remove -= 1
        stack.append(ch)

    return "".join(stack[:k])


def solve_joltage_parts(filename):
    total_part1 = 0  # For k = 2
    total_part2 = 0  # For k = 12

    with open(filename) as f:
        for line in f:
            s = line.strip()
            if not s:
                continue

            # Part 1: choose best 2 digits
            best2 = int(max_k_digits(s, 2))
            total_part1 += best2

            # Part 2: choose best 12 digits
            best12 = int(max_k_digits(s, 12))
            total_part2 += best12

    return total_part1, total_part2


# Run on actual input file
file_path = "input_day_3"
part1, part2 = solve_joltage_parts(file_path)

print("Part 1 Total Joltage:", part1)
print("Part 2 Total Joltage:", part2)
