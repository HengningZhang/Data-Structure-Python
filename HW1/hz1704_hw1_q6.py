#Hengning Zhang
#CS 1134
#HW 1
#2019/2/2

class Vector:
    def __init__(self, d):
        if isinstance(d,list):
            self.coords=d
        elif isinstance(d,int):
            self.coords = [0]*d
    def __len__(self):
        return len(self.coords)
    def __getitem__(self, j):
        return self.coords[j]
    def __setitem__(self, j, val):
        self.coords[j] = val
    def __add__(self, other):
        if (len(self) != len(other)):
            raise ValueError("dimensions must agree")
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result
    def __sub__(self,other):
        if (len(self) != len(other)):
            raise ValueError("dimensions must agree")
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result
    def __neg__(self):
        result = Vector(len(self))
        for dimension in range(len(self)):
            result[dimension]-=self[dimension]
        return result
    def __mul__(self,multiplyer):
        result = Vector(len(self))
        if isinstance(multiplyer,int):
            for dimension in range(len(self)):
                result[dimension]=self[dimension]*multiplyer
            
        elif isinstance(multiplyer,Vector):
            if (len(self) != len(multiplyer)):
                raise ValueError("dimensions must agree")
            result = 0
            for dimension in range(len(self)):
                result+=self[dimension]*multiplyer[dimension]
            
        return result
    def __rmul__(self,multiplyer):
        return self*multiplyer
    def __eq__(self, other):
        return self.coords == other.coords
    def __ne__(self, other):
        return not (self == other)
    def __str__(self):
        return "<"+ str(self.coords)[1:len(str(self.coords))-1] + ">"
    def __repr__(self):
        return str(self)
