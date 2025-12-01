# def simulate_robots_from_file(filename, t, width=101, height=103):
#     # Read input from a file
#     with open(filename, 'r') as file:
#         input_data = file.read().strip()
    
#     # Parse input
#     robots = []
#     for line in input_data.splitlines():
#         pos, vel = line.split(" ")
#         px, py = map(int, pos[2:].split(","))
#         vx, vy = map(int, vel[2:].split(","))
#         robots.append(((px, py), (vx, vy)))
    
#     # Simulate motion after t seconds
#     final_positions = []
#     for (px, py), (vx, vy) in robots:
#         new_x = (px + t * vx) % width
#         new_y = (py + t * vy) % height
#         final_positions.append((new_x, new_y))
    
#     # Count robots in each quadrant
#     quadrants = [0, 0, 0, 0]
#     for x, y in final_positions:
#         if x == 50 or y == 51:
#             continue  # Ignore robots on the middle lines
#         if x <= 50 and y <= 51:
#             quadrants[0] += 1  # Top-left
#         elif x > 50 and y <= 51:
#             quadrants[1] += 1  # Top-right
#         elif x <= 50 and y > 51:
#             quadrants[2] += 1  # Bottom-left
#         elif x > 50 and y > 51:
#             quadrants[3] += 1  # Bottom-right
    
#     # Calculate safety factor
#     safety_factor = quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3]
#     return safety_factor

# # Example usage
# if __name__ == "__main__":
#     # Input file containing the robot data
#     input_file = "safety.txt"  
#     t = 100  # Time to simulate
#     result = simulate_robots_from_file(input_file, t)
#     print("Safety Factor after", t, "seconds:", result)
    
##############################
import re
from dataclasses import dataclass

import numpy as np


@dataclass
class Robot:
    col: int
    row: int
    vcol: int
    vrow: int


def load_robots(filename):
    pattern = re.compile(r"-?\d+")
    with open(filename, "rt") as fin:
        nums = [int(m.group()) for m in re.finditer(pattern, fin.read())]
    return [Robot(*nums[i : i + 4]) for i in range(0, len(nums), 4)]


def move(robos, seconds, area_rows, area_cols):
    for r in robos:
        r.row = (r.row + r.vrow * seconds) % area_rows
        r.col = (r.col + r.vcol * seconds) % area_cols


def find_tree_second(robos, current_seconds, area_rows, area_cols):
    row_var_thres = np.var([r.row for r in robos]) * 0.5
    col_var_thres = np.var([r.col for r in robos]) * 0.5
    row_low_var, col_low_var = 0, 0

    # look for first second when variance is low (indicates clustered robots)
    while row_low_var == 0 or col_low_var == 0:
        current_seconds += 1
        move(robos, 1, area_rows, area_cols)
        if row_low_var == 0 and np.var([r.row for r in robos]) < row_var_thres:
            row_low_var = current_seconds % area_rows
        if col_low_var == 0 and np.var([r.col for r in robos]) < col_var_thres:
            col_low_var = current_seconds % area_cols

    # low row variance occurs every area_rows seconds
    # low col variance occurs every area_cols seconds
    # find second when both are low together, i.e. find x and y in this equation:
    # row_low_var + area_rows*x = col_low_var + area_cols*y

    # brute force solution
    x, y = 1, 1
    while True:
        left_side = row_low_var + area_rows * x
        right_side = col_low_var + area_cols * y
        if left_side == right_side:
            return left_side
        if left_side < right_side:
            x += 1
        else:
            y += 1


def safety_factor(robos, area_rows, area_cols):
    mid_row, mid_col = area_rows // 2, area_cols // 2
    quadrants = {(True, True): 0, (True, False): 0, (False, True): 0, (False, False): 0}

    for r in robos:
        if r.row == mid_row or r.col == mid_col:
            continue
        quadrants[r.row < mid_row, r.col < mid_col] += 1

    return (
        quadrants[True, True]
        * quadrants[True, False]
        * quadrants[False, True]
        * quadrants[False, False]
    )


def main():
    robos = load_robots("safety.txt")
    area_rows, area_cols = 103, 101

    move(robos, 100, area_rows, area_cols)
    print(f"Part 1: {safety_factor(robos, area_rows, area_cols)}")
    print(f"Part 2: {find_tree_second(robos, 100, area_rows, area_cols)}")


if __name__ == "__main__":
    main()
