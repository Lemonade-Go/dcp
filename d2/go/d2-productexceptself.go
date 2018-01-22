package main

import "fmt"

func main() {

	//Soultion with Hashmap, but i think its n^2 complexity
	listinput := []int{1, 2, 3, 4, 5}
	// listinput := []int{1}
	list2 := []int{}

	hm := make(map[int]int)

	for i, val := range listinput {
		hm[i] = val
	}

	for i := range listinput {
		product := 1
		for key, val := range hm {
			if key != i {
				product = product * val
			}
		}
		list2 = append(list2, product)
	}

	fmt.Println("List2 -- ", list2)

	// ====== o(n) solution ========
	// Approach 2
	list3 := [5]int{}
	// list4 := [5]int{}

	left := 1
	for i := 0; i < len(listinput); i++ {
		// list1 = append(list1, p) // append won't work here as it adds at end of the slice.
		list3[i] = left
		left = left * listinput[i]
	}

	fmt.Println("Input List ", listinput)

	right := 1
	for i := len(listinput) - 1; i >= 0; i-- {

		// Approach 2.1 with 1 set of extra array
		// list4[i] = right
		// right = right * listinput[i]

		temp := listinput[i]
		listinput[i] = list3[i] * right
		right = right * temp

	}
	// Approach 2.1 with 1 set of extra array
	// for i := 0; i < len(listinput); i++ {
	// 	listinput[i] = list3[i] * list4[i]
	// 	fmt.Println("Values ====", list3[i], list4[i], listinput[i])
	// }

	fmt.Println("Left array -- ", list3)
	// fmt.Println("Right array --", list4)
	fmt.Println("Output List ", listinput)

}
