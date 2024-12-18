from collections import deque

def parse_input(input_data):
    """Parses the input into a list of tuples representing byte positions."""
    return [tuple(map(int, line.split(','))) for line in input_data.strip().splitlines()]

def simulate_bytes(grid_size, byte_positions, max_bytes):
    """Simulates the bytes falling and returns the corrupted grid."""
    grid = [["." for _ in range(grid_size)] for _ in range(grid_size)]
    
    for i, (x, y) in enumerate(byte_positions):
        if i >= max_bytes:
            break
        # Skip coordinates that are out of bounds
        if 0 <= x < grid_size and 0 <= y < grid_size:
            grid[y][x] = "#"
    
    return grid

def bfs_shortest_path(grid):
    """Finds the shortest path from (0, 0) to (n-1, n-1) using BFS."""
    n = len(grid)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    queue = deque([(0, 0, 0)])  # (x, y, steps)
    visited = set()
    visited.add((0, 0))

    while queue:
        x, y, steps = queue.popleft()

        # Check if we reached the bottom-right corner
        if (x, y) == (n - 1, n - 1):
            return steps

        # Explore neighbors
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < n and grid[ny][nx] == "." and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny, steps + 1))

    return -1  # No path found

def main(input_file, grid_size=70, max_bytes=1024):
    with open(input_file, 'r') as f:
        input_data = f.read()
    
    byte_positions = parse_input(input_data)
    grid = simulate_bytes(grid_size, byte_positions, max_bytes)
    return bfs_shortest_path(grid)

# Example usage
input_file = "RAM.txt"
result = main(input_file, grid_size=71, max_bytes=1024)
print("Shortest path length:", result)
