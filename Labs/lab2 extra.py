class Complex:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def __add__(self,other):
        result = Complex(0,0)
        result.a = self.a+other.a
        result.b = self.b+other.b
        return result
    def __sub__(self,other):
        result = Complex(0,0)
        result.a = self.a-other.a
        result.b = self.b-other.b
        return result
    def __mul__(self,other):
        result = Complex(0,0)
        result.a = self.a*other.a - self.b*other.b
        result.b = self.a*other.b + self.b*other.a
        return result
    def __str__(self):
        if self.b>0:
            return str(self.a)+"+"+str(self.b)+"i"
        elif self.b==0:
            return str(self.a)+"i"
        else:
            return str(self.a)+str(self.b)+"i"
