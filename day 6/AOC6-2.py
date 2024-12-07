def parse_input_from_file(filename):
    with open(filename, 'r') as file:
        grid = [list(line.strip()) for line in file.readlines()]
    directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
    reverse_directions = {v: k for k, v in directions.items()}
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell in directions:
                return grid, (i, j), directions[cell], directions, reverse_directions
    return grid, None, None, directions, reverse_directions

def simulate_guard(grid, start, initial_dir, directions):
    rows, cols = len(grid), len(grid[0])
    pos = start
    direction = initial_dir
    visited_states = set()  # Track (position, direction)
    visited = set()
    visited.add(pos)
    
    while True:
        # Record the current state
        state = (pos, direction)
        if state in visited_states:
            return visited, True  # Loop detected
        visited_states.add(state)

        # Calculate the position in front
        next_pos = (pos[0] + direction[0], pos[1] + direction[1])
        if 0 <= next_pos[0] < rows and 0 <= next_pos[1] < cols and grid[next_pos[0]][next_pos[1]] == '#':
            # Turn right if there's an obstacle
            direction = (direction[1], -direction[0])  # Rotate right
        else:
            # Move forward
            pos = next_pos
            if not (0 <= pos[0] < rows and 0 <= pos[1] < cols):
                break  # Guard left the grid
            visited.add(pos)

    return visited, False

def find_loop_positions(grid, start, initial_dir, directions):
    rows, cols = len(grid), len(grid[0])
    loop_positions = []

    for i in range(rows):
        for j in range(cols):
            # Skip non-empty cells and the starting position
            if grid[i][j] != '.' or (i, j) == start:
                continue
            
            # Temporarily add an obstruction
            grid[i][j] = '#'
            _, is_loop = simulate_guard(grid, start, initial_dir, directions)
            if is_loop:
                loop_positions.append((i, j))
            # Remove the obstruction
            grid[i][j] = '.'

    return loop_positions

def main():
    input_file = "guard.txt"
    grid, start, initial_dir, directions, _ = parse_input_from_file(input_file)
    loop_positions = find_loop_positions(grid, start, initial_dir, directions)
    print(f"Number of valid obstruction positions: {len(loop_positions)}")
    for pos in loop_positions:
        print(f"Obstruction can be placed at: {pos}")

if __name__ == "__main__":
    main()
