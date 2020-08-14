from linkedList import *

l = LinkedList()
head = Node(10)
l.head = head
l.append(11)
l.append(12)
l.append(13)
l.append(14)
l.append(15)
l.append(16)


def findNode_Nth(head,n):
    left_pointer = head
    
    right_pointer = head

    for i in range(n-1,-1,-1):
        if not right_pointer.next:
            raise LookupError('Given N is larger than the Linked List')

        right_pointer = right_pointer.next

    while right_pointer.next:
        left_pointer = left_pointer.next
        right_pointer = right_pointer.next

    return left_pointer

res = findNode_Nth(l.head , 1)

print(res.val)