import DoublyLinkedList

class Integer:
    def __init__(self,num_str):
        self.data = DoublyLinkedList.DoublyLinkedList()
        for i in range(len(num_str)):
            self.data.add_last(int(num_str[i]))
    def __add__(self,other):
        more=0
        if len(self.data)==0:
            return other
        elif len(other.data)==0:
            return self
        elif len(self.data)>=len(other.data):
            thesum=Integer("")
            longercursor=self.data.last_node()
            shortercursor=other.data.last_node()
        else:
            thesum=Integer("")
            longercursor=other.data.last_node()
            shortercursor=self.data.last_node()
        while shortercursor.data!=None:
            if longercursor.data+shortercursor.data+more<10:
                thesum.data.add_first(longercursor.data+shortercursor.data+more)
                more=0
                shortercursor=shortercursor.prev
                longercursor=longercursor.prev
            else:
                thesum.data.add_first((longercursor.data+shortercursor.data+more)-10)
                more=1
                shortercursor=shortercursor.prev
                longercursor=longercursor.prev
        while longercursor.data!=None:
            if longercursor.data+more<10:
                thesum.data.add_first(longercursor.data+more)
                more=0
                longercursor=longercursor.prev
            else:
                thesum.data.add_first((longercursor.data+more)-10)
                more=1
                longercursor=longercursor.prev
        if more==1:
            thesum.data.add_first(1)
        return thesum
    def __repr__(self):
        output=0
        tens=0
        current=self.data.last_node()
        for i in range(len(self.data)):
            output+=(current.data*10**tens)
            current=current.prev
            tens+=1
        return str(output)

def main():
    n1 = Integer('50')
    n2 = Integer('50')
    n3=n1+n2
    print(n3)

    
