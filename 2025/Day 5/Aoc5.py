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


def count_fresh_ids_part2(filename):
    """
    Part 2: Count total number of fresh IDs covered by merged safe ranges.
    
    Logic:
    - Extract all safe ranges from input
    - Sort ranges by start value
    - Merge overlapping or touching ranges into continuous intervals
    - Count total IDs covered by all merged ranges
    
    This efficiently counts how many IDs are fresh by merging ranges
    and calculating the total coverage without iterating each ID.
    """
    with open(filename, "r") as f:
        lines = [line.strip() for line in f.readlines()]

    # Split at blank line
    blank_index = lines.index("")
    fresh_ranges = lines[:blank_index]

    intervals = []
    for r in fresh_ranges:
        start, end = map(int, r.split("-"))
        intervals.append((start, end))

    # Sort ranges by start
    intervals.sort()

    # Merge the intervals
    merged = []
    current_start, current_end = intervals[0]

    for s, e in intervals[1:]:
        if s <= current_end + 1:  # overlapping or touching
            current_end = max(current_end, e)
        else:
            merged.append((current_start, current_end))
            current_start, current_end = s, e

    merged.append((current_start, current_end))

    # Count total IDs covered by merged ranges
    total_fresh_ids = sum(e - s + 1 for s, e in merged)

    return total_fresh_ids



# ----- Run on your input file -----
if __name__ == "__main__":
    with open("input_day_5", "r") as f:
        data = f.read()

    # Part 1: Count IDs within ranges
    print("="*50)
    print("PART 1: Count fresh IDs by checking each ID")
    print("="*50)
    answer1 = count_fresh_ids(data)
    print("Fresh IDs count:", answer1)
    
    # Part 2: Count total IDs covered by merged ranges
    print("\n" + "="*50)
    print("PART 2: Count fresh IDs by merging ranges")
    print("="*50)
    answer2 = count_fresh_ids_part2("input_day_5")
    print("Total fresh IDs (by merged ranges):", answer2)
