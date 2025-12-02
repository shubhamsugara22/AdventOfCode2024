def is_invalid_id(n):
    s = str(n)
    # Must have even number of digits
    if len(s) % 2 != 0:
        return False
    mid = len(s) // 2
    # First half repeated twice
    return s[:mid] == s[mid:]

def solve(filename):
    with open(filename, "r") as f:
        line = f.read().strip()

    total = 0
    ranges = line.split(",")

    for r in ranges:
        start, end = map(int, r.split("-"))
        for n in range(start, end + 1):
            if is_invalid_id(n):
                total += n

    return total


# Run on your input file
file_path = "input_day_2"  # change if needed
answer = solve(file_path)
print("Sum of all invalid IDs =", answer)
def is_invalid_id_part2(n):
    s = str(n)
    L = len(s)

    # Try all possible block lengths
    for k in range(1, L // 2 + 1):
        if L % k != 0:
            continue  # must divide evenly

        repeat_count = L // k
        if repeat_count < 2:
            continue  # must repeat at least twice

        block = s[:k]

        if block * repeat_count == s:
            return True

    return False


def solve_part2(filename):
    with open(filename, "r") as f:
        line = f.read().strip()

    total = 0
    ranges = line.split(",")

    for r in ranges:
        start, end = map(int, r.split("-"))
        for n in range(start, end + 1):
            if is_invalid_id_part2(n):
                total += n

    return total


# Run it
file_path = "input_day_2"  # adjust if needed
answer = solve_part2(file_path)
print("Part 2 sum of invalid IDs =", answer)
