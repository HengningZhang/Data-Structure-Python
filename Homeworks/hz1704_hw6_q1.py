import DoublyLinkedList
class LinkedQueue:
    def __init__(self):
        self.data=DoublyLinkedList.DoublyLinkedList()

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data)==0

    def enqueue(self,elem):
        self.data.add_first(elem)

    def dequeue(self):
        return self.data.delete_first(self)

    def first(self):
        return self.data.first_node.data
