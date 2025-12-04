from typing import List, Tuple

def count_accessible_rolls(grid_lines: List[str], mark: bool = False) -> Tuple[int, List[str]]:
    """
    Count accessible '@' rolls in the grid.
    
    Logic:
    - A roll ('@') is "accessible" by a forklift if it has FEWER than 4 adjacent '@' rolls
    - We check all 8 neighbors (up, down, left, right, and 4 diagonals)
    - If a roll has 4 or more '@' neighbors, it's surrounded and inaccessible
    
    If mark==True, also return a new grid (list of strings) where accessible rolls are marked 'x'.
    """
    # Normalize grid as list of lists for mutability, removing empty lines
    grid = [list(line.rstrip("\n")) for line in grid_lines if line.strip() != ""]
    if not grid:
        return 0, []

    rows = len(grid)
    cols = len(grid[0])

    # Direction offsets for 8 neighbors: up-left, up, up-right, left, right, down-left, down, down-right
    neighbors = [(-1,-1), (-1,0), (-1,1),
                 (0,-1),          (0,1),
                 (1,-1),  (1,0),  (1,1)]

    accessible_count = 0

    # We'll build a marked grid copy if requested
    marked = [row[:] for row in grid] if mark else None

    # Iterate through every cell in the grid
    for r in range(rows):
        for c in range(cols):
            # Only process '@' rolls
            if grid[r][c] != '@':
                continue

            # Count how many adjacent cells also contain '@'
            adj_at = 0
            for dr, dc in neighbors:
                nr, nc = r + dr, c + dc
                # Check if neighbor is within bounds and contains '@'
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '@':
                    adj_at += 1
                    # Early exit optimization: if already 4+ neighbors, it's not accessible
                    if adj_at >= 4:
                        break

            # A roll is accessible if it has FEWER than 4 adjacent '@' rolls
            # This means the forklift can reach it without all sides being blocked
            if adj_at < 4:
                accessible_count += 1
                if mark:
                    marked[r][c] = 'x'  # Mark accessible rolls with 'x'

    # Convert marked grid back to strings for output
    if mark:
        marked_lines = ["".join(row) for row in marked]
    else:
        marked_lines = []

    return accessible_count, marked_lines


# ---------- Helper to run on a file ----------
def solve_file(path: str, mark: bool = False):
    """
    Read grid from file and solve the problem.
    
    Logic:
    - Load the grid from input file
    - Count accessible rolls using the main algorithm
    - Optionally display the marked grid showing which rolls are accessible
    """
    with open(path, "r") as f:
        lines = [line.rstrip("\n") for line in f]
    count, marked = count_accessible_rolls(lines, mark=mark)
    print("Accessible rolls:", count)
    if mark:
        print("\nMarked grid (x = accessible):\n")
        for line in marked:
            print(line)
    return count


# ---------- Self-test using the example from prompt ----------
if __name__ == "__main__":
    # Test with a small example grid
    example = [
        "..@@.@@@@.",
        "@@@.@.@.@@",
        "@@@@@.@.@@",
        "@.@@@@..@.",
        "@@.@@@@.@@",
        ".@@@@@@@.@",
        ".@.@.@.@@@",
        "@.@@@.@@@@",
        ".@@@@@@@@.",
        "@.@.@@@.@."
    ]

    # Test the algorithm on the example
    cnt, marked_grid = count_accessible_rolls(example, mark=True)
    print("Example accessible count (expected 13):", cnt)
    print("\nExample marked grid:")
    for line in marked_grid:
        print(line)

    # Run on the actual input file for the final answer
    print("\n" + "="*50)
    print("Running on actual input file:")
    print("="*50 + "\n")
    solve_file("input_day_4", mark=True)
