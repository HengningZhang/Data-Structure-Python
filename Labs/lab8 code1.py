class ArrayStack:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return (len(self) == 0)

    def push(self, item):
        self.data.append(item)

    def pop(self):
        if(self.is_empty() == True):
            raise Exception("Stack is empty")
        return self.data.pop()

    def top(self):
        if (self.is_empty() == True):
            raise Exception("Stack is empty")
        return self.data[-1]



import ctypes  # provides low-level arrays
def make_array(n):
    return (n * ctypes.py_object)()

class ArrayQueue:
    INITIAL_CAPACITY = 8

    def __init__(self):
        self.data_arr = make_array(ArrayQueue.INITIAL_CAPACITY)
        self.num_of_elems = 0
        self.front_ind = None

    def __len__(self):
        return self.num_of_elems

    def is_empty(self):
        return (len(self) == 0)

    def enqueue(self, elem):
        if(self.num_of_elems == len(self.data_arr)):
            self.resize(2 * len(self.data_arr))
        if(self.is_empty()):
            self.data_arr[0] = elem
            self.front_ind = 0
            self.num_of_elems += 1
        else:
            back_ind = (self.front_ind + self.num_of_elems) % len(self.data_arr)
            self.data_arr[back_ind] = elem
            self.num_of_elems += 1

    def dequeue(self):
        if(self.is_empty()):
            raise Exception("Queue is empty")
        val = self.data_arr[self.front_ind]
        self.data_arr[self.front_ind] = None
        self.front_ind = (self.front_ind + 1) % len(self.data_arr)
        self.num_of_elems -= 1
        if(self.is_empty()):
            self.front_ind = None
        if((self.num_of_elems < len(self.data_arr) // 4) and (len(self.data_arr) > ArrayQueue.INITIAL_CAPACITY)):
            self.resize(len(self.data_arr) // 2)
        return val

    def first(self):
        if (self.is_empty()):
            raise Exception("Queue is empty")
        return self.data_arr[self.front_ind]

    def resize(self, new_capacity):
        new_arr = make_array(new_capacity)
        old_arr = self.data_arr
        old_ind = self.front_ind
        for new_ind in range(self.num_of_elems):
            new_arr[new_ind] = old_arr[old_ind]
            old_ind = (old_ind + 1) % len(old_arr)
        self.data_arr = new_arr
        self.front_ind = 0
'''
def remove_even_queue(q):
    length = len(q)
    for i in range(length):
        if q.first()%2!=0:
            q.enqueue(q.first())
        q.dequeue()

q=ArrayQueue()
q.enqueue(1)
q.enqueue(-14)
q.enqueue(5)
q.enqueue(6)
q.enqueue(-7)
q.enqueue(9)
q.enqueue(10)
q.enqueue(-5)
q.enqueue(-8)
remove_even_queue(q)
for i in range(len(q)):
    print(q.first())
    q.dequeue()
     
def remove_even_stack(s):
    length=len(s)
    res=[]
    for i in range(length):
        if s.top()%2!=0:
            res.append(s.top())
        s.pop()
    for i in range(len(res)):
        s.push(res[len(res)-i-1])
s=ArrayStack()
s.push(-8)
s.push(-5)
s.push(10)
s.push(9)
s.push(-7)
s.push(6)
s.push(5)
s.push(-14)
s.push(1)
remove_even_stack(s)
for i in range(len(s)):
    print(s.pop())
    '''
class ArrayDeque():
    INITIAL_CAPACITY = 9

    def __init__(self):
        self.data_arr = make_array(ArrayDeque.INITIAL_CAPACITY)
        self.num_of_elems = 0
        self.front_ind = None
        self.capacity=len(self.data_arr)
    def __len__(self):
        return self.num_of_elems

    def is_empty(self):
        return (len(self) == 0)
    
    def first(self):
        if (self.is_empty()):
            raise Exception("Queue is empty")
        return self.data_arr[self.front_ind]

    def last(self):
        if (self.is_empty()):
            raise Exception("Queue is empty")
        return self.data_arr[int((self.front_ind+len(self)-1)%self.capacity)]

    def enqueue_first(self,elem):
        if(self.num_of_elems == self.capacity):
            self.resize(3 * self.capacity)
        if(self.is_empty()):
            self.data_arr[self.capacity//3] = elem
            self.front_ind = self.capacity//3
            self.num_of_elems += 1
        else:
            self.front_ind = (self.front_ind - 1+self.capacity) % self.capacity
            self.data_arr[int(self.front_ind)] = elem
            self.num_of_elems += 1
    def enqueue_last(self, elem):
        if(self.num_of_elems == self.capacity):
            self.resize(3 * self.capacity)
        if(self.is_empty()):
            self.data_arr[self.capacity//3] = elem
            self.front_ind = self.capacity//3
            self.num_of_elems += 1
        else:
            back_ind = (self.front_ind + self.num_of_elems +self.capacity) % self.capacity
            self.data_arr[int(back_ind)] = elem
            self.num_of_elems += 1
    def dequeue_first(self):
        if(self.is_empty()):
            raise Exception("Queue is empty")
        val = self.data_arr[int(self.front_ind)]
        self.data_arr[int(self.front_ind)] = None
        self.front_ind = (self.front_ind + 1) % len(self.data_arr)
        self.num_of_elems -= 1
        if(self.is_empty()):
            self.front_ind = None
        if((self.num_of_elems < len(self.data_arr) // 9) and (len(self.data_arr) > ArrayQueue.INITIAL_CAPACITY)):
            self.resize(len(self.data_arr) // 3)
        return val
    def dequeue_last(self):
        if(self.is_empty()):
            raise Exception("Queue is empty")
        val = self.last()
        self.data_arr[int(self.data_arr[int((self.front_ind+len(self)-1)%self.capacity)])]=None
        self.num_of_elems-=1
        if(self.is_empty()):
            self.front_ind = None
        if((self.num_of_elems < len(self.data_arr) // 9) and (len(self.data_arr) > ArrayQueue.INITIAL_CAPACITY)):
            self.resize(len(self.data_arr) // 3)
        return val
    def resize(self, new_capacity):
        new_arr = make_array(new_capacity)
        old_arr = self.data_arr
        old_ind = self.front_ind
        for new_ind in range(len(self)):
            new_arr[new_ind+new_capacity//3] = old_arr[int(old_ind)]
            old_ind = (old_ind + 1) % self.capacity
        self.data_arr = new_arr
        self.front_ind = new_capacity/3
        self.capacity = new_capacity

blyat=ArrayDeque()
'''
for i in range():
    blyat.enqueue_last(1)
    print(i,blyat.capacity)
    '''
for i in range(100):
    blyat.enqueue_last(2)
for i in range(100):
    blyat.enqueue_first(2)
for j in range(90):
    print(blyat.dequeue_first())
for j in range(90):
    print(blyat.dequeue_last())
