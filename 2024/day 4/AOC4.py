## part 1
def count_word_occurrences(filename, word="XMAS"):
    # Read the grid from the file
    with open(filename, 'r') as file:
        grid = [line.strip() for line in file if line.strip()]

    rows, cols = len(grid), len(grid[0])
    word_length = len(word)
    directions = [
        (0, 1),   # Right
        (1, 0),   # Down
        (1, 1),   # Diagonal Down-Right
        (1, -1),  # Diagonal Down-Left
        (0, -1),  # Left
        (-1, 0),  # Up
        (-1, -1), # Diagonal Up-Left
        (-1, 1),  # Diagonal Up-Right
    ]

    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols

    def count_from(r, c, dr, dc):
        """Count occurrences of the word starting from (r, c) in direction (dr, dc)."""
        for i in range(word_length):
            nr, nc = r + dr * i, c + dc * i
            if not is_valid(nr, nc) or grid[nr][nc] != word[i]:
                return 0
        return 1

    total_count = 0

    # Iterate over the grid and check for the word in all directions
    for r in range(rows):
        for c in range(cols):
            for dr, dc in directions:
                total_count += count_from(r, c, dr, dc)

    return total_count
## part 2
def count_x_mas_occurrences(filename):
    # Read the grid from the file
    with open(filename, 'r') as file:
        grid = [line.strip() for line in file if line.strip()]

    rows, cols = len(grid), len(grid[0])
    patterns = ["MAS", "SAM"]  # Possible "MAS" patterns, including reversed
    x_mas_count = 0

    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols

    def check_x_mas(center_r, center_c):
        """Check for an X-MAS centered at (center_r, center_c)."""
        # Coordinates for the diagonals
        diag1 = [(center_r - 1, center_c - 1), (center_r, center_c), (center_r + 1, center_c + 1)]
        diag2 = [(center_r - 1, center_c + 1), (center_r, center_c), (center_r + 1, center_c - 1)]

        # Ensure all positions are valid
        if not all(is_valid(r, c) for r, c in diag1 + diag2):
            return 0

        # Extract characters for both diagonals
        chars_diag1 = ''.join(grid[r][c] for r, c in diag1)
        chars_diag2 = ''.join(grid[r][c] for r, c in diag2)

        # Check for valid X-MAS patterns
        for pattern1 in patterns:
            for pattern2 in patterns:
                if chars_diag1 == pattern1 and chars_diag2 == pattern2:
                    return 1
        return 0

    # Iterate over the grid to find X-MAS patterns
    for r in range(1, rows - 1):  # Avoid edges
        for c in range(1, cols - 1):  # Avoid edges
            x_mas_count += check_x_mas(r, c)

    return x_mas_count
# Example usage:
filename = "xmas.txt"  # Replace with the actual filename
# result = count_word_occurrences(filename)
# print(f"The word XMAS appears {result} times in the word search.")
result = count_x_mas_occurrences(filename)
print(f"The X-MAS pattern appears {result} times in the word search.")
