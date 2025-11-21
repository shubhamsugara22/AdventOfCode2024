package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func parseSchematics(filePath string) ([][]string, [][]string) {
	file, err := os.Open(filePath)
	if err != nil {
		fmt.Printf("Error: %v\n", err)
		return nil, nil
	}
	defer file.Close()

	content := ""
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		content += scanner.Text() + "\n"
	}

	// Handle both Unix and Windows line endings
	contentStr := strings.ReplaceAll(content, "\r\n", "\n")
	schematics := strings.Split(strings.TrimSpace(contentStr), "\n\n")
	var locks, keys [][]string

	for _, schematic := range schematics {
		lines := strings.Split(schematic, "\n")
		if len(lines) > 0 {
			if lines[0] == "#####" {
				locks = append(locks, lines)
			} else if lines[len(lines)-1] == "#####" {
				keys = append(keys, lines)
			}
		}
	}

	return locks, keys
}

func convertToHeights(schematic []string, isLock bool) []int {
	if len(schematic) == 0 {
		return nil
	}

	numColumns := len(schematic[0])
	heights := make([]int, numColumns)

	for col := 0; col < numColumns; col++ {
		height := 0
		if isLock {
			for row := 0; row < len(schematic); row++ {
				if schematic[row][col] == '#' {
					height++
				} else {
					break
				}
			}
		} else {
			for row := len(schematic) - 1; row >= 0; row-- {
				if schematic[row][col] == '#' {
					height++
				} else {
					break
				}
			}
		}
		heights[col] = height
	}

	return heights
}

func countValidPairs(locks, keys [][]string) int {
	if len(locks) == 0 {
		return 0
	}

	validPairs := 0
	maxHeight := len(locks[0])

	for _, lock := range locks {
		lockHeights := convertToHeights(lock, true)
		for _, key := range keys {
			keyHeights := convertToHeights(key, false)

			fits := true
			for i := range lockHeights {
				if lockHeights[i]+keyHeights[i] > maxHeight {
					fits = false
					break
				}
			}

			if fits {
				validPairs++
			}
		}
	}

	return validPairs
}

func main() {
	filePath := "christmas.txt"
	locks, keys := parseSchematics(filePath)
	result := countValidPairs(locks, keys)
	fmt.Printf("Number of unique lock/key pairs that fit: %d\n", result)
}
