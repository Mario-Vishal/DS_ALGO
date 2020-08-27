class node:

    def __init__(self,val):

        self.val=val
        self.next = None


class List:

    def __init__(self):
        
        self.head=None

    def append(self,val):

        root = self.head

        if root is None:
            root = node(val)
            return

        while root.next!=None:
            root=root.next

        root.next = node(val)


    def printL(self):

        current = self.head

        while current!=None:
            print(current.val,end=" ")
        
            current = current.next

        print()

def merge(root,root1):

    answer = List()

    if root.val<root1.val:
        answer.head = node(root.val)
        root=root.next
    else:
        answer.head = node(root1.val)
        root1 = root1.next

    i=0
    while root!=None and root1!=None:

        if root.val < root1.val:
            answer.append(root.val)
            root = root.next

        else:
            answer.append(root1.val)
            root1 = root1.next

    while root!=None:
        answer.append(root.val)
        root = root.next

    while root1!=None:
        answer.append(root1.val)
        root1=root1.next

    
    return answer


l = List()
l.head = node(3)
l.append(4)
l.append(6)
l.append(8)
l.append(10)
# l.printL()

l1 = List()
l1.head = node(5)
l1.append(7)
l1.append(9)
l1.append(11)
# l1.printL()


h = merge(l.head,l1.head)

h.printL()



