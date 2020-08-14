class Node:
    def __init__(self,val):
        self.right = None
        self.left = None
        self.val = val

class Queue:
    def __init__(self):
        self.size = None
        self.l=[]

    def enQueue(self,val):
        self.l.append(val)
        self.size = len(self.l)

    def deQueue(self):
        self.l.pop(0)
        self.size=len(self.l)

    def qPeak(self):
        return self.l[0]

    def printQ(self):
        print(*self.l)
        



def insert_node(root,node):
    
    if root is None:
        root = node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insert_node(root.right,node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert_node(root.left,node)

def preOrder(root):
    if root is None:
        return
    else:
        print(root.val)
        preOrder(root.left)
        preOrder(root.right)

def levelOrder(root):
    q = Queue()
    q.enQueue(root)
    while q.size:
        if root.left is not None:
            q.enQueue(root.left)
        if root.right is not None:
            q.enQueue(root.right)
        
        print(q.qPeak())
        q.deQueue()


root = Node(10)
root.left = Node(1)
root.right = Node(4)
root.left.right = Node(0)

# insert_node(9)
# insert_node(10)
# insert_node(4)

insert_node(root,Node(11))

preOrder(root)

levelOrder(root)