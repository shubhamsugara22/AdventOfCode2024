import heapq

def parse_maze_from_file(file_path):
    """
    Parse the maze from a file, locating the start (S) and end (E) positions.
    """
    with open(file_path, 'r') as f:
        maze = [list(line.strip()) for line in f.readlines()]
    
    start, end = None, None
    for y, row in enumerate(maze):
        for x, char in enumerate(row):
            if char == 'S':
                start = (x, y)
            elif char == 'E':
                end = (x, y)
    return maze, start, end

def reindeer_maze(file_path):
    """
    Solve the reindeer maze problem from the input file.
    """
    maze, start, end = parse_maze_from_file(file_path)
    directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]  # East, North, West, South
    start_state = (start[0], start[1], 0)  # (x, y, direction_index)
    
    # Priority queue and visited states
    pq = [(0, start_state)]  # (cost, (x, y, dir))
    visited = {}
    
    while pq:
        cost, (x, y, d) = heapq.heappop(pq)
        
        # If we've reached the end, return the cost
        if (x, y) == end:
            return cost
        
        # Skip if we've visited this state with a lower cost
        if (x, y, d) in visited and visited[(x, y, d)] <= cost:
            continue
        visited[(x, y, d)] = cost
        
        # Move forward
        dx, dy = directions[d]
        nx, ny = x + dx, y + dy
        if 0 <= ny < len(maze) and 0 <= nx < len(maze[0]) and maze[ny][nx] != '#':  # Not a wall
            heapq.heappush(pq, (cost + 1, (nx, ny, d)))
        
        # Rotate clockwise
        new_dir = (d + 1) % 4
        heapq.heappush(pq, (cost + 1000, (x, y, new_dir)))
        
        # Rotate counterclockwise
        new_dir = (d - 1) % 4
        heapq.heappush(pq, (cost + 1000, (x, y, new_dir)))

# Example Usage
file_path = "maze.txt"
result = reindeer_maze(file_path)
print(f"The lowest score is: {result}")
