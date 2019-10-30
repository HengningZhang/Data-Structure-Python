import ArrayStack
class MaxStack:
    def __init__(self):
        self.data=ArrayStack.ArrayStack()
        self.maxnum=None

    def is_empty(self):
        return self.data.is_empty()

    def __len__(self):
        return len(self.data)

    def push(self,num):
        if self.maxnum==None:
            self.maxnum=num
        if num>self.maxnum:
            self.maxnum=num
        self.data.push((self.maxnum,num))

    def top(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        else:
            return self.data.top()[1]

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        else:
            output=self.data.pop()[1]
            if self.is_empty():
                maxnum=None
            elif self.data.top()[0]<self.maxnum:
                self.maxnum=self.data.top()[0]
            return output

    def max(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        else:
            return self.data.top()[0]
