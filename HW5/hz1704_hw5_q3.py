import ArrayStack
import ArrayDeque

class MidStack():
    def __init__(self):
        self.stack=ArrayStack.ArrayStack()
        self.deque=ArrayDeque.ArrayDeque()

    def is_empty(self):
        return (len(self.stack.data)+self.deque.num_of_elems)==0

    def __len__(self):
        return len(self.stack.data)+self.deque.num_of_elems

    def push(self,num):
        self.deque.enqueue_last(num)
        if self.deque.num_of_elems==len(self.stack.data)+1:
            self.stack.push(self.deque.dequeue_first())

    def top(self):
        if len(self)==0:
            raise Exception("MidStack is empty")
        elif self.deque.num_of_elems!=0:
            return self.deque.last()
        else:
            return self.stack.top()

    def pop(self):
        if len(self)==0:
            raise Exception("MidStack is empty")
        elif self.deque.num_of_elems!=0:
            return self.deque.dequeue_last()
        else:
            return self.stack.pop()

    def mid_push(self,num):
        self.stack.push(num)
