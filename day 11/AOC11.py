def process_stones(stones):
    """Simulates a single blink and updates the stones."""
    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        elif len(str(stone)) % 2 == 0:
            mid = len(str(stone)) // 2
            left = int(str(stone)[:mid])
            right = int(str(stone)[mid:])
            new_stones.extend([left, right])
        else:
            new_stones.append(stone * 2024)
    return new_stones

def simulate_blinks(initial_stones, blinks):
    """Simulates the given number of blinks and returns the final stones."""
    stones = initial_stones
    for _ in range(blinks):
        stones = process_stones(stones)
    return stones

def count_stones_after_blinks(initial_stones, blinks):
    """Counts the total number of stones after the specified number of blinks."""
    final_stones = simulate_blinks(initial_stones, blinks)
    return len(final_stones)

# Example input
initial_stones = [2 ,77706 ,5847 ,9258441, 0 ,741 ,883933 ,12]
blinks = 75

# Calculate the result
result = count_stones_after_blinks(initial_stones, blinks)
print(f"Total stones after {blinks} blinks: {result}")
