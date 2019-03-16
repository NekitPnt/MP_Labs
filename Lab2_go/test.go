package main

import "fmt"

func main() {
	array := [14]int{3, 4, 0, 2, 1, 2, 2, 4, 5, 3, 1, 2, 8}
	b := make([]int, 0)
	res := make([][]int, 0)

	intCh := make(chan int, len(array))
	var i int
	for i=0; i<len(array); i++{
		intCh <- array[i]
	}
	if len(intCh) > 0 {
		counter := 0
		for ; len(intCh) > 0; {
			if counter == 0{
				if len(b) > 0 {
					res = append(res, b)
				}
				b = make([]int, 0)
				counter = <-intCh
			}else{
				b = append(b, <-intCh)
				counter --
			}
		}
	}
	fmt.Println(res)
}