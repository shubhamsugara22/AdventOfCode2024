package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

type Pos struct {
	x, y int
}

func bfsPathExists(grid [][]rune, size int) bool {
	if grid[0][0] == '#' || grid[size-1][size-1] == '#' {
		return false
	}

	queue := []Pos{{0, 0}}
	visited := make(map[Pos]bool)
	visited[Pos{0, 0}] = true
	directions := []Pos{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}

	for len(queue) > 0 {
		curr := queue[0]
		queue = queue[1:]

		if curr.x == size-1 && curr.y == size-1 {
			return true
		}

		for _, dir := range directions {
			nx, ny := curr.x+dir.x, curr.y+dir.y
			newPos := Pos{nx, ny}
			if nx >= 0 && nx < size && ny >= 0 && ny < size &&
				grid[nx][ny] == '.' && !visited[newPos] {
				visited[newPos] = true
				queue = append(queue, newPos)
			}
		}
	}
	return false
}

func main() {
	file, err := os.Open("RAM.txt")
	if err != nil {
		fmt.Printf("Error: %v\n", err)
		return
	}
	defer file.Close()

	var bytePositions []Pos
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		parts := strings.Split(scanner.Text(), ",")
		if len(parts) == 2 {
			x, _ := strconv.Atoi(parts[0])
			y, _ := strconv.Atoi(parts[1])
			bytePositions = append(bytePositions, Pos{x, y})
		}
	}

	gridSize := 71
	grid := make([][]rune, gridSize)
	for i := range grid {
		grid[i] = make([]rune, gridSize)
		for j := range grid[i] {
			grid[i][j] = '.'
		}
	}

	for i, pos := range bytePositions {
		if pos.x >= 0 && pos.x < gridSize && pos.y >= 0 && pos.y < gridSize {
			grid[pos.y][pos.x] = '#'
			if !bfsPathExists(grid, gridSize) {
				fmt.Printf("First blocking byte: %d,%d\n", pos.x, pos.y)
				return
			}
		}
		if i >= 1024 {
			break
		}
	}
}
