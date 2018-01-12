## Original Q: Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i. Solve it without using division and in O(n) time.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

## Thought Process 
* Use HashMap - I wanted to populate the hashmap with key(index of the given array) and value (value in the index location). Then iterate the given array from begining to end and verify the index i exists in the hashmap
    then ignore that value otherwise prod = prod * value. At the end of the hash map iteration place the product value in a new array of the index i.

    Constraint - This is not an o(n) solution. Its n^2 complexity

* Split and Two array approach - 


