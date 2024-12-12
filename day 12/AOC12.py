from collections import deque

def parse_map(input_map):
    return [list(row) for row in input_map.splitlines()]

def get_neighbors(x, y, rows, cols):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols:
            yield nx, ny

def flood_fill(grid, x, y, visited):
    rows, cols = len(grid), len(grid[0])
    queue = deque([(x, y)])
    region_type = grid[x][y]
    region_cells = []
    visited[x][y] = True

    while queue:
        cx, cy = queue.popleft()
        region_cells.append((cx, cy))

        for nx, ny in get_neighbors(cx, cy, rows, cols):
            if not visited[nx][ny] and grid[nx][ny] == region_type:
                visited[nx][ny] = True
                queue.append((nx, ny))

    return region_cells

def calculate_perimeter(grid, region_cells):
    perimeter = 0
    rows, cols = len(grid), len(grid[0])

    for x, y in region_cells:
        for nx, ny in get_neighbors(x, y, rows, cols):
            # Increment perimeter if the neighbor is not part of the same region
            if grid[nx][ny] != grid[x][y]:
                perimeter += 1
        # Add edge contributions explicitly
        if x == 0:
            perimeter += 1
        if x == rows - 1:
            perimeter += 1
        if y == 0:
            perimeter += 1
        if y == cols - 1:
            perimeter += 1

    return perimeter


def calculate_total_price(input_map):
    grid = parse_map(input_map)
    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    total_price = 0

    for x in range(rows):
        for y in range(cols):
            if not visited[x][y]:
                region_cells = flood_fill(grid, x, y, visited)
                area = len(region_cells)
                perimeter = calculate_perimeter(grid, region_cells)
                price = area * perimeter
                total_price += price

    return total_price

# Read input from file
with open("perem.txt", "r") as file:
    input_map = file.read()

print(calculate_total_price(input_map))
