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

class MidStack:
    def __init__(self):
        self.data=DoublyLinkedList()
        self.midnode=None
    def __len__(self):
        return self.data.size
    def is_empty(self):
        return len(self)==0
    def push(self,e):
        self.data.add_last(e)
        if len(self)==1 or len(self)==2:
            self.midnode=self.data.first_node()
        elif len(self)//2!=0:
            self.midnode=self.midnode.next
            
    def top(self):
        return self.data.last_node().data
    def pop(self):
        if len(self)==0:
            raise Exception("stack is empty")
        output = self.data.delete_last()
        if len(self)==0:
            self.midnode=None
        elif len(self)==1 or len(self)==2:
            self.midnode=self.data.first_node()
        elif len(self)//2!=0:
            self.midnode=self.midnode.prev
        return output
    def mid_push(self,e):
        if self.is_empty():
            raise Exception("stack is empty")
        else:
            self.data.add_before(self.midnode,e)
        
