from collections import Counter

def process_stones_optimized(stone_counts):
    """Simulates a single blink and updates the stones using a Counter."""
    new_stone_counts = Counter()
    for stone, count in stone_counts.items():
        if stone == 0:
            new_stone_counts[1] += count
        elif len(str(stone)) % 2 == 0:
            mid = len(str(stone)) // 2
            left = int(str(stone)[:mid])
            right = int(str(stone)[mid:])
            new_stone_counts[left] += count
            new_stone_counts[right] += count
        else:
            new_stone_counts[stone * 2024] += count
    return new_stone_counts

def simulate_blinks_optimized(initial_stones, blinks):
    """Simulates the given number of blinks using a Counter for optimization."""
    stone_counts = Counter(initial_stones)
    for _ in range(blinks):
        stone_counts = process_stones_optimized(stone_counts)
    return stone_counts

def count_stones_after_blinks_optimized(initial_stones, blinks):
    """Counts the total number of stones after the specified number of blinks."""
    final_stone_counts = simulate_blinks_optimized(initial_stones, blinks)
    return sum(final_stone_counts.values())

initial_stones = [2, 77706, 5847, 9258441, 0, 741, 883933, 12]
blinks = 75

# Calculate the result
result = count_stones_after_blinks_optimized(initial_stones, blinks)
print(f"Total stones after {blinks} blinks: {result}")
