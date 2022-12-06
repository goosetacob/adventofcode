package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {
	input, err := os.ReadFile("06.input.txt")
	if err != nil {
		panic(err)
	}

	line := strings.TrimSpace(string(input))
	fmt.Println(line)

	// a
	packetMarker := 4
	for runeIdx := 0; runeIdx < len(line)-packetMarker; runeIdx++ {
		seen := make(map[byte]bool)
		// fmt.Println("===")
		for subIdx := runeIdx; subIdx < runeIdx+packetMarker; subIdx++ {
			// fmt.Printf("%d => |%c|\n", subIdx, line[subIdx])
			seen[line[subIdx]] = true
		}
		if len(seen) == packetMarker {
			fmt.Printf("a: %d\n", runeIdx+packetMarker)
			break
		}
	}

	// b
	messageMarker := 14
	for runeIdx := 0; runeIdx < len(line)-messageMarker; runeIdx++ {
		seen := make(map[byte]bool)
		// fmt.Println("===")
		for subIdx := runeIdx; subIdx < runeIdx+messageMarker; subIdx++ {
			// fmt.Printf("%d => |%c|\n", subIdx, line[subIdx])
			seen[line[subIdx]] = true
		}
		if len(seen) == messageMarker {
			fmt.Printf("b: %d\n", runeIdx+messageMarker)
			break
		}
	}
}
