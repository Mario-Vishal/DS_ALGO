class Node:

    def __init__(self,value):
        self.level=None
        self.value = value
        self.left=None
        self.right =None

class BinarySearchTree:

    def __init__(self):
        self.root=None

    def create(self,val):
        if self.root == None:
            self.root =Node(val)
        else:
            current = self.root

            while True:
                if val<current.value:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val>current.value:
                    if current.right:
                        current=current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

def listChildren(node):
    res=[]
    if node.left !=None:
        res.append(node.left)
    if node.right!=None:
        res.append(node.right)
    return res



class Queue:
    def __init__(self):
        self.list =[]
        

    def enQueue(self,value):
        self.list.append(value)

    def deQueue(self):
        if len(self.list)==0:
            print("Queue is empty")
            return 
        else:
            val=self.list.pop(0)
            return val

    def peak(self):
        return(self.list[0])

    def size(self):
        return len(self.list)

    def dispQ(self):
        print(self.list)
    


def preOrder(root):
    if root ==None:
        return
    else:
        print(root.value,end=" ")
        preOrder(root.left)
        preOrder(root.right)
    

def levelOrder(root):
    q = Queue()
    q.enQueue(root)
    while q.size()!=0:
        l=listChildren(q.peak())
            
        for i in l:
            q.enQueue(i)
            
        print(q.deQueue().value,end=" ")
    print("\n")

# insert function for binary tree(normal not binary search tree)
def insert_bt(root,val):
        q = Queue()
        q.enQueue(root)
        while q.size()!=0:
            current_node = q.peak()
            if current_node.left ==None:
                print(f"inserted to the left of {current_node.value}")
                current_node.left = Node(val)
                break
            elif current_node.right ==None:
                current_node.right = Node(val)
                print(f"inserted to the right of {current_node.value}")
                break
            else:
                q.deQueue()
                q.enQueue(current_node.left)
                q.enQueue(current_node.right)

def deepest_node(root):
    q=Queue()
    q.enQueue(root)
    val=0
    while q.size()!=0:
        l=listChildren(q.peak())
        for i in l:
            q.enQueue(i)
        val = q.peak()
        q.deQueue()
    return val
    

def delete_node(root,val):
    val_deep = deepest_node(root)
    q = Queue()
    q.enQueue(root)
    #search for the node which is to be deleted
    while q.size()!=0:
        node = q.peak()
        
        if node.value ==val:
            node.val = val_deep.value
            break
        else:
            q.deQueue()
            if node.left!=None:
                q.enQueue(node.left)
            if node.right!=None:
                q.enQueue(node.right)
    val_deep=None

        
        

# Simple Binary Tree creation---------

tree = BinarySearchTree()

btree = Node(20)
btree.left=Node(100)
btree.right=Node(3)
btree.left.left = Node(50)
btree.left.right = Node(15)
btree.right.left = Node(250)
btree.right.right = Node(35)
btree.left.left.left = Node(222)
btree.left.left.right = Node(66)
#--------------------------------

#Binary search tree -----------------


l=[123,34,2,12,90,30,44]

for i in l:
    tree.create(i)

# insert_bt(btree,999)
# levelOrder(btree)
# -------------------------------------

# levelOrder(btree)
# insert_bt(btree,999)
# levelOrder(btree)

# tree.create(999)
# levelOrder(tree.root)
levelOrder(btree)

delete_node(btree,250)

levelOrder(btree)

