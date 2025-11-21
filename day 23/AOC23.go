package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strings"
)

func bronKerbosch(r, p, x map[string]bool, graph map[string]map[string]bool, cliques *[][]string) {
	if len(p) == 0 && len(x) == 0 {
		var clique []string
		for node := range r {
			clique = append(clique, node)
		}
		*cliques = append(*cliques, clique)
		return
	}

	pCopy := make(map[string]bool)
	for k, v := range p {
		pCopy[k] = v
	}

	for node := range pCopy {
		newR := make(map[string]bool)
		for k, v := range r {
			newR[k] = v
		}
		newR[node] = true

		newP := make(map[string]bool)
		newX := make(map[string]bool)

		for neighbor := range graph[node] {
			if p[neighbor] {
				newP[neighbor] = true
			}
			if x[neighbor] {
				newX[neighbor] = true
			}
		}

		bronKerbosch(newR, newP, newX, graph, cliques)

		delete(p, node)
		x[node] = true
	}
}

func main() {
	file, err := os.Open("Lan.txt")
	if err != nil {
		fmt.Printf("Error: %v\n", err)
		return
	}
	defer file.Close()

	graph := make(map[string]map[string]bool)
	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		parts := strings.Split(scanner.Text(), "-")
		if len(parts) == 2 {
			a, b := parts[0], parts[1]
			if graph[a] == nil {
				graph[a] = make(map[string]bool)
			}
			if graph[b] == nil {
				graph[b] = make(map[string]bool)
			}
			graph[a][b] = true
			graph[b][a] = true
		}
	}

	p := make(map[string]bool)
	for node := range graph {
		p[node] = true
	}

	var cliques [][]string
	bronKerbosch(make(map[string]bool), p, make(map[string]bool), graph, &cliques)

	// Find largest clique
	var largest []string
	for _, clique := range cliques {
		if len(clique) > len(largest) {
			largest = clique
		}
	}

	sort.Strings(largest)
	password := strings.Join(largest, ",")

	fmt.Printf("Largest clique size: %d\n", len(largest))
	fmt.Printf("Password to the LAN party: %s\n", password)
}
