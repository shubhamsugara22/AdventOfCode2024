# from collections import deque

# def parse_input(input_data):
#     """Parses the input into a list of tuples representing byte positions."""
#     return [tuple(map(int, line.split(','))) for line in input_data.strip().splitlines()]

# def simulate_bytes(grid_size, byte_positions, max_bytes):
#     """Simulates the bytes falling and returns the corrupted grid."""
#     grid = [["." for _ in range(grid_size)] for _ in range(grid_size)]
    
#     for i, (x, y) in enumerate(byte_positions):
#         if i >= max_bytes:
#             break
#         # Skip coordinates that are out of bounds
#         if 0 <= x < grid_size and 0 <= y < grid_size:
#             grid[y][x] = "#"
    
#     return grid

# def bfs_shortest_path(grid):
#     """Finds the shortest path from (0, 0) to (n-1, n-1) using BFS."""
#     n = len(grid)
#     directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
#     queue = deque([(0, 0, 0)])  # (x, y, steps)
#     visited = set()
#     visited.add((0, 0))

#     while queue:
#         x, y, steps = queue.popleft()

#         # Check if we reached the bottom-right corner
#         if (x, y) == (n - 1, n - 1):
#             return steps

#         # Explore neighbors
#         for dx, dy in directions:
#             nx, ny = x + dx, y + dy

#             if 0 <= nx < n and 0 <= ny < n and grid[ny][nx] == "." and (nx, ny) not in visited:
#                 visited.add((nx, ny))
#                 queue.append((nx, ny, steps + 1))

#     return -1  # No path found

# def main(input_file, grid_size=70, max_bytes=1024):
#     with open(input_file, 'r') as f:
#         input_data = f.read()
    
#     byte_positions = parse_input(input_data)
#     grid = simulate_bytes(grid_size, byte_positions, max_bytes)
#     return bfs_shortest_path(grid)

# # Example usage
# input_file = "RAM.txt"
# result = main(input_file, grid_size=71, max_bytes=1024)
# print("Shortest path length:", result)


####################################################################
from collections import deque

def simulate_bytes_until_block(grid_size, byte_positions):
    """Simulates bytes falling and identifies the first byte that blocks the path."""
    grid = [["." for _ in range(grid_size)] for _ in range(grid_size)]

    def bfs_path_exists():
        """Checks if a path exists from (0, 0) to (grid_size-1, grid_size-1)."""
        n = len(grid)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        queue = deque([(0, 0)])
        visited = set([(0, 0)])

        if grid[0][0] == "#" or grid[n-1][n-1] == "#":
            return False  # Start or end is blocked

        while queue:
            x, y = queue.popleft()
            if (x, y) == (n - 1, n - 1):
                return True  # Exit is reachable

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and grid[ny][nx] == "." and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny))

        return False  # No path found

    # Simulate bytes falling
    for i, (x, y) in enumerate(byte_positions):
        if 0 <= x < grid_size and 0 <= y < grid_size:
            grid[y][x] = "#"
            if not bfs_path_exists():
                return f"{x},{y}"  # Return the first blocking byte's coordinates

    return "No blocking byte found"  # All bytes added without blocking the path

# Main function
def main(input_file, grid_size):
    with open(input_file, "r") as f:
        byte_positions = parse_input(f.read())
    blocking_byte = simulate_bytes_until_block(grid_size, byte_positions)
    print(f"First blocking byte: {blocking_byte}")

def parse_input(input_data):
    """Parses the input into a list of tuples representing byte positions."""
    return [tuple(map(int, line.split(','))) for line in input_data.strip().splitlines()]

# Example usage
if __name__ == "__main__":
    input_file = "RAM.txt"  # Replace with your input file
    main(input_file, grid_size=71)
