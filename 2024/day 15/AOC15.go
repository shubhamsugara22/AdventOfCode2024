package main

import (
	"bufio"
	"fmt"
	"os"
)

type Coord struct {
	x, y int
}

func main() {
	file, err := os.Open("lantern_fish.txt")
	if err != nil {
		fmt.Printf("Error opening file: %v\n", err)
		return
	}
	defer file.Close()

	var mapList []string
	orderList := ""
	inputState := 0
	
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		if line == "" {
			inputState = 1
		} else if inputState == 0 {
			mapList = append(mapList, line)
		} else {
			orderList += line
		}
	}

	wallSet := make(map[Coord]bool)
	openSet := make(map[Coord]bool)
	boxSet := make(map[Coord]bool)
	var robotStart Coord

	for y, row := range mapList {
		for x, c := range row {
			coord := Coord{x, y}
			switch c {
			case '.':
				openSet[coord] = true
			case 'O':
				boxSet[coord] = true
				openSet[coord] = true
			case '#':
				wallSet[coord] = true
			case '@':
				openSet[coord] = true
				robotStart = coord
			}
		}
	}

	directionDict := map[rune]Coord{
		'^': {0, -1},
		'v': {0, 1},
		'>': {1, 0},
		'<': {-1, 0},
	}

	robotPosition := robotStart
	for _, m := range orderList {
		dir := directionDict[m]
		newLoc := Coord{robotPosition.x + dir.x, robotPosition.y + dir.y}

		if wallSet[newLoc] {
			continue
		} else if openSet[newLoc] && !boxSet[newLoc] {
			robotPosition = newLoc
			continue
		} else if boxSet[newLoc] {
			bx, by := newLoc.x+dir.x, newLoc.y+dir.y
			for {
				boxCoord := Coord{bx, by}
				if wallSet[boxCoord] {
					break
				} else if boxSet[boxCoord] {
					bx, by = bx+dir.x, by+dir.y
					continue
				} else if openSet[boxCoord] {
					robotPosition = newLoc
					delete(boxSet, newLoc)
					boxSet[boxCoord] = true
					break
				}
			}
		}
	}

	part1Answer := 0
	for coord := range boxSet {
		part1Answer += 100*coord.y + coord.x
	}

	fmt.Printf("Part1Answer = %d\n", part1Answer)
}
