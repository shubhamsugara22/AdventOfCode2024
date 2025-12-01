package main

import (
	"bufio"
	"fmt"
	"os"
)

type Position struct {
	r, c int
}

func parseMap(filePath string) ([][]int, error) {
	file, err := os.Open(filePath)
	if err != nil {
		return nil, err
	}
	defer file.Close()

	var grid [][]int
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		var row []int
		for _, ch := range line {
			row = append(row, int(ch-'0'))
		}
		grid = append(grid, row)
	}

	return grid, nil
}

func findTrailheads(grid [][]int) []Position {
	var trailheads []Position
	for r := 0; r < len(grid); r++ {
		for c := 0; c < len(grid[0]); c++ {
			if grid[r][c] == 0 {
				trailheads = append(trailheads, Position{r, c})
			}
		}
	}
	return trailheads
}

func countReachableNines(grid [][]int, start Position) int {
	rows, cols := len(grid), len(grid[0])
	visited := make(map[Position]bool)
	reachableNines := make(map[Position]bool)
	
	stack := []Position{start}
	visited[start] = true
	
	directions := []Position{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}
	
	for len(stack) > 0 {
		pos := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		
		for _, dir := range directions {
			nr, nc := pos.r+dir.r, pos.c+dir.c
			newPos := Position{nr, nc}
			
			if nr >= 0 && nr < rows && nc >= 0 && nc < cols && !visited[newPos] {
				if grid[nr][nc] == grid[pos.r][pos.c]+1 {
					visited[newPos] = true
					stack = append(stack, newPos)
					if grid[nr][nc] == 9 {
						reachableNines[newPos] = true
					}
				}
			}
		}
	}
	
	return len(reachableNines)
}

func calculateScores(grid [][]int) int {
	trailheads := findTrailheads(grid)
	totalScore := 0
	
	for _, trailhead := range trailheads {
		totalScore += countReachableNines(grid, trailhead)
	}
	
	return totalScore
}

func main() {
	filePath := "path.txt"
	grid, err := parseMap(filePath)
	if err != nil {
		fmt.Printf("Error reading file: %v\n", err)
		return
	}

	result := calculateScores(grid)
	fmt.Printf("Total score of all trailheads: %d\n", result)
}
