from ChainingHashTableMap import ChainingHashTableMap
from DoublyLinkedList import DoublyLinkedList
class PlayList():
    def __init__(self):
        self.table = ChainingHashTableMap()
        self.dll = DoublyLinkedList()
    def add_song(self,new_song_name):
        self.dll.add_last(new_song_name)
        self.table[new_song_name]=self.dll.last_node()
    def add_song_after(self,song_name,new_song_name):
        try:
            curr=self.table[song_name]
            newnode=DoublyLinkedList.Node(new_song_name)  
            nextone=curr.next
            curr.next=newnode
            newnode.prev=curr
            newnode.next=nextone
            if nextone is not None:
                nextone.prev=newnode
            self.table[new_song_name]=newnode
        except:
            raise KeyError("song not in playlist")
    def play_song(self,song_name):
        try:
            print(song_name)
            print("playing",self.table[song_name].data)
            curr=self.table[song_name]
            if curr is self.dll.header.next:
                self.dll.header.next=curr.next
                if curr.next is not None:
                    curr.next.prev=self.dll.header
            else:
                curr.prev.next=curr.next
                if curr.next is not None:
                    curr.next.prev=curr.prev
                
                
        except:
            raise KeyError("song does not exist")
    def play_list(self):
        if self.dll.header.next is None:
            print(" ")
        
        else:
            curr=self.dll.header.next
            while curr.data is not None:
                print("playing",curr.data)
                curr=curr.next
def main():
    p1 = PlayList( )
    p1.add_song("Despacito")
    p1.add_song("Girls Like You")
    p1.add_song("Shallow")
    p1.add_song("Havana")
    p1.add_song_after("Shallow", "Sunflower")
    p1.add_song_after("Girls Like You", "Shape of You")

    p1.add_song("thank u, next")
    print(p1.dll)
    for i in p1.table:
        print(i)
    p1.play_song("Shallow")
    '''
    p1.play_song("Despacito")
    '''
    p1.play_list( )
main()
        
