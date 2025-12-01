package main

import (
	"fmt"
	"os"
)

func createDisk(diskMap []int) []int {
	var disk []int
	currentBlockID := 0
	
	for i, block := range diskMap {
		if i%2 == 1 {
			// Free space
			for j := 0; j < block; j++ {
				disk = append(disk, -1)
			}
		} else {
			// File blocks
			for j := 0; j < block; j++ {
				disk = append(disk, currentBlockID)
			}
			currentBlockID++
		}
	}
	
	return disk
}

func partOne(disk []int) []int {
	updatedDisk := make([]int, len(disk))
	copy(updatedDisk, disk)
	
	// Find free spaces
	var freeSpace []int
	for i, num := range disk {
		if num == -1 {
			freeSpace = append(freeSpace, i)
		}
	}
	
	freeIdx := 0
	for i := len(disk) - 1; i >= 0; i-- {
		if disk[i] != -1 && freeIdx < len(freeSpace) && freeSpace[freeIdx] < i {
			indexToMove := freeSpace[freeIdx]
			updatedDisk[indexToMove], updatedDisk[i] = updatedDisk[i], -1
			freeIdx++
		}
	}
	
	return updatedDisk
}

func solve(updatedDisk []int) int {
	sum := 0
	for i, num := range updatedDisk {
		if num > -1 {
			sum += i * num
		}
	}
	return sum
}

func main() {
	content, err := os.ReadFile("snake.txt")
	if err != nil {
		fmt.Printf("Error reading file: %v\n", err)
		return
	}

	var diskMap []int
	for _, ch := range content {
		if ch >= '0' && ch <= '9' {
			diskMap = append(diskMap, int(ch-'0'))
		}
	}

	disk := createDisk(diskMap)
	updatedDisk := partOne(disk)
	fmt.Println(solve(updatedDisk))
}
