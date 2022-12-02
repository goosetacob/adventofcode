package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {
	input, err := os.ReadFile("02.input.txt")
	if err != nil {
		panic(err)
	}

	lines := strings.Split(string(input), "\n")
	moveAMap := map[string]int{
		// Rock
		"X": 1,
		// Paper
		"Y": 2,
		// Scissors
		"Z": 3,
	}

	// a
	resultsAMap := map[string]map[string]int{
		// Rock
		"A": {
			// Rock
			"X": 3,
			// Paper
			"Y": 6,
			// Scissors
			"Z": 0,
		},
		// Paper
		"B": {
			// Rock
			"X": 0,
			// Paper
			"Y": 3,
			// Scissors
			"Z": 6,
		},
		// Scissors
		"C": {
			// Rock
			"X": 6,
			// Paper
			"Y": 0,
			// Scissors
			"Z": 3,
		},
	}
	scoreA := 0
	for _, line := range lines {
		if line == "" {
			continue
		}
		moves := strings.Split(line, " ")
		opponent := moves[0]
		self := moves[1]

		scoreA += moveAMap[self] + resultsAMap[opponent][self]
	}
	fmt.Println(scoreA)

	// b
	moveBMap := map[string]int{
		// Lose
		"X": 0,
		// Draw
		"Y": 3,
		// Win
		"Z": 6,
	}
	resultsBMap := map[string]map[string]int{
		// Rock
		"A": {
			// Scissors to Lose
			"X": 3,
			// Rock to Draw
			"Y": 1,
			// Paper to Win
			"Z": 2,
		},
		// Paper
		"B": {
			// Rock to Lose
			"X": 1,
			// Paper to Draw
			"Y": 2,
			// Scissors to Win
			"Z": 3,
		},
		// Scissors
		"C": {
			// Paper to Lose
			"X": 2,
			// Scissors to Draw
			"Y": 3,
			// Rock to Win
			"Z": 1,
		},
	}
	scoreB := 0
	for _, line := range lines {
		if line == "" {
			continue
		}
		moves := strings.Split(line, " ")
		opponent := moves[0]
		self := moves[1]

		scoreB += moveBMap[self] + resultsBMap[opponent][self]
	}
	fmt.Println(scoreB)
}
