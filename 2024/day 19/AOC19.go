package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func countWaysToForm(design string, patterns map[string]bool, memo map[string]int) int {
	if val, ok := memo[design]; ok {
		return val
	}

	if design == "" {
		return 1
	}

	ways := 0
	for pattern := range patterns {
		if strings.HasPrefix(design, pattern) {
			remaining := design[len(pattern):]
			ways += countWaysToForm(remaining, patterns, memo)
		}
	}

	memo[design] = ways
	return ways
}

func main() {
	file, err := os.Open("tshirt.txt")
	if err != nil {
		fmt.Printf("Error: %v\n", err)
		return
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	var towelPatterns []string
	var designs []string
	readingPatterns := true

	for scanner.Scan() {
		line := scanner.Text()
		if line == "" {
			readingPatterns = false
			continue
		}

		if readingPatterns {
			towelPatterns = strings.Split(line, ", ")
		} else {
			designs = append(designs, line)
		}
	}

	patterns := make(map[string]bool)
	for _, p := range towelPatterns {
		patterns[p] = true
	}

	totalCombinations := 0
	for _, design := range designs {
		memo := make(map[string]int)
		totalCombinations += countWaysToForm(design, patterns, memo)
	}

	fmt.Printf("Total number of combinations: %d\n", totalCombinations)
}
