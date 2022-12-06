package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func solveA(board [][]string) {

}

func main() {
	input, err := os.ReadFile("05.input.txt")
	if err != nil {
		panic(err)
	}

	lines := strings.Split(string(input), "\n\n")

	var board [][]string
	boardLines := strings.Split(lines[0], "\n")
	for lineIdx := len(boardLines) - 1; lineIdx >= 0; lineIdx-- {
		if lineIdx == len(boardLines)-1 {
			stackIds := strings.Split(boardLines[lineIdx], "  ")
			board = make([][]string, len(stackIds))
			continue
		}

		for charIdx := 0; charIdx < len(boardLines[lineIdx]); charIdx += 4 {
			crateIdx := charIdx / 4
			crateChar := boardLines[lineIdx][charIdx : charIdx+3]
			if crateChar == "   " {
				continue
			}
			// fmt.Printf("char: %d => %d |%v|\n", charIdx, crateIdx, crateChar)
			board[crateIdx] = append(board[crateIdx], crateChar)
		}
	}

	moveLines := strings.Split(lines[1], "\n")

	// a
	// for _, move := range moveLines {
	// 	if move == "" {
	// 		continue
	// 	}
	// 	// fmt.Printf("|%v|\n", move)
	// 	moveParts := strings.Split(move, " ")
	// 	// example: move 6 from 6 to 5
	// 	moveCount, _ := strconv.Atoi(moveParts[1])
	// 	stackA, _ := strconv.Atoi(moveParts[3])
	// 	stackA -= 1
	// 	stackB, _ := strconv.Atoi(moveParts[5])
	// 	stackB -= 1
	// 	// fmt.Printf("%d|%d|%d\n", moveCount, stackA, stackB)
	//
	// 	for count := 0; count < moveCount; count++ {
	// 		crate := board[stackA][len(board[stackA])-1]
	// 		board[stackA] = board[stackA][:len(board[stackA])-1]
	// 		board[stackB] = append(board[stackB], crate)
	// 	}
	// }
	//
	// fmt.Printf("a: ")
	// for _, stack := range board {
	// 	cleanStackId := strings.ReplaceAll(stack[len(stack)-1], "[", "")
	// 	cleanStackId = strings.ReplaceAll(cleanStackId, "]", "")
	// 	fmt.Printf("%v", cleanStackId)
	// }
	// fmt.Println("")

	// b
	for _, move := range moveLines {
		if move == "" {
			continue
		}
		moveParts := strings.Split(move, " ")
		//example: move 6 from 6 to 5
		moveCount, _ := strconv.Atoi(moveParts[1])
		stackA, _ := strconv.Atoi(moveParts[3])
		stackA -= 1
		stackB, _ := strconv.Atoi(moveParts[5])
		stackB -= 1

		for i, l := range board {
			fmt.Printf("%d => %v\n", i, l)
		}
		fmt.Printf("\n%d %d %d\n", moveCount, stackA, stackB)

		crates := board[stackA][len(board[stackA])-moveCount:]
		board[stackA] = board[stackA][:len(board[stackA])-moveCount]
		board[stackB] = append(board[stackB], crates...)
	}

	fmt.Printf("b: ")
	for _, stack := range board {
		cleanStackId := strings.ReplaceAll(stack[len(stack)-1], "[", "")
		cleanStackId = strings.ReplaceAll(cleanStackId, "]", "")
		fmt.Printf("%v", cleanStackId)
	}
	fmt.Println("")
}
