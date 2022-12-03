package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {
	input, err := os.ReadFile("03.input.txt")
	if err != nil {
		panic(err)
	}

	lines := strings.Split(string(input), "\n")

	// a
	prioritySum := 0
	for _, line := range lines {
		if line == "" {
			continue
		}

		itemCount := len(line)
		compartmentA := line[0 : itemCount/2]
		compartmentASet := make(map[rune]bool)
		for _, item := range compartmentA {
			compartmentASet[item] = true
		}

		compartmentB := line[itemCount/2:]
		for _, item := range compartmentB {
			if compartmentASet[item] {
				// a-z => 97-122 => 1-26
				// A-Z => 65-90 => 27-52
				var priority int
				if item >= 'a' {
					priority = int(item-'a') + 1
				} else {
					priority = int(item-'A') + 27
				}
				prioritySum += priority

				fmt.Println("=====")
				fmt.Println(line)
				fmt.Println(compartmentA)
				fmt.Println(compartmentB)
				fmt.Printf("repeated: %c or %d or %d\n", item, item, priority)
				break
			}
		}
	}
	fmt.Printf("a: %d\n",prioritySum)

	// b
	prioritySum = 0
	for i := 0; i < len(lines)-1; i += 3 {
		foundInGroup := make(map[rune]int)
		group := lines[i : i+3]
		for _, sack := range group {
			foundInSack := make(map[rune]bool)
			for _, item := range sack {
				if foundInSack[item] {
					continue
				}
				foundInSack[item] = true
				foundInGroup[item] += 1
			}
		}

		for item, foundCount := range foundInGroup {
			if foundCount == 3 {
				// a-z => 97-122 => 1-26
				// A-Z => 65-90 => 27-52
				var priority int
				if item >= 'a' {
					priority = int(item-'a') + 1
				} else {
					priority = int(item-'A') + 27
				}
				prioritySum += priority
			}
		}

	}

	fmt.Printf("b: %d\n",prioritySum)
}
