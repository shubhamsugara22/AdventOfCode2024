package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func evaluateLeftToRight(numbers []int, operators []string) int {
	result := numbers[0]
	for i, op := range operators {
		switch op {
		case "+":
			result += numbers[i+1]
		case "*":
			result *= numbers[i+1]
		case "||":
			// Concatenate digits
			result, _ = strconv.Atoi(strconv.Itoa(result) + strconv.Itoa(numbers[i+1]))
		}
	}
	return result
}

func generateOperatorCombinations(n int, ops []string) [][]string {
	if n == 0 {
		return [][]string{{}}
	}
	
	smaller := generateOperatorCombinations(n-1, ops)
	var result [][]string
	
	for _, combo := range smaller {
		for _, op := range ops {
			newCombo := make([]string, len(combo)+1)
			copy(newCombo, combo)
			newCombo[len(combo)] = op
			result = append(result, newCombo)
		}
	}
	
	return result
}

func solveCalibration(filePath string) int {
	file, err := os.Open(filePath)
	if err != nil {
		fmt.Printf("Error opening file: %v\n", err)
		return 0
	}
	defer file.Close()

	totalCalibrationResult := 0
	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		line := scanner.Text()
		parts := strings.Split(line, ":")
		if len(parts) != 2 {
			continue
		}

		target, _ := strconv.Atoi(strings.TrimSpace(parts[0]))
		numStrs := strings.Fields(strings.TrimSpace(parts[1]))
		
		var numbers []int
		for _, numStr := range numStrs {
			num, _ := strconv.Atoi(numStr)
			numbers = append(numbers, num)
		}

		numOperators := len(numbers) - 1
		operators := []string{"+", "*", "||"}
		combinations := generateOperatorCombinations(numOperators, operators)

		valid := false
		for _, ops := range combinations {
			if evaluateLeftToRight(numbers, ops) == target {
				valid = true
				break
			}
		}

		if valid {
			totalCalibrationResult += target
		}
	}

	return totalCalibrationResult
}

func main() {
	fileName := "pattern.txt"
	result := solveCalibration(fileName)
	fmt.Printf("Total Calibration Result (with concatenation): %d\n", result)
}
