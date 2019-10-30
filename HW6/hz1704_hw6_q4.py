import DoublyLinkedList
'''
def copy_linked_list(lnk_lst):
    output=DoublyLinkedList.DoublyLinkedList()
    if len(lnk_lst)==0:
        return output
    newnode=DoublyLinkedList.DoublyLinkedList.Node()
    newnode.data=lnk_lst.first_node().data
    lnk_lst.add_last(newnode)
    current=lnk_lst.first_node()
    while current.next.next.data!=None:
        current=current.next.next
        lnk_lst.add_after(current,current.data)
    current=lnk_lst.first_node().next
    output.header.next=current
    current.prev.next=current.next
    current.next.prev=current.prev
    current.prev=output.header
    while current.next.next.data!=None:
        current.next=current.next.next
        current=current.next
        current.prev.next=current.next
        current.next.prev=current.prev
        current.prev=output.last_node()
    current.next=output.trailer
    return output
'''
def copy_linked_list(lnk_lst):
    output=DoublyLinkedList.DoublyLinkedList()
    for i in lnk_lst:
        output.add_last(i)
    return output

def deepcopy_linked_list(lnk_lst):
    while deepcopy_linked_list
