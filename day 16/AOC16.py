# import heapq

# def parse_maze_from_file(file_path):
#     """
#     Parse the maze from a file, locating the start (S) and end (E) positions.
#     """
#     with open(file_path, 'r') as f:
#         maze = [list(line.strip()) for line in f.readlines()]
    
#     start, end = None, None
#     for y, row in enumerate(maze):
#         for x, char in enumerate(row):
#             if char == 'S':
#                 start = (x, y)
#             elif char == 'E':
#                 end = (x, y)
#     return maze, start, end

# def reindeer_maze(file_path):
#     """
#     Solve the reindeer maze problem from the input file.
#     """
#     maze, start, end = parse_maze_from_file(file_path)
#     directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]  # East, North, West, South
#     start_state = (start[0], start[1], 0)  # (x, y, direction_index)
    
#     # Priority queue and visited states
#     pq = [(0, start_state)]  # (cost, (x, y, dir))
#     visited = {}
    
#     while pq:
#         cost, (x, y, d) = heapq.heappop(pq)
        
#         # If we've reached the end, return the cost
#         if (x, y) == end:
#             return cost
        
#         # Skip if we've visited this state with a lower cost
#         if (x, y, d) in visited and visited[(x, y, d)] <= cost:
#             continue
#         visited[(x, y, d)] = cost
        
#         # Move forward
#         dx, dy = directions[d]
#         nx, ny = x + dx, y + dy
#         if 0 <= ny < len(maze) and 0 <= nx < len(maze[0]) and maze[ny][nx] != '#':  # Not a wall
#             heapq.heappush(pq, (cost + 1, (nx, ny, d)))
        
#         # Rotate clockwise
#         new_dir = (d + 1) % 4
#         heapq.heappush(pq, (cost + 1000, (x, y, new_dir)))
        
#         # Rotate counterclockwise
#         new_dir = (d - 1) % 4
#         heapq.heappush(pq, (cost + 1000, (x, y, new_dir)))

# # Example Usage
# file_path = "maze.txt"
# result = reindeer_maze(file_path)
# print(f"The lowest score is: {result}")


##################################################################

import heapq
from collections import deque

def parse_grid(grid):
    """Find the start and end points in the grid."""
    rows = len(grid)
    cols = len(grid[0])
    start, end = None, None
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 'S':
                start = (i, j)
            elif grid[i][j] == 'E':
                end = (i, j)
    return start, end, rows, cols


def dijkstra(grid, start, end, rows, cols):
    """Run Dijkstra's algorithm to find minimum costs and visited states."""
    # Directions: N=0, E=1, S=2, W=3
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    start_state = (start[0], start[1], 1)  # Start facing East

    # Priority queue and visited dictionary
    pq = []
    heapq.heappush(pq, (0, start_state))
    visited = {start_state: 0}

    while pq:
        cost, (x, y, d) = heapq.heappop(pq)

        # Skip if we've already processed a better cost for this state
        if visited.get((x, y, d), float('inf')) < cost:
            continue

        # Move forward
        dx, dy = directions[d]
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] != '#':
            new_cost = cost + 1
            if new_cost < visited.get((nx, ny, d), float('inf')):
                visited[(nx, ny, d)] = new_cost
                heapq.heappush(pq, (new_cost, (nx, ny, d)))

        # Turn left or right
        for nd in [(d - 1) % 4, (d + 1) % 4]:
            new_cost = cost + 1000
            if new_cost < visited.get((x, y, nd), float('inf')):
                visited[(x, y, nd)] = new_cost
                heapq.heappush(pq, (new_cost, (x, y, nd)))

    return visited


def backtrack_shortest_paths(grid, visited, end, rows, cols):
    """Backtrack from the end to find all states on the shortest path."""
    # Directions: N=0, E=1, S=2, W=3
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    min_end_cost = min(visited[(end[0], end[1], d)] for d in range(4) if (end[0], end[1], d) in visited)

    # Backward search
    on_shortest_path = set()
    q = deque()
    for d in range(4):
        ed_state = (end[0], end[1], d)
        if ed_state in visited and visited[ed_state] == min_end_cost:
            on_shortest_path.add(ed_state)
            q.append(ed_state)

    while q:
        cx, cy, cd = q.popleft()
        current_cost = visited[(cx, cy, cd)]

        # Backward for forward moves
        dx, dy = directions[cd]
        px, py = cx - dx, cy - dy
        if 0 <= px < rows and 0 <= py < cols and grid[px][py] != '#':
            prev_cost = current_cost - 1
            if prev_cost >= 0:
                prev_state = (px, py, cd)
                if prev_state in visited and visited[prev_state] == prev_cost:
                    if prev_state not in on_shortest_path:
                        on_shortest_path.add(prev_state)
                        q.append(prev_state)

        # Backward for turns
        turn_cost = current_cost - 1000
        if turn_cost >= 0:
            for pd in [(cd - 1) % 4, (cd + 1) % 4]:
                prev_state = (cx, cy, pd)
                if prev_state in visited and visited[prev_state] == turn_cost:
                    if prev_state not in on_shortest_path:
                        on_shortest_path.add(prev_state)
                        q.append(prev_state)

    # Return unique tiles (x, y) on the shortest path
    return {(x, y) for (x, y, d) in on_shortest_path}


def solve_maze(grid):
    start, end, rows, cols = parse_grid(grid)
    visited = dijkstra(grid, start, end, rows, cols)
    print("part1, ", min(visited[(end[0], end[1], d)] for d in range(4) if (end[0], end[1], d) in visited))
    shortest_path_tiles = backtrack_shortest_paths(grid, visited, end, rows, cols)
    print("part2, ", len(shortest_path_tiles))


if __name__ == "__main__":
    with open("maze+.txt", "r") as f:
        grid = [list(line.rstrip('\n')) for line in f]
    solve_maze(grid)
