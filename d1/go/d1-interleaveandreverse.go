package main

import (
	"fmt"

	"github.com/golang-collections/collections/queue"
	"github.com/golang-collections/collections/stack"
)

func main() {

	/*
		 Psudocode solution for - "Given a stack of N elements,
						interleave the first half of the stack with the second half reversed using only one other queue. This should be done in-place."

		 1) Initialize a stack & queue object
		 2) Iterate the array and store it in stack[5,4,3,2,1]  and queue [1,2,3,4,5]
		 3) Run a loop upto the length of the array
		 4) Overwrite the array (Inplace) with queue and stack elements alternatively to get [1,5,2,4,3]
	*/

	list := []int{1, 2, 3, 4, 5, 6}
	stack := stack.New()
	queue := queue.New()

	// Iterate the array and store in stack and queue
	for _, val := range list {
		stack.Push(val)
		queue.Enqueue(val)
	}

	// Iterate the array and overwrite with Queue and Stack values alternatively
	qflag := true
	for i := range list {
		if qflag {
			val, _ := queue.Dequeue().(int)
			list[i] = val
			qflag = false
		} else {
			val, _ := stack.Pop().(int)
			list[i] = val
			qflag = true
		}

	}

	// Print the list
	fmt.Println("Result Array : ", list)

}
