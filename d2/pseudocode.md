##Original Q:
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i. Solve it without using division and in O(n) time.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

##Thought Process
I am looking for useful methods in array.prototype to help me solve 
this problem. Because 1) without using division 2) in O(n) time, I 
want to save the iteration for array.prototype.map function, which 
helps me iterate through the array.

The next obstacle is, how do I get the `rest` array without the 
current iterator? I realized I can use `filter` method from
array. `rest = givenArray.filter(e)` when `e` represent the current
iterator. 

The final question is how do I get the product of all the
elements in `rest` array. I found out `reduce` help me if I write
the callback function to be `(x, y) => { return x * y }`.

The end result is what I put in jim.js