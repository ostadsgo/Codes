package main

import (
	"fmt"
	"math/rand"
)

type Hand int

const (
	Rock Hand = iota
	Paper
	Scissors
)

func getWinner(userHand string, computerHand string) {
	if userHand == "r" && computerHand == "s" {
		fmt.Println("You win", "Rocks break scissors.")
	} else if userHand == "p" && computerHand == "r" {
		fmt.Println("You win", "Paper overs rock.")
	} else if userHand == "s" && computerHand == "p" {
		fmt.Println("You win", "Scissors cuts paper.")
	} else if computerHand == "r" && userHand == "s" {
		fmt.Println("You Lose", "Rocks break scissors.")
	} else if computerHand == "p" && userHand == "r" {
		fmt.Println("You Lose", "Paper overs rock.")
	} else if computerHand == "s" && userHand == "p" {
		fmt.Println("You Lose", "Scissors cuts paper.")
	} else {
		fmt.Println("Draw")
	}
}

func main() {
	options := [3]string{"r", "p", "s"}
	userHand := Rock
	randomIndex := rand.Intn(3)
	computerHand := options[randomIndex]
	// determine who wins

}
