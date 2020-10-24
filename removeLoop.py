class Node:

    def __init__(self,data):

        self.data = data

        self.next = None


def detectLoop(head):

    slow = head
    fast = head

    while slow and fast and fast.next:

        slow=slow.next
        fast=fast.next.next

        if slow==fast:
            
            return True,slow
    return False

def removeLoop(head):

    if not detectLoop(head):
        return head 

    b,node = detectLoop(head)
    
    
    curr = node
    count=1
    while node.next!=curr:
        node = node.next
        # print(node.data)
        count+=1

    ptr1=head
    ptr2 = head

    for i in range(count):
        ptr2=ptr2.next

    while ptr2!=ptr1:
        ptr1 = ptr1.next
        ptr2 = ptr2.next

    while ptr2.next!=ptr1:
        ptr2 = ptr2.next

    ptr2.next = None

    return head


head = Node(10)
head.next = Node(20)
head.next.next = Node(4)
head.next.next.next = Node(5)
head.next.next.next.next = Node(6)
head.next.next.next.next.next = Node(7)
head.next.next.next.next.next.next = head.next.next

print(detectLoop(head))

removeLoop(head)

print(detectLoop(head))



