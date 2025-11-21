package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func step(A int) (int, int) {
	B := A % 8
	B = B ^ 5
	C := A >> B
	B = B ^ 6 ^ C
	return B, C
}

func run(A int) []int {
	var out []int
	for A > 0 {
		B, _ := step(A)
		A = A >> 3
		out = append(out, B%8)
	}
	return out
}

func main() {
	file, err := os.Open("three_digit.txt")
	if err != nil {
		fmt.Printf("Error: %v\n", err)
		return
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	var regA int
	
	// Read register A value
	if scanner.Scan() {
		line := scanner.Text()
		parts := strings.Split(line, ":")
		if len(parts) == 2 {
			regA, _ = strconv.Atoi(strings.TrimSpace(parts[1]))
		}
	}

	result := run(regA)
	fmt.Println(result)
}
