/**
 * Given a stack of N elements, interleave the first half of the stack with the second half reversed using only one other queue. This should be done in-place.

    Recall that you can only push or pop from a stack, and enqueue or dequeue from a queue.

    For example, if the stack is [1, 2, 3, 4, 5], it should become [1, 5, 2, 4, 3]. If the stack is [1, 2, 3, 4], it should become [1, 4, 2, 3].

    Hint: Try working backwords from the end state.
  *
  ============================================================================
  * to mimic queue's method, I am leveraging array.prototype.shift as dequeue, and array.prototype.push as enqueue.
  * JavaScript's array method pop and push are similar to what stack does.
  * First part is to push stack into queue except the first element.
  * Second is to take from the oldest of queue and the newest of queue alternatively. Since we can only use dequeue but not 
  * .pop(), I use `queue[queue.length-1]` to represent the newest of queue. After everytime we access the newest of queue, 
  * we will re-assign queue as `queue.splice(0, queue.length-1)`.
  *
  * At the end, we print out the stack, which now should represent the interweaving of two half of given stack.
  * Assuming stack length N is not larger than 232-1
*/


const interleaving = (stack, queue) => {
  while (stack.length > 1) {
    queue.push(stack.pop());
  }

  while (queue.length > 1) {
    stack.push(queue.shift());
    stack.push(queue[queue.length - 1]);
    queue = queue.splice(0, queue.length - 1);
  }

  return stack;
}
interleaving([N], [])