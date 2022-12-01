package main

import (
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func main() {
	input, err := os.ReadFile("01.input.txt")
	if err != nil {
		panic(err)
	}

	lines := strings.Split(string(input), "\n")

	// a
	var highest int
	var totalCalories int
	for _, line := range lines {
		if line == "" {
			if highest < totalCalories {
				highest = totalCalories
			}
			totalCalories = 0
		}
		snack, _ := strconv.Atoi(line)
		totalCalories += snack
	}
	if highest < totalCalories {
		highest = totalCalories
	}
	fmt.Println(highest)

	// b
	var elfCalories []int
	totalCalories = 0
	for _, line := range lines {
		if line == "" {
			elfCalories = append(elfCalories, totalCalories)
			totalCalories = 0
		}
		snack, _ := strconv.Atoi(line)
		totalCalories += snack
	}
	elfCalories = append(elfCalories, totalCalories)
	sort.Ints(elfCalories)
	var elfCaloriesCount = len(elfCalories)
	var sum = elfCalories[elfCaloriesCount-1] + elfCalories[elfCaloriesCount-2] + elfCalories[elfCaloriesCount-3]
	fmt.Println(sum)
}
