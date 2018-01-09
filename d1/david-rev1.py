"""
d1 solution using stack/queue object
"""
from collections import deque


def solve(mylist):
    tmplist = []
    count = len(mylist)/2
    stack = mylist
    queue = deque(mylist)

    while len(queue) > count:
        tmplist.append(queue.popleft())
        if len(queue) < count:
            break
        else:
            tmplist.append(stack.pop())
    return tmplist

if __name__ == "__main__":
    mylist = [1,2,3,4,5]
    print(solve(mylist))
