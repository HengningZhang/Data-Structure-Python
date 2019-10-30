class DoublyLinkedList:
    class Node:
        def __init__(self, data=None, prev=None, next=None):
            self.data = data
            self.prev = prev
            self.next = next

        def disconnect(self):
            self.data = None
            self.prev = None
            self.next = None


    def __init__(self):
        self.header = DoublyLinkedList.Node()
        self.trailer = DoublyLinkedList.Node()
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return len(self) == 0

    def first_node(self):
        if(self.is_empty()):
            raise Exception("List is empty")
        return self.header.next

    def last_node(self):
        if(self.is_empty()):
            raise Exception("List is empty")
        return self.trailer.prev

    def add_after(self, node, data):
        prev_node = node
        next_node = node.next
        new_node = DoublyLinkedList.Node(data, prev_node, next_node)
        prev_node.next = new_node
        next_node.prev = new_node
        self.size += 1
        return new_node

    def add_first(self, data):
        return self.add_after(self.header, data)

    def add_last(self, data):
        return self.add_after(self.trailer.prev, data)

    def add_before(self, node, data):
        return self.add_after(node.prev, data)

    def delete_node(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        self.size -= 1
        data = node.data
        node.disconnect()
        return data

    def delete_first(self):
        if (self.is_empty()):
            raise Exception("List is empty")
        return self.delete_node(self.first_node())

    def delete_last(self):
        if (self.is_empty()):
            raise Exception("List is empty")
        return self.delete_node(self.last_node())

    def __iter__(self):
        if (self.is_empty()):
            return
        cursor = self.first_node()
        while cursor is not self.trailer:
            yield cursor.data
            cursor = cursor.next

    def __repr__(self):
        return "[" + " <--> ".join([str(item) for item in self]) + "]"

    def __getitem__(self,i):
        if i>self.size-1:
            raise IndexError
        elif i<=self.size//2:
            current=self.header
            for i in range(i+1):
                current=current.next
            return current.data
        else:
            current=self.trailer
            for i in range(self.size-i):
                current=current.prev
            return current.data
class LinkedStack:
    def __init__(self):
        self.data = DoublyLinkedList()
    def __len__(self):
        return self.data.size
    def is_empty(self):
        return self.data.is_empty()
    def push(self,e):
        self.data.add_last(e)
    def pop(self):
        if self.data.is_empty():
            raise Exception("stack is empty")
        output=self.data.last_node().data
        self.data.delete_last()
        return output
    def top(self):
        if self.data.is_empty():
            raise Exception("stack is empty")
        return self.data.last_node().data

class LeakyStack():
    def __init__(self,n):
        self.limit=n
        self.data = DoublyLinkedList()
    def __len__(self):
        return self.data.size
    def is_empty(self):
        return self.data.is_empty()
    def push(self,e):
        if self.data.size==self.limit:
            self.data.delete_first()
        self.data.add_last(e)
    def pop(self):
        if self.data.is_empty():
            raise Exception("stack is empty")
        output=self.data.last_node().data
        self.data.delete_last()
        return output
    def top(self):
        if self.data.is_empty():
            raise Exception("stack is empty")
        return self.data.last_node().data


a=LeakyStack(3)
a.push(1)
a.push(2)
a.push(3)
a.push(4)

print(a.pop())
print(a.pop())
print(a.top())
