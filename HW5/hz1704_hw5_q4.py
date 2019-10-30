import ArrayStack

class Queue:
    def __init__(self):
        self.data=ArrayStack.ArrayStack()
        

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self)==0

    def enqueue(self,num):
        self.data.push(num)

    def dequeue(self):
        mirror=ArrayStack.ArrayStack()
        if len(self.data)==0:
            raise Exception("Queue is empty")
        else:
            for element in range(len(self.data)):
                mirror.push(self.data.pop())
            output=mirror.pop()
            for element in range(len(mirror)):
                self.data.push(mirror.pop())

            return output
    
