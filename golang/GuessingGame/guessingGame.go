package main

import (
	"fmt"
	"math/rand"
	"time"
)

func main() {
	s1 := rand.NewSource(time.Now().UnixNano())
	r1 := rand.New(s1)
	fmt.Println("I am a number between 1 to 100")
	fmt.Println("Try to guess me.")
	randNumber := r1.Intn(100)
	fmt.Printf("%v", randNumber)
	guess := 0
	counter := 0
	succeed := false

	for counter < 10 {
		fmt.Println("Enter your guess: ")
		fmt.Scanf("%d", &guess)
		if guess > randNumber {
			fmt.Println("Try lower ...")
		} else if guess < randNumber {
			fmt.Println("Try higher")
		} else {
			fmt.Println("Congrats")
			succeed = true
			break
		}
		counter++
	}

	if !succeed {
		fmt.Println("You didn't guess it. Maybe next time!!")
	}
}
