package main

import (
	"fmt"
	"os"
	"strings"
)

type Pos struct {
	x, y int
}

func parseMap(inputMap string) [][]rune {
	lines := strings.Split(strings.TrimSpace(inputMap), "\n")
	grid := make([][]rune, len(lines))
	for i, line := range lines {
		grid[i] = []rune(line)
	}
	return grid
}

func getNeighbors(x, y, rows, cols int) []Pos {
	directions := []Pos{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}
	var neighbors []Pos
	for _, dir := range directions {
		nx, ny := x+dir.x, y+dir.y
		if nx >= 0 && nx < rows && ny >= 0 && ny < cols {
			neighbors = append(neighbors, Pos{nx, ny})
		}
	}
	return neighbors
}

func floodFill(grid [][]rune, x, y int, visited [][]bool) []Pos {
	rows, cols := len(grid), len(grid[0])
	queue := []Pos{{x, y}}
	regionType := grid[x][y]
	var regionCells []Pos
	visited[x][y] = true

	for len(queue) > 0 {
		curr := queue[0]
		queue = queue[1:]
		regionCells = append(regionCells, curr)

		for _, neighbor := range getNeighbors(curr.x, curr.y, rows, cols) {
			if !visited[neighbor.x][neighbor.y] && grid[neighbor.x][neighbor.y] == regionType {
				visited[neighbor.x][neighbor.y] = true
				queue = append(queue, neighbor)
			}
		}
	}

	return regionCells
}

func calculatePerimeter(grid [][]rune, regionCells []Pos) int {
	rows, cols := len(grid), len(grid[0])
	perimeter := 0

	for _, cell := range regionCells {
		for _, neighbor := range getNeighbors(cell.x, cell.y, rows, cols) {
			if grid[neighbor.x][neighbor.y] != grid[cell.x][cell.y] {
				perimeter++
			}
		}
		// Add edge contributions
		if cell.x == 0 {
			perimeter++
		}
		if cell.x == rows-1 {
			perimeter++
		}
		if cell.y == 0 {
			perimeter++
		}
		if cell.y == cols-1 {
			perimeter++
		}
	}

	return perimeter
}

func calculateTotalPrice(inputMap string) int {
	grid := parseMap(inputMap)
	rows, cols := len(grid), len(grid[0])
	visited := make([][]bool, rows)
	for i := range visited {
		visited[i] = make([]bool, cols)
	}

	totalPrice := 0
	for x := 0; x < rows; x++ {
		for y := 0; y < cols; y++ {
			if !visited[x][y] {
				regionCells := floodFill(grid, x, y, visited)
				area := len(regionCells)
				perimeter := calculatePerimeter(grid, regionCells)
				price := area * perimeter
				totalPrice += price
			}
		}
	}

	return totalPrice
}

func main() {
	content, err := os.ReadFile("perem.txt")
	if err != nil {
		fmt.Printf("Error reading file: %v\n", err)
		return
	}

	result := calculateTotalPrice(string(content))
	fmt.Println(result)
}
