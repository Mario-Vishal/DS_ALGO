def levelOrder(root):

    if root == None:
        return 
    Q=[root]
    Q.append(None)
    
    while Q:
        
        temp = Q[0]
        if temp:
            print(temp.data)

            while Q[0]!=None:
                temp= Q[0]
                if temp.left:
                    Q.append(temp.left)
                
            
                if temp.right:
                    Q.append(temp.right)

                Q.pop(0)

            Q.append(None)

        Q.pop(0)

class Node:

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(10)
root.right.right.right = Node(1)

levelOrder(root)
        