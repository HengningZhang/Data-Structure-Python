from LinkedBinaryTree import LinkedBinaryTree
from ArrayQueue import ArrayQueue
def print_tree_level(bin_Tree,level):
    output=[]
    if (bin_Tree.is_empty()):
        return
    line = ArrayQueue()
    line.enqueue((bin_Tree.root,0))
    while (line.is_empty() == False):
        curr=line.dequeue()
        output.append(curr)
        depth=curr[1]
        if (curr[0].left is not None):
            line.enqueue((curr[0].left,depth+1))
        if (curr[0].right is not None):
            line.enqueue((curr[0].right,depth+1))

    i=0
    outputlst=[]
    for i in output:
        if i[1]==level:
            
            outputlst.append(i[0].data)
            
    print(outputlst)

def main():
   
    
    g=LinkedBinaryTree.Node(5)
    h=LinkedBinaryTree.Node(11)
    i=LinkedBinaryTree.Node(4)
    f=LinkedBinaryTree.Node(9,i)
    c=LinkedBinaryTree.Node(5,None,f)
    d=LinkedBinaryTree.Node(2)
    e=LinkedBinaryTree.Node(6,g,h)
    
    b=LinkedBinaryTree.Node(7,d,e)
    a=LinkedBinaryTree.Node(2,b,c)
    
    tree=LinkedBinaryTree(a)
    for i in range(4):
        print_tree_level(tree,i)
main()
