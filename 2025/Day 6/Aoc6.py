def solve_day6(filename):
    """Solve cephalopod math worksheet.

    Input is a small number of rows (numbers) with a final row of operators.
    Problems are arranged horizontally and separated by full-blank columns.
    For each problem, read the vertical numbers (all rows except the last),
    apply the operator from the last row (+ or *), and sum all problem results.
    """
    with open(filename, 'r') as f:
        lines = f.read().splitlines()

    if not lines:
        return 0

    # Normalize line lengths
    max_len = max(len(line) for line in lines)
    lines = [line.ljust(max_len) for line in lines]
    num_rows = len(lines)

    # Find problem column ranges by scanning for blank columns
    problems = []
    in_problem = False
    start = 0
    for col in range(max_len):
        is_blank = all(lines[row][col].isspace() for row in range(num_rows))
        if not is_blank and not in_problem:
            in_problem = True
            start = col
        elif is_blank and in_problem:
            in_problem = False
            problems.append((start, col))
    if in_problem:
        problems.append((start, max_len))

    total = 0
    for start, end in problems:
        # Collect numbers from all rows except last
        numbers = []
        for row in range(num_rows - 1):
            chunk = lines[row][start:end].strip()
            if not chunk:
                continue
            # chunk should be a single integer, but if it contains multiple tokens
            # pick the last token (right-aligned numbers) as a fallback
            tokens = chunk.split()
            try:
                numbers.append(int(tokens[-1]))
            except Exception:
                continue

        # Operator is on the last row
        op_chunk = lines[-1][start:end].strip()
        op = None
        if op_chunk:
            # operator chunk might contain spaces; take first non-space char
            for ch in op_chunk:
                if ch in ('+', '*'):
                    op = ch
                    break

        if not numbers or op is None:
            continue

        # Compute the problem result
        res = numbers[0]
        if op == '+':
            for n in numbers[1:]:
                res += n
        else:  # '*'
            for n in numbers[1:]:
                res *= n

        total += res

    return total


def solve_day6_part2(filename):
    """Part 2: numbers are written right-to-left in columns.

    For each problem block, read columns from right to left. Each column
    (within the problem) contains the digits of a single number stacked
    top-to-bottom (most significant at top). Extract each column's digits,
    parse into integers (skipping empty columns), then apply the operator
    (from the last row) to the numbers in that right-to-left order.
    """
    with open(filename, 'r') as f:
        lines = f.read().splitlines()

    if not lines:
        return 0

    max_len = max(len(line) for line in lines)
    lines = [line.ljust(max_len) for line in lines]
    num_rows = len(lines)

    # Find problem boundaries (same as part1)
    problems = []
    in_problem = False
    start = 0
    for col in range(max_len):
        is_blank = all(lines[row][col].isspace() for row in range(num_rows))
        if not is_blank and not in_problem:
            in_problem = True
            start = col
        elif is_blank and in_problem:
            in_problem = False
            problems.append((start, col))
    if in_problem:
        problems.append((start, max_len))

    total = 0
    for start, end in problems:
        # operator for this problem
        op_chunk = lines[-1][start:end]
        op = None
        for ch in op_chunk:
            if ch in ('+', '*'):
                op = ch
                break
        if op is None:
            continue

        # collect numbers by reading columns right-to-left
        numbers = []
        for col in range(end - 1, start - 1, -1):
            # build digit string top->bottom from rows 0..num_rows-2
            digits = []
            for row in range(num_rows - 1):
                ch = lines[row][col]
                if not ch.isspace():
                    digits.append(ch)
            if not digits:
                continue
            num_str = ''.join(digits)
            try:
                numbers.append(int(num_str))
            except Exception:
                # if parsing fails, skip this column
                continue

        if not numbers:
            continue

        # compute result
        res = numbers[0]
        if op == '+':
            for n in numbers[1:]:
                res += n
        else:
            for n in numbers[1:]:
                res *= n

        total += res

    return total


if __name__ == '__main__':
    import os

    fname = 'input_day_6'
    if not os.path.exists(fname):
        print("Input file 'input_day_6' not found.")
    else:
        p1 = solve_day6(fname)
        p2 = solve_day6_part2(fname)
        print('Day 6 - Part 1:', p1)
        print('Day 6 - Part 2:', p2)

