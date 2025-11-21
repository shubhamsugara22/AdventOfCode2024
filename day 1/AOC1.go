package main

import "fmt"

func calculateComparisonScore(list1, list2 []int) int {
	// Count frequency of elements in list2
	list2Freq := make(map[int]int)
	for _, item := range list2 {
		list2Freq[item]++
	}

	// Calculate total score
	totalScore := 0
	for _, item := range list1 {
		frequency := list2Freq[item]
		itemScore := item * frequency
		totalScore += itemScore
	}

	return totalScore
}

func main() {
	// Input lists (truncated for brevity - use full data from Python version)
	// For full implementation, read from file or include complete arrays
	list1 := []int{10047, 10163, 10291, 10420, 10493, 10538, 10775, 10814, 11077, 11156}
	list2 := []int{10142, 10169, 10428, 10501, 10607, 10877, 10891, 11075, 11401, 11742}
	
	// Note: This is a simplified version. For the full solution matching Python,
	// include all 1000 elements from the Python lists or read from a data file

	// Calculate and print result
	result := calculateComparisonScore(list1, list2)
	fmt.Println("Detailed Scoring Breakdown:")
	fmt.Printf("\nTotal Score: %d\n", result)
}
