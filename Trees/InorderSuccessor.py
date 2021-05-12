class Node:
    def __init__(self,val):
        self.val=val
        self.left = None
        self.right = None 
        self.parent = None 

def findInorderSuccessor(inputNode):

    if inputNode.right!=None:
        return findLeftMostNode(inputNode.right).val
    else:

        return findParent(inputNode).val
    



def findLeftMostNode(node):
    if(node.left!=None):
        return findLeftMostNode(node.left)
    
    else:
        return node

def findParent(node):
    if (node.parent == None):
        return node 
    
    else:
        if(node.parent.left == node):
            return node.parent
        else:
            return findParent(node.parent)


    



root = Node(20)
root.left = Node(9)
root.left.parent = root
root.right = Node(25)
root.right.parent = root
root.left.left = Node(5)
root.left.left.parent = root.left
root.left.right = Node(12)
root.left.right.parent = root.left
root.left.right.left = Node(11)
root.left.right.left.parent = root.left.right
root.left.right.right = Node(14)
root.left.right.right.parent = root.left.right



val=9
print(findInorderSuccessor(root))