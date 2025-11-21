package main

import (
	"fmt"
	"strconv"
)

func processStones(stoneCounts map[int]int) map[int]int {
	newStoneCounts := make(map[int]int)
	
	for stone, count := range stoneCounts {
		if stone == 0 {
			newStoneCounts[1] += count
		} else {
			stoneStr := strconv.Itoa(stone)
			if len(stoneStr)%2 == 0 {
				mid := len(stoneStr) / 2
				left, _ := strconv.Atoi(stoneStr[:mid])
				right, _ := strconv.Atoi(stoneStr[mid:])
				newStoneCounts[left] += count
				newStoneCounts[right] += count
			} else {
				newStoneCounts[stone*2024] += count
			}
		}
	}
	
	return newStoneCounts
}

func simulateBlinks(initialStones []int, blinks int) map[int]int {
	stoneCounts := make(map[int]int)
	for _, stone := range initialStones {
		stoneCounts[stone]++
	}
	
	for i := 0; i < blinks; i++ {
		stoneCounts = processStones(stoneCounts)
	}
	
	return stoneCounts
}

func countStones(stoneCounts map[int]int) int {
	total := 0
	for _, count := range stoneCounts {
		total += count
	}
	return total
}

func main() {
	initialStones := []int{2, 77706, 5847, 9258441, 0, 741, 883933, 12}
	blinks := 75
	
	finalCounts := simulateBlinks(initialStones, blinks)
	result := countStones(finalCounts)
	
	fmt.Printf("Total stones after %d blinks: %d\n", blinks, result)
}
