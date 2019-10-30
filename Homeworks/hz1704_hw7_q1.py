from LinkedBinaryTree import LinkedBinaryTree
def min_and_max(bin_tree):
    
    def subtree_min_and_max(subtree_root):
        if subtree_root.left is None and subtree_root.right is None:
            return (subtree_root.data,subtree_root.data)
        elif subtree_root.left is not None and subtree_root.right is None:
            return subtree_min_and_max(subtree_root.left)
        elif subtree_root.left is None and subtree_root.right is not None:
            return subtree_min_and_max(subtree_root.right)
        else:
            return (min(subtree_min_and_max(subtree_root.left)[0],subtree_min_and_max(subtree_root.right)[0]),max(subtree_min_and_max(subtree_root.left)[1],subtree_min_and_max(subtree_root.right)[1],subtree_root.data))
    if bin_tree.is_empty():
        raise Exception("EmptyTree")
    return subtree_min_and_max(bin_tree.root)

def main():
    
    a = LinkedBinaryTree.Node(5)
    b = LinkedBinaryTree.Node(4,a)
    c = LinkedBinaryTree.Node(6,b)
    d = LinkedBinaryTree.Node(8,c)
    e = LinkedBinaryTree.Node(10,d)
    f = LinkedBinaryTree.Node(12, e)
    tree=LinkedBinaryTree(f)
    for i in tree:
        print(i)
    print(min_and_max(tree))
    for i in tree:
        print(i)

main()
