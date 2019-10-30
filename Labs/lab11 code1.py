import ArrayQueue

class LinkedBinaryTree:

    class Node:
        def __init__(self, data, left=None, right=None):
            self.data = data
            self.parent = None
            self.left = left
            if (self.left is not None):
                self.left.parent = self
            self.right = right
            if (self.right is not None):
                self.right.parent = self

    def __init__(self, root=None):
        self.root = root
        self.size = self.subtree_count(root)

    def __len__(self):
        return self.size

    def is_empty(self):
        return len(self) == 0

    def subtree_count(self, root):
        if (root is None):
            return 0
        else:
            left_count = self.subtree_count(root.left)
            right_count = self.subtree_count(root.right)
            return 1 + left_count + right_count


    def sum(self):
        return self.subtree_sum(self.root)

    def subtree_sum(self, root):
        if (root is None):
            return 0
        else:
            left_sum = self.subtree_sum(root.left)
            right_sum = self.subtree_sum(root.right)
            return root.data + left_sum + right_sum


    def height(self):
        return self.subtree_height(self.root)

    def subtree_height(self, root):
        if (root.left is None and root.right is None):
            return 0
        elif (root.left is  None):
            return 1 + self.subtree_height(root.right)
        elif (root.right is  None):
            return 1 + self.subtree_height(root.left)
        else:
            left_height = self.subtree_height(root.left)
            right_height = self.subtree_height(root.right)
            return 1 + max(left_height, right_height)


    def preorder(self):
        yield from self.subtree_preorder(self.root)

    def subtree_preorder(self, root):
        if(root is None):
            return
        else:
            yield root
            yield from self.subtree_preorder(root.left)
            yield from self.subtree_preorder(root.right)


    def postorder(self):
        yield from self.subtree_postorder(self.root)

    def subtree_postorder(self, root):
        if(root is None):
            return
        else:
            yield from self.subtree_postorder(root.left)
            yield from self.subtree_postorder(root.right)
            yield root


    def inorder(self):
        yield from self.subtree_inorder(self.root)

    def subtree_inorder(self, root):
        if(root is None):
            return
        else:
            yield from self.subtree_inorder(root.left)
            yield root
            yield from self.subtree_inorder(root.right)


    def breadth_first(self):
        if (self.is_empty()):
            return
        line = ArrayQueue.ArrayQueue()
        line.enqueue(self.root)
        while (line.is_empty() == False):
            curr_node = line.dequeue()
            yield curr_node
            if (curr_node.left is not None):
                line.enqueue(curr_node.left)
            if (curr_node.right is not None):
                line.enqueue(curr_node.right)

    def __iter__(self):
        for node in self.breadth_first():
            yield node.data


def binary_tree_even_sum(root):
    output=0
    if(root is None):
        return 0
    else:
        if root.data%2==0:
            return root.data+binary_tree_even_sum(root.right)+binary_tree_even_sum(root.right)
def binary_tree_contains(root,val):
    if root is None:
        return False
    else:
        if root.data==val:
            return True
        else:
            return binary_tree_contains(root.left,val) or binary_tree_contains(root.right,val)
def invert_binary_tree1(root):
    if root.left is None and root.right is None:
        return
    if root.left is None and root.right is not None:
        invert_binary_tree1(root.right)
    elif root.left is not None and root.right is None:
        invert_binary_tree1(root.left)
    else:
        root.left,root.right=root.right,root.left
        invert_binary_tree1(root.left)
        invert_binary_tree1(root.right)
        
def invert_binary_tree2(root):
    if root==None:
        return
    line = ArrayQueue.ArrayQueue()
    line.enqueue(root)
    while (line.is_empty() == False):
        curr_node = line.dequeue()
        curr_node.left,curr_node.right=curr_node.right,curr_node.left
        if (curr_node.left is not None):
            line.enqueue(curr_node.left)
        if (curr_node.right is not None):
            line.enqueue(curr_node.right)

def is_full(root):
    if root is None:
        return True
    else:
        if root.left is None and root.right is not None:
            return False
        elif root.left is not None and root.right is None:
            return False
        else:
            return is_full(root.left) and is_full(root.right)
def is_complete(root):
    if root==None:
        return
    line = ArrayQueue.ArrayQueue()
    line.enqueue(root)
    count=1
    while (line.is_empty() == False):
        for i in range(count):
            curr_node = line.dequeue()
            if (curr_node.left is None and curr_node.right is not None) or (curr_node.left is not None and curr_node.right is None):
                return False
            if (curr_node.left is not None):
                line.enqueue(curr_node.left)
            if (curr_node.right is not None):
                line.enqueue(curr_node.right)
        count*=2
    return True

def preorder_with_stack():
    temp=ArrayStack.ArrayStack()
    
    
def main():
    
    a = LinkedBinaryTree.Node(5)
    b = LinkedBinaryTree.Node(4)
    c = LinkedBinaryTree.Node(6, a, b)
    d = LinkedBinaryTree.Node(8)
    e = LinkedBinaryTree.Node(10, None, d)
    f = LinkedBinaryTree.Node(12, e, c)
    tree=LinkedBinaryTree(f)
    tree=LinkedBinaryTree(f)
    for i in tree:
        print(i)
    is_complete(f)
    print(is_full(f))
    for i in tree:
        print(i)
main()
