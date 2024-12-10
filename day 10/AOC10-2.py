def parse_map(file_path):
    """Parses the input map from a text file into a 2D grid of integers."""
    with open(file_path, "r") as f:
        return [list(map(int, line.strip())) for line in f.readlines()]

def find_trailheads(grid):
    """Finds all positions with height 0."""
    trailheads = []
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 0:
                trailheads.append((r, c))
    return trailheads

def count_distinct_trails(grid, start):
    """Counts the number of distinct hiking trails starting from the given trailhead."""
    rows, cols = len(grid), len(grid[0])
    trail_count = 0

    # DFS with path tracking
    def dfs(r, c, current_path):
        nonlocal trail_count

        # If we've reached a 9, count this as a valid trail
        if grid[r][c] == 9:
            trail_count += 1
            return

        # Check neighbors for valid moves
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if (nr, nc) not in current_path and grid[nr][nc] == grid[r][c] + 1:
                    dfs(nr, nc, current_path | {(nr, nc)})

    # Start DFS from the trailhead
    dfs(start[0], start[1], {start})
    return trail_count

def calculate_ratings(grid):
    """Calculates the total rating of all trailheads."""
    trailheads = find_trailheads(grid)
    total_rating = 0

    for trailhead in trailheads:
        total_rating += count_distinct_trails(grid, trailhead)
    
    return total_rating

# Main Execution
if __name__ == "__main__":
    
    file_path = "path.txt"
    
    # Parse the map and calculate the total rating
    grid = parse_map(file_path)
    result = calculate_ratings(grid)
    print(f"Total rating of all trailheads: {result}")
