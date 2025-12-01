# AdventOfCode2024

Homepage : https://adventofcode.com/

## Table of Contents

### [Day 1](./day%201/) - Historian Hysteria
**Problem:** Calculate similarity scores between two lists by comparing element frequencies.
- Part 1: Calculate total score based on frequency matching
- Part 2: Enhanced scoring with weighted comparisons
- **Files:** `AOC1.py`

### [Day 2](./day%202/) - Red-Nosed Reports
**Problem:** Analyze sequences to determine if they are "safe" based on monotonic increase/decrease rules.
- Part 1: Check if sequences are strictly increasing or decreasing with differences in range [1,3]
- Part 2: Allow removing one element to make sequences safe (Problem Dampener)
- **Files:** `AOC2.py`, `row.txt`

### [Day 3](./day%203/) - Mull It Over
**Problem:** Parse corrupted memory to find and execute valid multiplication instructions.
- Part 1: Extract and sum results of `mul(X,Y)` instructions using regex
- Part 2: Handle conditional execution with `do()` and `don't()` instructions
- **Files:** `AOC3.py`, `scrambled.txt`

### [Day 4](./day%204/) - Ceres Search
**Problem:** Word search puzzle finding patterns in a 2D grid.
- Part 1: Count occurrences of "XMAS" in all 8 directions
- Part 2: Find X-shaped "MAS" patterns (diagonal crosses)
- **Files:** `AOC4.py`, `xmas.txt`

### [Day 5](./day%205/) - Print Queue
**Problem:** Validate and correct page ordering based on dependency rules.
- Part 1: Find correctly ordered updates and sum their middle pages
- Part 2: Correct invalid updates using topological sorting
- **Files:** `AOC5.py`, `rules.txt`

### [Day 6](./day%206/) - Guard Gallivant  ===> Pending
**Problem:** Simulate guard patrol movement on a grid with obstacles.
- Part 1: Track distinct positions visited by guard following turn-right-on-obstacle rules
- Part 2: Find positions to place obstacles that create loops
- **Files:** `AOC6.py`, `guard.txt`

### [Day 7](./day%207/) - Bridge Repair
**Problem:** Determine which equations can be made true by inserting operators.
- Part 1: Use `+` and `*` operators evaluated left-to-right
- Part 2: Add concatenation operator `||` to combine digits
- **Files:** `AOC7.py`, `pattern.txt`

### [Day 8](./day%208/) - Resonant Collinearity ===> Part 2 redo
**Problem:** Find antinode positions created by antenna frequency resonance.
- Part 1: Calculate antinode positions at specific distances from antenna pairs
- Part 2: Find all collinear antinode positions along antenna lines
- **Files:** `AOC8.py`, `mid.txt`

### [Day 9](./day%209/) - Disk Fragmenter ==> work on solutions
**Problem:** Defragment disk by moving file blocks to fill free space.
- Part 1: Move individual blocks to leftmost free space
- Part 2: Move whole files without fragmenting them
- **Files:** `AOC9.py`, `snake.txt`

### [Day 10](./day%2010/) - Hoof It
**Problem:** Find hiking trails on a topographic map from height 0 to height 9.
- Part 1: Count reachable height-9 positions from each trailhead
- Part 2: Count distinct hiking trails (paths)
- **Files:** `AOC10.py`, `AOC10-2.py`, `path.txt`

### [Day 11](./day%2011/) - Plutonian Pebbles
**Problem:** Simulate stone transformation rules over multiple blinks.
- Rules: 0→1, even-digit split, else multiply by 2024
- Optimized using Counter to track stone counts efficiently
- **Files:** `AOC11.py`

### [Day 12](./day%2012/) - Garden Groups ===? Part 2 redo
**Problem:** Calculate fencing costs for garden regions.
- Part 1: Cost = area × perimeter for each connected region
- Part 2: Cost = area × number of sides (bulk discount)
- **Files:** `AOC12.py`, `AOC12-a.py`, `perem.txt`

