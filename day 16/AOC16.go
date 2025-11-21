package main

import (
	"bufio"
	"container/heap"
	"fmt"
	"os"
)

type State struct {
	x, y, dir, cost int
}

type PriorityQueue []State

func (pq PriorityQueue) Len() int           { return len(pq) }
func (pq PriorityQueue) Less(i, j int) bool { return pq[i].cost < pq[j].cost }
func (pq PriorityQueue) Swap(i, j int)      { pq[i], pq[j] = pq[j], pq[i] }
func (pq *PriorityQueue) Push(x interface{}) {
	*pq = append(*pq, x.(State))
}
func (pq *PriorityQueue) Pop() interface{} {
	old := *pq
	n := len(old)
	item := old[n-1]
	*pq = old[0 : n-1]
	return item
}

func solveMaze(filename string) {
	file, err := os.Open(filename)
	if err != nil {
		fmt.Printf("Error: %v\n", err)
		return
	}
	defer file.Close()

	var grid []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		grid = append(grid, scanner.Text())
	}

	var startX, startY, endX, endY int
	for i, row := range grid {
		for j, cell := range row {
			if cell == 'S' {
				startX, startY = i, j
			} else if cell == 'E' {
				endX, endY = i, j
			}
		}
	}

	directions := [][2]int{{-1, 0}, {0, 1}, {1, 0}, {0, -1}}
	pq := &PriorityQueue{{startX, startY, 1, 0}}
	heap.Init(pq)
	visited := make(map[[3]int]int)

	for pq.Len() > 0 {
		state := heap.Pop(pq).(State)
		
		if state.x == endX && state.y == endY {
			fmt.Printf("part1: %d\n", state.cost)
			return
		}

		key := [3]int{state.x, state.y, state.dir}
		if cost, ok := visited[key]; ok && cost <= state.cost {
			continue
		}
		visited[key] = state.cost

		// Move forward
		dx, dy := directions[state.dir][0], directions[state.dir][1]
		nx, ny := state.x+dx, state.y+dy
		if nx >= 0 && nx < len(grid) && ny >= 0 && ny < len(grid[0]) && grid[nx][ny] != '#' {
			heap.Push(pq, State{nx, ny, state.dir, state.cost + 1})
		}

		// Rotate
		heap.Push(pq, State{state.x, state.y, (state.dir + 1) % 4, state.cost + 1000})
		heap.Push(pq, State{state.x, state.y, (state.dir + 3) % 4, state.cost + 1000})
	}
}

func main() {
	solveMaze("maze.txt")
}
