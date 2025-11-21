package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

type Scenario struct {
	AX, AY     int
	BX, BY     int
	PrizeX, PrizeY int
}

func parse2(scenario string) Scenario {
	lines := strings.Split(strings.TrimSpace(scenario), "\n")
	var s Scenario
	
	// Parse Button A
	aParts := strings.Split(strings.Split(lines[0], ":")[1], ",")
	s.AX, _ = strconv.Atoi(strings.TrimSpace(strings.Split(aParts[0], "+")[1]))
	s.AY, _ = strconv.Atoi(strings.TrimSpace(strings.Split(aParts[1], "+")[1]))
	
	// Parse Button B
	bParts := strings.Split(strings.Split(lines[1], ":")[1], ",")
	s.BX, _ = strconv.Atoi(strings.TrimSpace(strings.Split(bParts[0], "+")[1]))
	s.BY, _ = strconv.Atoi(strings.TrimSpace(strings.Split(bParts[1], "+")[1]))
	
	// Parse Prize
	prizeParts := strings.Split(strings.Split(lines[2], ":")[1], ",")
	prizeX, _ := strconv.Atoi(strings.TrimSpace(strings.Split(prizeParts[0], "=")[1]))
	prizeY, _ := strconv.Atoi(strings.TrimSpace(strings.Split(prizeParts[1], "=")[1]))
	s.PrizeX = 10000000000000 + prizeX
	s.PrizeY = 10000000000000 + prizeY
	
	return s
}

func solve2(s Scenario) int {
	ax, ay := s.AX, s.AY
	bx, by := s.BX, s.BY
	tx, ty := s.PrizeX, s.PrizeY
	
	b := (tx*ay - ty*ax) / (ay*bx - by*ax)
	a := (tx*by - ty*bx) / (by*ax - bx*ay)
	
	if ax*a+bx*b == tx && ay*a+by*b == ty {
		return 3*a + b
	}
	return 0
}

func main() {
	content, err := os.ReadFile("claw.txt")
	if err != nil {
		fmt.Printf("Error reading file: %v\n", err)
		return
	}

	scenarios := strings.Split(strings.TrimSpace(string(content)), "\n\n")
	answer := 0
	
	for _, scenario := range scenarios {
		s := parse2(scenario)
		answer += solve2(s)
	}
	
	fmt.Println(answer)
}
