def count_fresh_ids(input_text: str) -> int:
    """
    Count IDs that fall within the safe ranges.
    
    Logic:
    - Parse the input to extract safe ranges and IDs
    - For each ID, check if it falls within any of the safe ranges
    - Count IDs that are within at least one range (safe/fresh)
    """
    lines = input_text.strip().splitlines()

    # Split on blank line to separate ranges from IDs
    blank_index = lines.index("")
    range_lines = lines[:blank_index]
    id_lines = lines[blank_index + 1:]

    # Parse ranges as (start, end) tuples
    ranges = []
    for line in range_lines:
        start, end = map(int, line.split("-"))
        ranges.append((start, end))

    # Parse ingredient IDs
    ids = list(map(int, id_lines))

    # Count fresh ones (IDs within any safe range)
    fresh_count = 0
    for val in ids:
        for start, end in ranges:
            if start <= val <= end:
                fresh_count += 1
                break  # no need to check other ranges

    return fresh_count


# ----- Run on your input file -----
if __name__ == "__main__":
    with open("input_day_5", "r") as f:
        data = f.read()

    answer = count_fresh_ids(data)
    print("Fresh IDs count:", answer)
