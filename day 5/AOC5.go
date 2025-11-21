package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

type Rule struct {
	X, Y int
}

func parseInputFile(filePath string) ([]Rule, [][]int, error) {
	content, err := os.ReadFile(filePath)
	if err != nil {
		return nil, nil, err
	}

	// Handle both Unix and Windows line endings
	contentStr := strings.ReplaceAll(string(content), "\r\n", "\n")
	sections := strings.Split(strings.TrimSpace(contentStr), "\n\n")
	if len(sections) != 2 {
		return nil, nil, fmt.Errorf("invalid input format: expected 2 sections, got %d", len(sections))
	}

	// Parse rules
	var rules []Rule
	for _, line := range strings.Split(strings.TrimSpace(sections[0]), "\n") {
		parts := strings.Split(line, "|")
		if len(parts) == 2 {
			x, _ := strconv.Atoi(parts[0])
			y, _ := strconv.Atoi(parts[1])
			rules = append(rules, Rule{X: x, Y: y})
		}
	}

	// Parse updates
	var updates [][]int
	for _, line := range strings.Split(strings.TrimSpace(sections[1]), "\n") {
		parts := strings.Split(line, ",")
		var update []int
		for _, p := range parts {
			num, _ := strconv.Atoi(p)
			update = append(update, num)
		}
		updates = append(updates, update)
	}

	return rules, updates, nil
}

func buildGraph(rules []Rule, pages map[int]bool) (map[int][]int, map[int]int) {
	graph := make(map[int][]int)
	inDegree := make(map[int]int)

	for _, rule := range rules {
		if pages[rule.X] && pages[rule.Y] {
			graph[rule.X] = append(graph[rule.X], rule.Y)
			inDegree[rule.Y]++
			if _, exists := inDegree[rule.X]; !exists {
				inDegree[rule.X] = 0
			}
		}
	}

	return graph, inDegree
}

func topologicalSort(update []int, graph map[int][]int, inDegree map[int]int) []int {
	inDegreeCopy := make(map[int]int)
	for k, v := range inDegree {
		inDegreeCopy[k] = v
	}

	var queue []int
	for _, node := range update {
		if inDegreeCopy[node] == 0 {
			queue = append(queue, node)
		}
	}

	var sortedOrder []int
	for len(queue) > 0 {
		node := queue[0]
		queue = queue[1:]
		sortedOrder = append(sortedOrder, node)

		for _, neighbor := range graph[node] {
			inDegreeCopy[neighbor]--
			if inDegreeCopy[neighbor] == 0 {
				queue = append(queue, neighbor)
			}
		}
	}

	return sortedOrder
}

func isValidOrder(update []int, graph map[int][]int, inDegree map[int]int) bool {
	sorted := topologicalSort(update, graph, inDegree)
	if len(sorted) != len(update) {
		return false
	}
	for i := range update {
		if update[i] != sorted[i] {
			return false
		}
	}
	return true
}

func findMiddle(pageList []int) int {
	return pageList[len(pageList)/2]
}

func main() {
	filePath := "rules.txt"
	rules, updates, err := parseInputFile(filePath)
	if err != nil {
		fmt.Printf("Error reading file: %v\n", err)
		return
	}

	totalMiddleSumValid := 0
	totalMiddleSumCorrected := 0

	for _, update := range updates {
		pages := make(map[int]bool)
		for _, page := range update {
			pages[page] = true
		}

		graph, inDegree := buildGraph(rules, pages)

		if isValidOrder(update, graph, inDegree) {
			totalMiddleSumValid += findMiddle(update)
		} else {
			correctedUpdate := topologicalSort(update, graph, inDegree)
			totalMiddleSumCorrected += findMiddle(correctedUpdate)
		}
	}

	fmt.Printf("Sum of middle pages from correctly ordered updates: %d\n", totalMiddleSumValid)
	fmt.Printf("Sum of middle pages after correcting invalid updates: %d\n", totalMiddleSumCorrected)
}
