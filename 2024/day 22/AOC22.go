package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func generateSecrets(initialSecret, count int) []int {
	secrets := make([]int, count)
	secret := initialSecret

	for i := 0; i < count; i++ {
		// Step 1
		step1 := (secret * 64) % 16777216
		secret ^= step1
		secret %= 16777216

		// Step 2
		step2 := (secret / 32) % 16777216
		secret ^= step2
		secret %= 16777216

		// Step 3
		step3 := (secret * 2048) % 16777216
		secret ^= step3
		secret %= 16777216

		secrets[i] = secret
	}

	return secrets
}

func main() {
	file, err := os.Open("hiding.txt")
	if err != nil {
		fmt.Printf("Error: %v\n", err)
		return
	}
	defer file.Close()

	total := 0
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		buyer, _ := strconv.Atoi(scanner.Text())
		secrets := generateSecrets(buyer, 2000)
		if len(secrets) > 0 {
			total += secrets[len(secrets)-1]
		}
	}

	fmt.Printf("Sum of 2000th secret numbers: %d\n", total)
}
