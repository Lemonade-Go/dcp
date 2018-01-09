"""
final python solution for dcp day 1
"""
from collections import deque

def interleave(queue):
    stack = []
    while len(queue) > 0:
        try:
            stack.append(queue.popleft())
            stack.append(queue.pop())
        except IndexError:
            break
    return stack


if __name__ == "__main__":
    queue = deque([1,2,3,4,5])
    print(interleave(queue))
  
