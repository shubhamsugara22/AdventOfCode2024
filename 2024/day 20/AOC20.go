package main

import (
	"bufio"
	"fmt"
	"os"
)

type Pos struct {
	r, c int
}

func bfs(grid [][]rune, start Pos) map[Pos]int {
	distMap := make(map[Pos]int)
	distMap[start] = 0
	queue := []Pos{start}
	directions := []Pos{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}

	for len(queue) > 0 {
		curr := queue[0]
		queue = queue[1:]
		d := distMap[curr]

		for _, dir := range directions {
			nr, nc := curr.r+dir.r, curr.c+dir.c
			newPos := Pos{nr, nc}
			if _, visited := distMap[newPos]; !visited &&
				nr >= 0 && nr < len(grid) && nc >= 0 && nc < len(grid[0]) &&
				grid[nr][nc] != '#' {
				queue = append(queue, newPos)
				distMap[newPos] = d + 1
			}
		}
	}
	return distMap
}

func main() {
	file, err := os.Open("cheats.txt")
	if err != nil {
		fmt.Printf("Error: %v\n", err)
		return
	}
	defer file.Close()

	var grid [][]rune
	var start Pos
	scanner := bufio.NewScanner(file)
	r := 0
	for scanner.Scan() {
		line := []rune(scanner.Text())
		grid = append(grid, line)
		for c, ch := range line {
			if ch == 'S' {
				start = Pos{r, c}
			}
		}
		r++
	}

	startMap := bfs(grid, start)
	
	// Count cheats (simplified version)
	p1 := 0
	directions := []Pos{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
	for pos := range startMap {
		for _, dir := range directions {
			nr, nc := pos.r+2*dir.r, pos.c+2*dir.c
			newPos := Pos{nr, nc}
			if dist, ok := startMap[newPos]; ok {
				if startMap[pos] > dist {
					savings := startMap[pos] - dist - 2
					if savings >= 100 {
						p1++
					}
				}
			}
		}
	}

	fmt.Println(p1)
}
