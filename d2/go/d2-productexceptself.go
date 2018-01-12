package main

import "fmt"

func main() {

	//Soultion with Hashmap, but i think its n^2 complexity
	listinput := []int{1, 2, 3, 4, 5}
	list1 := []int{}
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

	// o(n) solution - InProgress

	list3 := [5]int{}
	list4 := [5]int{}

	p := 1
	for i := 0; i < len(listinput); i++ {
		// list1 = append(list1, p)
		list3[i] = p
		p = p * listinput[i]
	}

	p = 1
	for i := len(listinput) - 1; i >= 0; i-- {
		// list2 = append(list2, p) // append won't work here as it adds at end of the slice.
		list4[i] = p
		p = p * listinput[i]
	}

	fmt.Println(listinput)
	for i := 0; i < len(list1); i++ {
		listinput[i] = list3[i] * list4[i]
	}

	fmt.Println(list3)
	fmt.Println(list4)
	fmt.Println(listinput)

	/*
	   int a[N] // This is the input
	   int products_below[N];
	   p=1;
	   for(int i=0;i<N;++i) {
	     products_below[i]=p;
	     p*=a[i];
	   }

	   int products_above[N];
	   p=1;
	   for(int i=N-1;i>=0;--i) {
	     products_above[i]=p;
	     p*=a[i];
	   }

	   int products[N]; // This is the result
	   for(int i=0;i<N;++i) {
	     products[i]=products_below[i]*products_above[i];
	   }
	*/
}
