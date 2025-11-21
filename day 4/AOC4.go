package main

import (
	"bufio"
	"fmt"
	"os"
)

func countXMasOccurrences(filename string) int {
	file, err := os.Open(filename)
	if err != nil {
		fmt.Printf("Error opening file: %v\n", err)
		return 0
	}
	defer file.Close()

	var grid []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		if line != "" {
			grid = append(grid, line)
		}
	}

	rows := len(grid)
	if rows == 0 {
		return 0
	}
	cols := len(grid[0])
	patterns := []string{"MAS", "SAM"}
	xMasCount := 0

	isValid := func(r, c int) bool {
		return r >= 0 && r < rows && c >= 0 && c < cols
	}

	checkXMas := func(centerR, centerC int) int {
		// Coordinates for the diagonals
		diag1 := [][2]int{{centerR - 1, centerC - 1}, {centerR, centerC}, {centerR + 1, centerC + 1}}
		diag2 := [][2]int{{centerR - 1, centerC + 1}, {centerR, centerC}, {centerR + 1, centerC - 1}}

		// Check if all positions are valid
		for _, pos := range append(diag1, diag2...) {
			if !isValid(pos[0], pos[1]) {
				return 0
			}
		}

		// Extract characters for both diagonals
		charsDiag1 := ""
		for _, pos := range diag1 {
			charsDiag1 += string(grid[pos[0]][pos[1]])
		}
		charsDiag2 := ""
		for _, pos := range diag2 {
			charsDiag2 += string(grid[pos[0]][pos[1]])
		}

		// Check for valid X-MAS patterns
		for _, pattern1 := range patterns {
			for _, pattern2 := range patterns {
				if charsDiag1 == pattern1 && charsDiag2 == pattern2 {
					return 1
				}
			}
		}
		return 0
	}

	// Iterate over the grid to find X-MAS patterns (avoid edges)
	for r := 1; r < rows-1; r++ {
		for c := 1; c < cols-1; c++ {
			xMasCount += checkXMas(r, c)
		}
	}

	return xMasCount
}

func main() {
	filename := "xmas.txt"
	result := countXMasOccurrences(filename)
	fmt.Printf("The X-MAS pattern appears %d times in the word search.\n", result)
}
