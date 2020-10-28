class Stack:
    def __init__(self):
        self.l = []

    def push(self,val):
        self.l.append(val)

    def peak(self):
        return self.l[-1]

    def popl(self):
        self.l.pop(-1)

    def isEmpty(self):
        return self.l == []

    def printl(self):
        print(self.l[::-1])


def balance_check(s):
    l = Stack()
    matches = [('{','}'),('(',')'),('[',']')]
    if len(s)%2!=0:
        return False
    for i in s:
        
        if i not in [')','}',']']:
            l.push(i)
        else:
           
            if (l.peak(),i) in matches:
                l.popl()
            else:
                return False
            
    return True

s="[]{]"

print(balance_check(s))


    