### [Day 13](./day%2013/) - Claw Contraption
**Problem:** Solve systems of linear equations to win prizes with minimum tokens.
- Part 1: Find button press combinations within 100 presses
- Part 2: Solve with large coordinate offsets (10^13)
- Uses linear algebra to solve efficiently
- **Files:** `AOC13.py`, `claw.txt`

### [Day 14](./day%2014/) - Restroom Redoubt
**Problem:** Simulate robot movement on a toroidal grid.
- Part 1: Calculate safety factor after 100 seconds based on quadrant distribution
- Part 2: Find when robots form a Christmas tree pattern (low variance clustering)
- **Files:** `AOC14.py`, `safety.txt`

### [Day 15](./day%2015/) - Warehouse Woes ==> 2 solution
**Problem:** Simulate robot pushing boxes in a warehouse.
- Part 1: Push single-width boxes following movement commands
- Part 2: Handle double-width boxes with complex push mechanics
- **Files:** `AOC15.py`, `lantern_fish.txt`, `moves.txt`

### [Day 16](./day%2016/) - Reindeer Maze
**Problem:** Find optimal path through maze with rotation costs.
- Part 1: Minimum cost path (movement=1, rotation=1000)
- Part 2: Count all tiles on any optimal path
- Uses Dijkstra's algorithm with state tracking
- **Files:** `AOC16.py`, `maze.txt`

### [Day 17](./day%2017/) - Chronospatial Computer
**Problem:** Simulate a 3-register computer with 8 opcodes.
- Part 1: Execute program and capture output
- Part 2: Find initial register A value that makes program output itself (quine)
- **Files:** `AOC17.py`, `three_digit.txt`

### [Day 18](./day%2018/) - RAM Run
**Problem:** Navigate through falling bytes corrupting memory space.
- Part 1: Find shortest path after first 1024 bytes fall
- Part 2: Find first byte that blocks all paths to exit
- **Files:** `AOC18.py`, `RAM.txt`

### [Day 19](./day%2019/) - Linen Layout
**Problem:** Determine which towel designs can be formed from available patterns.
- Part 1: Count how many designs are possible
- Part 2: Count total number of ways to form each design
- Uses dynamic programming with memoization
- **Files:** `AOC19.py`, `tshirt.txt`

### [Day 20](./day%2020/) - Race Condition
**Problem:** Find cheats that save time by phasing through walls.
- Part 1: 2-picosecond cheats saving ≥100 picoseconds
- Part 2: 20-picosecond cheats saving ≥100 picoseconds
- **Files:** `AOC20.py`, `cheats.txt`

### [Day 21](./day%2021/) - Keypad Conundrum ==>Redo the solutions
**Problem:** Control robots controlling robots controlling a numeric keypad.
- Calculate minimum button presses through chain of directional keypads
- Part 1: 3 robots, Part 2: 26 robots
- Uses recursive optimization with memoization
- **Files:** `AOC21.py`, `keypad.txt`

### [Day 22](./day%2022/) - Monkey Market
**Problem:** Predict pseudo-random secret numbers and optimize banana trading.
- Part 1: Sum of 2000th secret numbers for all buyers
- Part 2: Find best sequence of 4 price changes to maximize bananas
- **Files:** `AOC22.py`, `hiding.txt`

### [Day 23](./day%2023/) - LAN Party
**Problem:** Find interconnected computers in a network.
- Part 1: Count triangles (3-cliques) containing computers starting with 't'
- Part 2: Find largest clique using Bron-Kerbosch algorithm
- **Files:** `AOC23.py`, `Lan.txt`

### [Day 24](./day%2024/) - Crossed Wires ==> Part2 redo
**Problem:** Simulate and debug a binary adder circuit.
- Part 1: Evaluate logic gates to get decimal output
- Part 2: Find swapped wires in broken adder circuit
- **Files:** `AOC24.py`, `gates.txt`

### [Day 25](./day%2025/) - Code Chronicle
**Problem:** Match lock and key schematics that fit together.
- Count valid lock/key pairs where pin heights don't overlap
- Final puzzle of Advent of Code 2024!
- **Files:** `AOC25.py`, `christmas.txt`
```
TODO: Fix the code and clean up , 
      Improve O() and add description files
	  Try to add solution in go