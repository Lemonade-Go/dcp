"""
d2 solution in python
13scoobie | 1/6/2018
"""

"""
Pseudocode thoughts:
    - list comprehension? 
    - iterate over enumerated list and multiply everything but the item

    so the solution below "works", but ends up looping over too many times.
    ideally, we would just have the return list comprehension part... still learning.
"""

from operator import mul
from functools import reduce

def multiple_except(mylist):
    tmp = []
    for count, item in enumerate(mylist):    
        b = [x for i,x in enumerate(mylist) if i != count]
        tmp.append(reduce(mul, b))
    return tmp

if __name__ == "__main__":
    mylist = [1,2,3,4,5]
    print(multiple_except(mylist))
    mylist = [3,2,1]
    print(multiple_except(mylist))
