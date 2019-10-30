import ctypes  # provides low-level arrays
def make_array(n):
    return (n * ctypes.py_object)()


class ArrayList:
    def __init__(self):
        self.data_arr = make_array(1)
        self.n = 0
        self.capacity = 1

    def __len__(self):
        return self.n

    def append(self, val):
        if(self.n == self.capacity):
            self.resize(2 * self.capacity)
        self.data_arr[self.n] = val
        self.n += 1

    def resize(self, new_size):
        new_arr = make_array(new_size)
        for i in range(self.n):
            new_arr[i] = self.data_arr[i]
        self.data_arr = new_arr
        self.capacity = new_size

    def __getitem__(self, ind):
        if not(-self.n <= ind <= (self.n - 1)):
            raise IndexError("Invalid Index")
        elif ind<0:
            return self.data_arr[self.n+ind]
        return self.data_arr[ind]

    def __setitem__(self, ind, val):
        if not(-self.n <= ind <= (self.n - 1)):
            raise IndexError("Invalid Index")
        elif ind<0:
            self.data_arr[self.n+ind]=val
        self.data_arr[ind] = val

    def __iter__(self):
        for i in range(self.n):
            yield self.data_arr[i]

    def extend(self, other_iterable):
        for elem in other_iterable:
            self.append(elem)
            
    def __repr__(self):
        print("[".end="")
        for i in range(self.n-1):
            print(self.data_arr[i],end=", ")
        print(self.data_arr[i],end="")
        print("]")
 
    def __add__(self,other):
        new_arr=make_array(self.n+other.n)
        for i in range(self.n):
            new_arr[i]=self.data_arr[i]
            count+=1
        for j in range(other.n):
            new_arr[count+j]=other.data_arr[j]
        
    def __iadd__(self.other):
        for elem in other_iterable:
            self.append(elem)

    def __mul__(self,multiplyer):
        new_arr=[]
        for i in range(multiplyer):
            for element in self.data_arr:
                new_arr.append(element)
        return new_arr

    def __rmul__(multiplyer,self):
        return __mul__(self.multiplyer)
