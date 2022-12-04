package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	input, err := os.ReadFile("04.input.txt")
	if err != nil {
		panic(err)
	}

	lines := strings.Split(string(input), "\n")

	// a
	containEachOtherCount := 0
	for _, line := range lines {
		if line == "" {
			continue
		}

		elfs := strings.Split(line, ",")

		elfAParts := strings.Split(elfs[0], "-")
		elfAStart, _ := strconv.Atoi(elfAParts[0])
		elfAEnd, _ := strconv.Atoi(elfAParts[1])

		elfBParts := strings.Split(elfs[1], "-")
		elfBStart, _ := strconv.Atoi(elfBParts[0])
		elfBEnd, _ := strconv.Atoi(elfBParts[1])

		elfAContainsElfB := (elfAStart <= elfBStart) && (elfBEnd <= elfAEnd)
		elfBContainsElfA := (elfBStart <= elfAStart) && (elfAEnd <= elfBEnd)

		if elfAContainsElfB || elfBContainsElfA {
			containEachOtherCount += 1
		}
	}
	fmt.Printf("a: %d\n", containEachOtherCount)


	// a
	overlapEachOtherCount := 0
	for _, line := range lines {
		if line == "" {
			continue
		}

		elfs := strings.Split(line, ",")

		elfAParts := strings.Split(elfs[0], "-")
		elfAStart, _ := strconv.Atoi(elfAParts[0])
		elfAEnd, _ := strconv.Atoi(elfAParts[1])

		elfBParts := strings.Split(elfs[1], "-")
		elfBStart, _ := strconv.Atoi(elfBParts[0])
		elfBEnd, _ := strconv.Atoi(elfBParts[1])

		elfAOverlapsElfB := (elfAStart <= elfBStart) && (elfBStart <= elfAEnd)
		elfBOverlapsElfA := (elfBStart <= elfAStart) && (elfAStart <= elfBEnd)

		if elfAOverlapsElfB || elfBOverlapsElfA {
			overlapEachOtherCount += 1
		}
	}
	fmt.Printf("b: %d\n", overlapEachOtherCount)
}
