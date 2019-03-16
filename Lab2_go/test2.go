package main

import (
	"fmt"
	"time"
	"math/rand"
)

func main() {
	intCh := make(chan int)

	go wrt(intCh)
	go read(intCh)
	time.Sleep(100000000000)
	println("finish")
}

func wrt(ch chan int){
	for {
		ch <- rand.Intn(5)
		time.Sleep(1000000000)
	}
}

func read(ch chan int){
	b := make([]int, 0)
	counter := 0
	for {
		if counter == 0{
			if len(b) > 0 {
				fmt.Println(b)
			}
			b = make([]int, 0)
			counter = <-ch
			fmt.Println(counter)
		}else{
			b = append(b, <-ch)
			counter --
		}
	}
}
