package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

// Simplified Day 24 - Logic gate simulation
// Full part 2 requires complex swap detection logic

func main() {
	file, err := os.Open("gates.txt")
	if err != nil {
		fmt.Printf("Error: %v\n", err)
		return
	}
	defer file.Close()

	wireValues := make(map[string]int)
	var gates []string

	scanner := bufio.NewScanner(file)
	readingInitial := true

	for scanner.Scan() {
		line := scanner.Text()
		if line == "" {
			readingInitial = false
			continue
		}

		if readingInitial {
			parts := strings.Split(line, ": ")
			if len(parts) == 2 {
				wire := parts[0]
				value, _ := strconv.Atoi(parts[1])
				wireValues[wire] = value
			}
		} else {
			gates = append(gates, line)
		}
	}

	// Process gates (simplified)
	for len(gates) > 0 {
		processed := false
		for i, gate := range gates {
			parts := strings.Split(gate, " -> ")
			if len(parts) != 2 {
				continue
			}

			expr := strings.Fields(parts[0])
			output := parts[1]

			if len(expr) == 3 {
				wire1, op, wire2 := expr[0], expr[1], expr[2]
				val1, ok1 := wireValues[wire1]
				val2, ok2 := wireValues[wire2]

				if ok1 && ok2 {
					var result int
					switch op {
					case "AND":
						result = val1 & val2
					case "OR":
						result = val1 | val2
					case "XOR":
						result = val1 ^ val2
					}
					wireValues[output] = result
					gates = append(gates[:i], gates[i+1:]...)
					processed = true
					break
				}
			}
		}
		if !processed {
			break
		}
	}

	// Get z wires
	var zWires []string
	for wire := range wireValues {
		if strings.HasPrefix(wire, "z") {
			zWires = append(zWires, wire)
		}
	}
	sort.Sort(sort.Reverse(sort.StringSlice(zWires)))

	binaryResult := ""
	for _, wire := range zWires {
		binaryResult += strconv.Itoa(wireValues[wire])
	}

	result, _ := strconv.ParseInt(binaryResult, 2, 64)
	fmt.Printf("part 1: %d\n", result)
}
