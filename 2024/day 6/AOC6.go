package main

import (
	"bufio"
	"fmt"
	"os"
)

type Position struct {
	row, col int
}

type Direction struct {
	dr, dc int
}

func parseInputFromFile(filename string) ([][]rune, Position, Direction, error) {
	file, err := os.Open(filename)
	if err != nil {
		return nil, Position{}, Direction{}, err
	}
	defer file.Close()

	var grid [][]rune
	var start Position
	var initialDir Direction

	directions := map[rune]Direction{
		'^': {-1, 0},
		'>': {0, 1},
		'v': {1, 0},
		'<': {0, -1},
	}

	scanner := bufio.NewScanner(file)
	row := 0
	for scanner.Scan() {
		line := []rune(scanner.Text())
		grid = append(grid, line)
		for col, cell := range line {
			if dir, ok := directions[cell]; ok {
				start = Position{row, col}
				initialDir = dir
			}
		}
		row++
	}

	return grid, start, initialDir, nil
}

func simulateGuard(grid [][]rune, start Position, initialDir Direction) map[Position]bool {
	rows, cols := len(grid), len(grid[0])
	pos := start
	direction := initialDir
	visited := make(map[Position]bool)
	visited[pos] = true

	for {
		nextPos := Position{pos.row + direction.dr, pos.col + direction.dc}
		
		if nextPos.row >= 0 && nextPos.row < rows && nextPos.col >= 0 && nextPos.col < cols &&
			grid[nextPos.row][nextPos.col] == '#' {
			// Turn right
			direction = Direction{direction.dc, -direction.dr}
		} else {
			pos = nextPos
			if pos.row < 0 || pos.row >= rows || pos.col < 0 || pos.col >= cols {
				break
			}
			visited[pos] = true
		}
	}

	return visited
}

func main() {
	inputFile := "guard.txt"
	grid, start, initialDir, err := parseInputFromFile(inputFile)
	if err != nil {
		fmt.Printf("Error reading file: %v\n", err)
		return
	}

	visitedPositions := simulateGuard(grid, start, initialDir)
	fmt.Printf("Distinct positions visited: %d\n", len(visitedPositions))
}
