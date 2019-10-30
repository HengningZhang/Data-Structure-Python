from LinkedBinaryTree import LinkedBinaryTree
def create_expression_tree(prefix_exp_str):

    if prefix_exp_str=="":
        return LinkedBinaryTree()
    lst=prefix_exp_str.split(" ")
    for i in range(len(lst)):
        if lst[i] not in "+-*/":
            lst[i]=int(lst[i])
    output=LinkedBinaryTree(LinkedBinaryTree.Node(lst[0]))
    prev=output.root
    counter=1
    while counter<len(lst):

        current=LinkedBinaryTree.Node(lst[counter])
        if prev.left is not None and prev.right is not None:
            prev=prev.parent
        if str(prev.data) in "+-*/":
            if prev.left is None:
                prev.left=current
                current.parent=prev
                prev=current
                counter+=1
            elif prev.right is None:
                prev.right=current
                current.parent=prev
                prev=current
                counter+=1
        else:
            prev=prev.parent
            if prev.right is None:
                prev.right=current
                current.parent=prev
                prev=current
                counter+=1
        
    return output

def prefix_to_postfix(prefix_exp_str):
    if prefix_exp_str=="":
        return ""
    tree=create_expression_tree(prefix_exp_str)
    output=""
    for i in tree.subtree_postorder(tree.root):
        output+=str(i.data)+" "
        
    return output [:-1]

'''
    def postfix_generator(root):
        if root is None:
            return
        else:
            yield from postfix_generator(root.left)
            yield from postfix_generator(root.right)
            yield root.data
''' 
                
            
            
