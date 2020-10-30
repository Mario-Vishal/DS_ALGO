def generate(n):
    m=[[1]]
    if n==1:
        return m
    first=0
    last=0
    while n:
        l=[]
        for i in range(first,last+2):
            print(i)
            if i==first:
                l.append(m[-1][first])
                continue
            if i==last+1:
                l.append(m[-1][last])
                break
            
            temp = m[-1][i-1]+m[-1][i]
            l.append(temp)
        m.append(l)
        n-=1
        first=0
        last=len(l)-1

    return m

generate(5)
            



            
    
