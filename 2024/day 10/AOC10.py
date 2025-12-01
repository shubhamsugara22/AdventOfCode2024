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

def count_reachable_nines(grid, start):
    """Counts the number of unique 9s reachable from the start position."""
    rows, cols = len(grid), len(grid[0])
    visited = set()
    reachable_nines = set()
    
    stack = [start]
    visited.add(start)
    
    while stack:
        r, c = stack.pop()
        
        # Check neighbors for valid moves
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                if grid[nr][nc] == grid[r][c] + 1:
                    visited.add((nr, nc))
                    stack.append((nr, nc))
                    if grid[nr][nc] == 9:
                        reachable_nines.add((nr, nc))
    
    return len(reachable_nines)

def calculate_scores(grid):
    """Calculates the total score of all trailheads."""
    trailheads = find_trailheads(grid)
    total_score = 0
    
    for trailhead in trailheads:
        total_score += count_reachable_nines(grid, trailhead)
    
    return total_score

# Main Execution
if __name__ == "__main__":
    
    file_path = "path.txt"
    
    # Parse the map and calculate the total score
    grid = parse_map(file_path)
    result = calculate_scores(grid)
    print(f"Total score of all trailheads: {result}")
