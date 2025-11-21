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
	// Full input lists from Python version
	list1 := []int{10047, 10163, 10291, 10420, 10493, 10538, 10775, 10814, 11077, 11156, 11282, 11292, 11377, 11443, 11470, 11492, 11518, 11683, 11698, 11717, 11738, 11773, 11793, 11798, 11827, 11832, 11881, 12443, 12462, 12630, 12683, 12770, 12794, 12959, 13037, 13150, 13200, 13207, 13236, 13264, 13351, 13383, 13516, 13699, 13813, 13845, 13884, 14074, 14130, 14154}
	list2 := []int{10142, 10169, 10428, 10501, 10607, 10877, 10891, 11075, 11401, 11742, 11773, 11773, 11773, 11793, 11865, 12210, 12238, 12305, 12377, 12488, 12494, 12627, 12771, 12888, 12959, 12959, 12959, 12959, 12959, 12959, 12959, 12959, 12959, 12959, 12959, 12959, 12959, 12959, 12959, 12959, 12959, 13132, 13219, 13287, 13380, 13407, 13417, 13647, 13890, 14154}
	
	// Note: Arrays truncated for file size. For production, read from data file.
	// This demonstrates the algorithm with sample data.

	// Calculate and print result
	result := calculateComparisonScore(list1, list2)
	fmt.Println("Detailed Scoring Breakdown:")
	fmt.Printf("\nTotal Score: %d\n", result)
}
