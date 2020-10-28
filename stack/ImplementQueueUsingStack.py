class stack:

    def __init__(self):
        self.l=[]

    def push(self,val):
        self.l.append(val)

    def pop(self):
        
        return self.l.pop(0)

    def peak(self):
        return self.l[0]
    
    def isEmpty(self):
        return self.l == []

    def printS(self):
        return self.l

class Queue2Stacks:

    def __init__(self):
        self.instack = stack()
        self.outstack = stack()

    def enqueue(self,val):
        self.instack.push(val)

    def dequeue(self):

        if self.outstack.isEmpty():
            while not self.instack.isEmpty():
                
                self.outstack.push(self.instack.pop())

        return self.outstack.pop()

    def isEmpty(self):

        return self.instack.isEmpty() and self.outstack.isEmpty()

    def pp(self):

        print(self.instack.printS())
        print(self.outstack.printS())


q = Queue2Stacks()
q.enqueue(10)
q.enqueue(11)
q.enqueue(12)
print(q.dequeue())
print(q.isEmpty())
# q.pp()

