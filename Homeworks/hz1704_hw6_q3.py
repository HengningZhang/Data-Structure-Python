import DoublyLinkedList

class CompactString:
    def __init__(self,orig_str):
        self.data= DoublyLinkedList.DoublyLinkedList()
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
        sumcompactstring=CompactString()
        sumcompactstring.data=self.data
        sumcompactstring.data.last_node.next=other.data.first_node
        return sumcompactstring
    
    
    def __lt__(self,other):
        cursor1=self.data.first_node()
        cursor2=other.data.first_node()
        length=0
        while cursor1.data!=None and cursor2.data!=None:
            
            if cursor1[0]>cursor2[0]:
                return true
                current1.data[1]-current2.data[1]
    def __le__(self,other):

    def __gt__(self,other):

    def __ge__(self,other):

    def __repr__(self):
        current = self.data.first_node()
        output=""
        while current.data!=None:
            output+=current.data[0]*current.data[1]
            current=current.next
        return output
    
