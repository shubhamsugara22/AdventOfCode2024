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


def find_accessible_positions(grid: List[List[str]]) -> List[Tuple[int,int]]:
    """
    Find all positions of accessible '@' rolls in the current grid state.
    
    Logic for Part 2:
    - Identifies which rolls can be removed in the current iteration
    - Returns list of (row, col) tuples for all accessible rolls
    - Used iteratively to simulate removing accessible rolls until none remain
    """
    rows = len(grid)
    cols = len(grid[0]) if rows else 0
    neighbors = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
    accessible = []

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != '@':
                continue
            # Count adjacent '@' rolls
            adj_at = 0
            for dr, dc in neighbors:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '@':
                    adj_at += 1
                    if adj_at >= 4:
                        break
            # If fewer than 4 neighbors, it's accessible
            if adj_at < 4:
                accessible.append((r, c))
    return accessible


def remove_iteratively(grid_lines: List[str], verbose: bool = False) -> Tuple[int, List[str]]:
    """
    Part 2: Iteratively remove all accessible rolls until none remain.
    
    Logic:
    - In each round, find all accessible rolls
    - Remove them all simultaneously (replace '@' with '.')
    - Repeat until no accessible rolls remain
    - Count total rolls removed across all rounds
    
    This simulates a forklift continuously picking up accessible rolls
    until they're all gone.
    """
    # Convert to mutable grid
    grid = [list(line.rstrip("\n")) for line in grid_lines if line.strip() != ""]
    total_removed = 0
    round_no = 0

    while True:
        accessible = find_accessible_positions(grid)
        if not accessible:
            break

        round_no += 1
        if verbose:
            print(f"Round {round_no}: removing {len(accessible)} rolls")

        # Remove them all simultaneously (replace '@' with '.')
        for (r, c) in accessible:
            grid[r][c] = '.'

        total_removed += len(accessible)

    # Convert grid back to lines if caller wants final state
    final_lines = ["".join(row) for row in grid]
    return total_removed, final_lines


# ---------- Helper to run on a file ----------
def solve_file(path: str, mark: bool = False):
    """
    Read grid from file and solve both parts.
    
    Logic:
    - Load the grid from input file
    - Part 1: Count accessible rolls using the initial state
    - Part 2: Iteratively remove rolls until none remain, count total removed
    """
    with open(path, "r") as f:
        lines = [line.rstrip("\n") for line in f]
    
    # Part 1: Initial accessible rolls
    count, marked = count_accessible_rolls(lines, mark=mark)
    print("="*50)
    print("PART 1: Initial accessible rolls")
    print("="*50)
    print("Accessible rolls:", count)
    if mark:
        print("\nMarked grid (x = accessible):\n")
        for line in marked:
            print(line)
    
    # Part 2: Iteratively remove all rolls
    print("\n" + "="*50)
    print("PART 2: Remove rolls iteratively")
    print("="*50)
    total, final_grid = remove_iteratively(lines, verbose=True)
    print("\nTotal rolls removed:", total)
    
    return count, total


# ---------- Self-test with example ----------
if __name__ == "__main__":
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

    print("EXAMPLE TEST:")
    print("="*50)
    
    # Test Part 1
    cnt, marked_grid = count_accessible_rolls(example, mark=True)
    print("Part 1 - Example accessible count (expected 13):", cnt)
    print("\nExample marked grid:")
    for line in marked_grid:
        print(line)
    
    # Test Part 2
    print("\nPart 2 - Example iterative removal:")
    total_removed, final_state = remove_iteratively(example, verbose=True)
    print("Example total removed (expected 43):", total_removed)

    # Run on the actual input file for final answers
    print("\n\n" + "="*60)
    print("ACTUAL INPUT FILE:")
    print("="*60 + "\n")
    solve_file("input_day_4", mark=False)
