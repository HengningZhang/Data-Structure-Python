from LinkedBinaryTree import LinkedBinaryTree

def min_max_BST(bst):
    if bst.root is None:
        return
    current=bst.root
    while current.right is not None:
        current=current.left
    minimum=current.data
    current=bst.root
    while current.right is not None:
        current=current.right
    maximum=current.data
    return (minimum,maximum)

def glt_n(bst,n):
    if bst.root is None:
        return -1
    output=-1
    current=bst.root
    going=True
    while current is not None:
        if current.data==n:
            return current.data
        if current.data<=n:
            output=current.data
        if current.data<=n:
            current=current.right
        elif current.data>n:
            current=current.left

    return output

def compare_BST(bst1,bst2):
    lst1=[]
    lst2=[]
    for i in bst1.subtree_inorder():
        lst1.append(i)
    for i in bst2.subtree_inorder():
        lst2.append(i)
    if len(lst1)!=len(lst2):
        return False
    for i in range(len(lst1)):
        if lst1[i]!=lst2[i]:
            return False
    return True

def is_BST(root):
    def is_BST_helper(root):
        if root.left is None and root.right is None:
            return (root.data,root.data,True)
        elif root.left is None and root.right is not None:
            return is_BST_helper(root.right)
        elif root.left is not None and root.right is None:
            return is_BST_helper(root.left)
        else:
            return (min(is_BST_helper(root.left)[0],is_BST_helper(root.right)[0]),max(is_BST_helper(root.left)[1],is_BST_helper(root.right)[1],root.data),(is_BST_helper(root.left)[1]<root.data and is_BST_helper(root.right)[0]>root.data and is_BST_helper(root.left)[2] and is_BST_helper(root.right)[2]))
    return is_BST_helper(root)[2]
    
def main():
    z=LinkedBinaryTree.Node(6)
    a=LinkedBinaryTree.Node(1)
    b=LinkedBinaryTree.Node(3,None,z)
    c=LinkedBinaryTree.Node(19)
    d=LinkedBinaryTree.Node(25)
    e=LinkedBinaryTree.Node(21,c,d)
    f=LinkedBinaryTree.Node(9)
    g=LinkedBinaryTree.Node(12,f,e)
    h=LinkedBinaryTree.Node(2,a,b)
    i=LinkedBinaryTree.Node(5,h,g)
    tree=LinkedBinaryTree(i)
    print(is_BST(i))

main()
