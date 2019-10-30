from LinkedBinaryTree import LinkedBinaryTree
def is_height_balanced(bin_tree):
    if bin_tree.root is None:
        return True
    def subtree_height(root):
        if root is None:
            return (0,0)
        return (1+max(subtree_height(root.left)[0],subtree_height(root.right)[0]),max(abs(subtree_height(root.left)[0]-subtree_height(root.right)[0]),subtree_height(root.left)[1],subtree_height(root.right)[1]))
    if subtree_height(bin_tree.root)[1]>1:
        return False
    else:
        return True

def main():
    g = LinkedBinaryTree.Node(5)
    a = LinkedBinaryTree.Node(5)
    b = LinkedBinaryTree.Node(4)
    c = LinkedBinaryTree.Node(6, a, b)
    d = LinkedBinaryTree.Node(8,None,g)
    e = LinkedBinaryTree.Node(10, None, d)
    f = LinkedBinaryTree.Node(12, e, c)
    
    tree=LinkedBinaryTree(f)
    for i in tree:
        print(i)
    print(is_height_balanced(tree))
    for i in tree:
        print(i)    
