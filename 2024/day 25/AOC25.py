def parse_schematics(file_path):
    """Parse the input file to extract lock and key schematics."""
    with open(file_path, 'r') as f:
        data = f.read().strip().split("\n\n")

    locks = []
    keys = []

    for schematic in data:
        lines = schematic.split("\n")
        if lines[0] == "#####":  # Identify locks by the top row filled with '#'
            locks.append(lines)
        elif lines[-1] == "#####":  # Identify keys by the bottom row filled with '#'
            keys.append(lines)

    return locks, keys

def convert_to_heights(schematic, is_lock=True):
    """Convert a schematic to a list of heights."""
    num_columns = len(schematic[0])
    heights = []

    for col in range(num_columns):
        height = 0
        if is_lock:
            for row in range(len(schematic)):
                if schematic[row][col] == '#':
                    height += 1
                else:
                    break
        else:  # For keys
            for row in range(len(schematic) - 1, -1, -1):
                if schematic[row][col] == '#':
                    height += 1
                else:
                    break
        heights.append(height)

    return heights

def count_valid_pairs(locks, keys):
    """Count the number of valid lock-key pairs."""
    valid_pairs = 0
    max_height = len(locks[0])  # Total rows in the schematics

    for lock in locks:
        lock_heights = convert_to_heights(lock, is_lock=True)
        for key in keys:
            key_heights = convert_to_heights(key, is_lock=False)

            # Check if all columns fit
            fits = all(lh + kh <= max_height for lh, kh in zip(lock_heights, key_heights))
            if fits:
                valid_pairs += 1

    return valid_pairs

def main():
    file_path = "christmas.txt"  
    locks, keys = parse_schematics(file_path)
    result = count_valid_pairs(locks, keys)
    print(f"Number of unique lock/key pairs that fit: {result}")

if __name__ == "__main__":
    main()
