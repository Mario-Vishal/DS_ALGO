class Node:
    def __init__(self,val):
        self.val=val
        self.next = None
        

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBeginning(self,val):
        
        if self.head == None:
            self.head = Node(val)
            return

        
        new_node = Node(val)

        new_node.next = self.head
        self.head = new_node

    def printLink(self):
        curr = self.head
        while curr!=None:
            print(curr.val)
            curr = curr.next
        
    def printRev(self,h):
        
        if h!=None:
            self.printRev(h.next)
            print(h.val)

    def append(self,val):

        curr = self.head
        while curr.next !=None:
            curr = curr.next

        curr.next = Node(val)

    def revLink(self):
        curr = self.head
        prev = None
        
        while curr!=None:
            c= curr.next
            curr.next = prev
            prev = curr
            curr = c

        self.head = prev

    def detectCycle(self):

        curr = self.head
        hare=curr.next
        tortoise = curr

        while tortoise and hare and hare.next:
            if tortoise==hare:
                print(True)
                return
            tortoise=tortoise.next
            hare = hare.next.next

        print(False)


# head = Node(10)

# head.next = Node(23)
# head.next.next = Node(34)
# head.next.next.next = Node(5)

# head.next.next.next.next = head.next

# l = LinkedList()
# l.head = head

# l.append(12)
# l.append(34)

# l.printLink()

# l.revLink()
# l.printLink()

def detectCycle(head):

        curr = head
        hare=curr.next
        tortoise = curr

        while tortoise and hare and hare.next:
            if tortoise==hare:
                print(True)
                break
            tortoise=tortoise.next
            hare = hare.next.next

        
        
        # print(False)
        
# detectCycle(head)