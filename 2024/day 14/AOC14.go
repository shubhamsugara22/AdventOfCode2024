package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"strconv"
)

type Robot struct {
	col, row   int
	vcol, vrow int
}

func loadRobots(filename string) []Robot {
	file, err := os.Open(filename)
	if err != nil {
		fmt.Printf("Error opening file: %v\n", err)
		return nil
	}
	defer file.Close()

	pattern := regexp.MustCompile(`-?\d+`)
	var robots []Robot
	
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		matches := pattern.FindAllString(scanner.Text(), -1)
		if len(matches) >= 4 {
			col, _ := strconv.Atoi(matches[0])
			row, _ := strconv.Atoi(matches[1])
			vcol, _ := strconv.Atoi(matches[2])
			vrow, _ := strconv.Atoi(matches[3])
			robots = append(robots, Robot{col, row, vcol, vrow})
		}
	}
	
	return robots
}

func move(robots []Robot, seconds, areaRows, areaCols int) {
	for i := range robots {
		robots[i].row = (robots[i].row + robots[i].vrow*seconds) % areaRows
		robots[i].col = (robots[i].col + robots[i].vcol*seconds) % areaCols
		
		// Handle negative modulo
		if robots[i].row < 0 {
			robots[i].row += areaRows
		}
		if robots[i].col < 0 {
			robots[i].col += areaCols
		}
	}
}

func safetyFactor(robots []Robot, areaRows, areaCols int) int {
	midRow, midCol := areaRows/2, areaCols/2
	quadrants := make(map[string]int)
	
	for _, r := range robots {
		if r.row == midRow || r.col == midCol {
			continue
		}
		key := fmt.Sprintf("%v,%v", r.row < midRow, r.col < midCol)
		quadrants[key]++
	}
	
	result := 1
	for _, count := range quadrants {
		result *= count
	}
	
	return result
}

func main() {
	robots := loadRobots("safety.txt")
	areaRows, areaCols := 103, 101
	
	move(robots, 100, areaRows, areaCols)
	fmt.Printf("Part 1: %d\n", safetyFactor(robots, areaRows, areaCols))
}
