package main

import (
	"bufio"
	"fmt"
	"os"
)

type Coord struct {
	x, y int
}

func getAntinodes(coord1, coord2 Coord, shapeX, shapeY int) map[Coord]bool {
	x1, y1 := coord1.x, coord1.y
	x2, y2 := coord2.x, coord2.y
	dx, dy := x2-x1, y2-y1
	
	output := make(map[Coord]bool)
	
	// Forward direction
	xa, ya := x1, y1
	for xa >= 0 && xa < shapeX && ya >= 0 && ya < shapeY {
		output[Coord{xa, ya}] = true
		xa, ya = xa+dx, ya+dy
	}
	
	// Backward direction
	xa, ya = x1, y1
	for xa >= 0 && xa < shapeX && ya >= 0 && ya < shapeY {
		output[Coord{xa, ya}] = true
		xa, ya = xa-dx, ya-dy
	}
	
	return output
}

func main() {
	file, err := os.Open("mid.txt")
	if err != nil {
		fmt.Printf("Error opening file: %v\n", err)
		return
	}
	defer file.Close()

	var grid [][]rune
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		grid = append(grid, []rune(scanner.Text()))
	}

	shapeX, shapeY := len(grid), len(grid[0])
	
	// Find all frequencies
	frequencies := make(map[rune]bool)
	for _, line := range grid {
		for _, char := range line {
			if char != '.' {
				frequencies[char] = true
			}
		}
	}

	// Get coordinates for each frequency
	freqCoords := make(map[rune][]Coord)
	for freq := range frequencies {
		for i, line := range grid {
			for j, char := range line {
				if char == freq {
					freqCoords[freq] = append(freqCoords[freq], Coord{i, j})
				}
			}
		}
	}

	// Find all antinodes
	allAntinodes := make(map[Coord]bool)
	for _, coords := range freqCoords {
		for i := 0; i < len(coords); i++ {
			for j := i + 1; j < len(coords); j++ {
				antinodes := getAntinodes(coords[i], coords[j], shapeX, shapeY)
				for antinode := range antinodes {
					allAntinodes[antinode] = true
				}
			}
		}
	}

	fmt.Println(len(allAntinodes))
}
