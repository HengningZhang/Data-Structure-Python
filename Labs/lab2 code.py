class Polynomial():
    def __init__(self,constructor=[]):
        self.coefficient = constructor
    def __add__(self,other):
        if len(self.coefficient)>len(other.coefficient):
            length = len(other.coefficient)
            longer = self.coefficient
        else:
            length = len(self.coefficient)
            longer = other.coefficient
        result = Polynomial([])
        for i in range(length):
            result.coefficient.append(self.coefficient[i]+other.coefficient[i])
        whatsmore=longer[length:]
        for element in whatsmore:
            result.coefficient.append(element)
        return result
    def __call__(self,num):
        result = 0
        for i in range(len(self.coefficient)):
            result+=self.coefficient[i]*num**i
        return result
    def __str__(self):
        self.coefficient.reverse()
        lst=[str(self.coefficient[i])+"x^"+str(len(self.coefficient)-1-i)+" + " for i in range(len(self.coefficient)) if len(self.coefficient)-1-i>1 and self.coefficient[i]!=0]
        string = "".join(lst)
        string = string[:-3]
        if self.coefficient[-2]!=0:
            string+=" + "+str(self.coefficient[-2])+"x"
        if self.coefficient[-1]!=0:
            string+=" + "+str(self.coefficient[-1])
        self.coefficient.reverse()
        return string
    def __mul__(self,other):
        length = len(self.coefficient)+len(other.coefficient)
        result = Polynomial([0]*(length-1))
        self.coefficient.reverse()
        other.coefficient.reverse()
        for i in range(len(self.coefficient)):
            for j in range(len(other.coefficient)):
                result.coefficient[i+j]+=self.coefficient[i]*other.coefficient[j]
        self.coefficient.reverse()
        other.coefficient.reverse()
        result.coefficient.reverse()
        return result
    def derive(self):
        
        result = Polynomial([0]*(len(self.coefficient)-1))
        self.coefficient.reverse()
        for i in range(len(self.coefficient)-1):
            result.coefficient.append((len(self.coefficient)-i-1)*self.coefficient[i])
        self.coefficient.reverse()
        result.coefficient.reverse(
            )
        return result
                
        
