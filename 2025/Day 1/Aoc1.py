import os
import sys


def count_zero_positions(filename):
    position = 50  # initial dial position
    zero_count = 0

    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            direction = line[0].upper()
            try:
                steps = int(line[1:])
            except ValueError:
                # skip malformed lines
                continue

            if direction == "L":
                position = (position - steps) % 100
            elif direction == "R":
                position = (position + steps) % 100
            else:
                # ignore lines that don't start with L/R
                continue

            if position == 0:
                zero_count += 1

    return zero_count





# Day 1 — Secret Entrance
# Part 1: count times the dial is at 0 after a rotation finishes
# Part 2: count times the dial is at 0 during any click while performing rotations
#
# Expects input file at /mnt/data/Input_day_1 (one instruction per line like "L68" or "R48").

def solve(filename):
    # initial dial position
    pos = 50

    # Part 1: count times position == 0 after a rotation completes
    part1_count = 0

    # Part 2: count times position == 0 during any click while performing rotations
    part2_count = 0

    with open(filename, "r") as f:
        for raw in f:
            line = raw.strip()
            if not line:
                continue

            direction = line[0].upper()
            try:
                steps = int(line[1:])
            except ValueError:
                # skip malformed lines
                continue

            if direction not in ("R", "L"):
                # ignore unknown directions
                continue

            # --- Part 2: count intermediate hits of 0 during this rotation ---
            # For right (increasing): position at click k is (pos + k) % 100
            # For left (decreasing): position at click k is (pos - k) % 100
            # We want number of integers k in [1..steps] such that the expression == 0.
            if direction == "R":
                # solve (pos + k) % 100 == 0 -> k ≡ (100 - pos) (mod 100)
                k0 = (100 - pos) % 100
            else:  # "L"
                # solve (pos - k) % 100 == 0 -> k ≡ pos (mod 100)
                k0 = pos % 100

            # convert k0 of 0 to 100 because k=0 is not a click; the first click that hits 0 occurs at 100 clicks when k0==0
            if k0 == 0:
                k0 = 100

            # if the first k0 occurs within the number of steps, we get 1 + floor((steps - k0)/100) total hits
            if steps >= k0:
                hits = 1 + (steps - k0) // 100
            else:
                hits = 0

            part2_count += hits

            # --- Now update the position (end of rotation) for both parts ---
            if direction == "R":
                pos = (pos + steps) % 100
            else:
                pos = (pos - steps) % 100

            # Part 1: if after this rotation the dial is at 0, count it
            if pos == 0:
                part1_count += 1

    return part1_count, part2_count


def main():
    # Default input file is `Input_day_1` in the same directory as this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    default_file = os.path.join(script_dir, "Input_day_1")

    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        input_file = default_file

    if not os.path.isfile(input_file):
        print(f"Error: input file not found: {input_file}")
        sys.exit(2)

    p1, p2 = solve(input_file)
    print("Part 1 (count ends at 0):", p1)
    print("Part 2 (count any click at 0):", p2)


if __name__ == "__main__":
    main()
