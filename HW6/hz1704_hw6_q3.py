import DoublyLinkedList

class CompactString:
    def __init__(self,orig_str):
        self.data= DoublyLinkedList.DoublyLinkedList()
        if orig_str!="":
            for i in range(len(orig_str)):
                if i==0:
                    checker=orig_str[i]
                    counter=1
                elif checker==orig_str[i]:
                    counter+=1
                else:
                    self.data.add_last((orig_str[i-1],counter))
                    counter=1
                    checker=orig_str[i]
            self.data.add_last((orig_str[-1],counter))
            
            
    def __add__(self,other):
        sumcompactstring=CompactString("")
        iterother=iter(other.data)
        for i in self.data:
            sumcompactstring.data.add_last(i)
        if sumcompactstring.data.last_node().data[0]==other.data.first_node().data[0]:
            sumcompactstring.data.last_node().data=(sumcompactstring.data.last_node().data[0],sumcompactstring.data.last_node().data[1]+other.data.first_node().data[1])
            next(iterother)
        for i in iterother:
            sumcompactstring.data.add_last(i)
        return sumcompactstring
    
    
    def __gt__(self,other):
        if len(self.data)==0:
            return False
        elif len(self.data)!=0 and len(other.data)==0:
            return True
        cursor1=self.data.first_node()
        cursor2=other.data.first_node()
        length= cursor1.data[1]-cursor2.data[1]
        
        while cursor1.data!=None or cursor2.data!=None:
            
            if cursor1.data[0]>cursor2.data[0]:
                return True
            elif cursor1.data[0]<cursor2.data[0]:
                return False
            else:
                if length > 0:
                    cursor2 = cursor2.next
                    if cursor2.data==None:
                        return True
                    length-=cursor2.data[1]
                elif length<0:
                    cursor1 = cursor1.next
                    if cursor1.data==None:
                        return False
                    length-=cursor1.data[1]
                else:
                    cursor1=cursor1.next
                    cursor2=cursor2.next
        return False
                    
    
    
    def __le__(self,other):
        return not self>other

    def __lt__(self, other):
        if self>other:
            return False
        cursor2=other.data.first_node()
        cursor1=self.data.first_node()
        length= cursor1.data[1]-cursor2.data[1]
        while cursor1.data!=None or cursor2.data!=None:
            
            if cursor1.data[0]>cursor2.data[0]:
                return False
            elif cursor1.data[0]<cursor2.data[0]:
                return True
            else:
                if length > 0:
                    cursor2 = cursor2.next
                    if cursor2.data==None:
                        return False
                    length-=cursor2.data[1]
                elif length<0:
                    cursor1 = cursor1.next
                    if cursor1.data==None:
                        return True
                    length-=cursor1.data[1]
                else:
                    cursor1=cursor1.next
                    cursor2=cursor2.next
        return False

    def __ge__(self,other):
        return not self<other
    def __repr__(self):
        if len(self.data)==0:
            return ""
        current = self.data.first_node()
        output=""
        while current.data!=None:
            output+=current.data[0]*current.data[1]
            current=current.next
        return output


