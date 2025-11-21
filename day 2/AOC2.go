package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func checkRow(row []int) string {
	if len(row) < 2 {
		return "Safe"
	}

	increasing := true
	decreasing := true

	for i := 1; i < len(row); i++ {
		diff := row[i] - row[i-1]
		absDiff := diff
		if absDiff < 0 {
			absDiff = -absDiff
		}

		if absDiff < 1 || absDiff > 3 {
			return "Unsafe"
		}
		if diff <= 0 {
			increasing = false
		}
		if diff >= 0 {
			decreasing = false
		}
	}

	if increasing || decreasing {
		return "Safe"
	}
	return "Unsafe"
}

func isSafeWithTolerance(row []int) string {
	if checkRow(row) == "Safe" {
		return "Safe"
	}

	// Try removing each element
	for i := 0; i < len(row); i++ {
		modifiedRow := make([]int, 0, len(row)-1)
		modifiedRow = append(modifiedRow, row[:i]...)
		modifiedRow = append(modifiedRow, row[i+1:]...)
		
		if checkRow(modifiedRow) == "Safe" {
			return "Safe"
		}
	}
	return "Unsafe"
}

func main() {
	fileName := "row.txt"
	file, err := os.Open(fileName)
	if err != nil {
		fmt.Printf("Error: '%s' not found in the current directory.\n", fileName)
		return
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	safeCount := 0
	rowNum := 1

	fmt.Println("\nResults:")
	for scanner.Scan() {
		line := scanner.Text()
		fields := strings.Fields(line)
		row := make([]int, 0, len(fields))

		for _, field := range fields {
			num, err := strconv.Atoi(field)
			if err != nil {
				continue
			}
			row = append(row, num)
		}

		result := isSafeWithTolerance(row)
		fmt.Printf("Row %d: %s\n", rowNum, result)
		if result == "Safe" {
			safeCount++
		}
		rowNum++
	}

	fmt.Printf("\ntotal safe rows: %d\n", safeCount)
}
