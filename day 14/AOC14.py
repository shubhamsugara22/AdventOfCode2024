def simulate_robots_from_file(filename, t, width=101, height=103):
    # Read input from a file
    with open(filename, 'r') as file:
        input_data = file.read().strip()
    
    # Parse input
    robots = []
    for line in input_data.splitlines():
        pos, vel = line.split(" ")
        px, py = map(int, pos[2:].split(","))
        vx, vy = map(int, vel[2:].split(","))
        robots.append(((px, py), (vx, vy)))
    
    # Simulate motion after t seconds
    final_positions = []
    for (px, py), (vx, vy) in robots:
        new_x = (px + t * vx) % width
        new_y = (py + t * vy) % height
        final_positions.append((new_x, new_y))
    
    # Count robots in each quadrant
    quadrants = [0, 0, 0, 0]
    for x, y in final_positions:
        if x == 50 or y == 51:
            continue  # Ignore robots on the middle lines
        if x <= 50 and y <= 51:
            quadrants[0] += 1  # Top-left
        elif x > 50 and y <= 51:
            quadrants[1] += 1  # Top-right
        elif x <= 50 and y > 51:
            quadrants[2] += 1  # Bottom-left
        elif x > 50 and y > 51:
            quadrants[3] += 1  # Bottom-right
    
    # Calculate safety factor
    safety_factor = quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3]
    return safety_factor

# Example usage
if __name__ == "__main__":
    # Input file containing the robot data
    input_file = "safety.txt"  
    t = 100  # Time to simulate
    result = simulate_robots_from_file(input_file, t)
    print("Safety Factor after", t, "seconds:", result)
    
##############################
def parse_input(filename):
    """Parse the input file containing robots' positions and velocities."""
    with open(filename, 'r') as file:
        input_data = file.read().strip()
    
    robots = []
    for line in input_data.splitlines():
        pos, vel = line.split(" ")
        px, py = map(int, pos[2:].split(","))
        vx, vy = map(int, vel[2:].split(","))
        robots.append(((px, py), (vx, vy)))
    return robots


def simulate_robots(robots, t, width=101, height=103):
    """Simulate the robots after `t` seconds."""
    final_positions = []
    for (px, py), (vx, vy) in robots:
        new_x = (px + t * vx) % width
        new_y = (py + t * vy) % height
        final_positions.append((new_x, new_y))
    return final_positions


def calculate_safety_factor(positions, width=101, height=103):
    """Calculate the safety factor based on robot positions."""
    quadrants = [0, 0, 0, 0]
    for x, y in positions:
        if x == width // 2 or y == height // 2:
            continue  # Ignore robots on the middle lines
        if x <= width // 2 and y <= height // 2:
            quadrants[0] += 1  # Top-left
        elif x > width // 2 and y <= height // 2:
            quadrants[1] += 1  # Top-right
        elif x <= width // 2 and y > height // 2:
            quadrants[2] += 1  # Bottom-left
        elif x > width // 2 and y > height // 2:
            quadrants[3] += 1  # Bottom-right
    return quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3]


def find_easter_egg(robots):
    """Find the fewest seconds for robots to display an Easter egg."""
    t = 0
    min_area = float('inf')
    best_positions = None
    
    while True:
        positions = [(px + t * vx, py + t * vy) for (px, py), (vx, vy) in robots]
        xs, ys = zip(*positions)
        min_x, max_x = min(xs), max(xs)
        min_y, max_y = min(ys), max(ys)
        area = (max_x - min_x + 1) * (max_y - min_y + 1)

        # Check if current area is smallest so far
        if area < min_area:
            min_area = area
            best_positions = positions
        else:
            # If area starts increasing, the previous t was the best time
            return t - 1, best_positions
        
        t += 1


def print_positions(positions):
    """Print the positions of robots as a grid."""
    xs, ys = zip(*positions)
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)
    
    grid = [['.' for _ in range(min_x, max_x + 1)] for _ in range(min_y, max_y + 1)]
    for x, y in positions:
        grid[y - min_y][x - min_x] = '#'
    
    for row in grid:
        print("".join(row))


if __name__ == "__main__":
    # Input file containing the robot data
    input_file = "robots_input.txt"  # Replace with your actual input file name

    # Parse input
    robots = parse_input(input_file)

    # Part 1: Safety factor after 100 seconds
    t = 100
    final_positions = simulate_robots(robots, t)
    safety_factor = calculate_safety_factor(final_positions)
    print("Safety Factor after", t, "seconds:", safety_factor)

    # Part 2: Find fewest seconds for the Easter egg pattern
    seconds, easter_egg_positions = find_easter_egg(robots)
    print("\nFewest seconds for Easter egg:", seconds)
    print("\nEaster egg pattern:")
    print_positions(easter_egg_positions)

