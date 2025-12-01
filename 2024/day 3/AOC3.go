package main

import (
	"fmt"
	"os"
	"regexp"
	"strconv"
)

func calculateSumWithConditions(memory string) int {
	mulPattern := regexp.MustCompile(`mul\((\d+),(\d+)\)`)
	doPattern := regexp.MustCompile(`do\(\)`)
	dontPattern := regexp.MustCompile(`don't\(\)`)

	// Combined pattern to find all instructions in order
	combinedPattern := regexp.MustCompile(`mul\((\d+),(\d+)\)|do\(\)|don't\(\)`)

	isMulEnabled := true
	totalSum := 0

	matches := combinedPattern.FindAllStringSubmatch(memory, -1)
	matchIndices := combinedPattern.FindAllStringIndex(memory, -1)

	for i, match := range matches {
		instruction := memory[matchIndices[i][0]:matchIndices[i][1]]

		if mulPattern.MatchString(instruction) && isMulEnabled {
			// Extract numbers from mul instruction
			if len(match) >= 3 && match[1] != "" && match[2] != "" {
				x, _ := strconv.Atoi(match[1])
				y, _ := strconv.Atoi(match[2])
				totalSum += x * y
			}
		} else if doPattern.MatchString(instruction) {
			isMulEnabled = true
		} else if dontPattern.MatchString(instruction) {
			isMulEnabled = false
		}
	}

	return totalSum
}

func main() {
	fileName := "scrambled.txt"
	content, err := os.ReadFile(fileName)
	if err != nil {
		fmt.Printf("Error: File '%s' not found in the current directory.\n", fileName)
		return
	}

	result := calculateSumWithConditions(string(content))
	fmt.Printf("The sum of all valid mul instructions is: %d\n", result)
}
