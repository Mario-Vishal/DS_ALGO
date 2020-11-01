'''
formula for computing the value at a pascal's triangle is
nCr
where n--> the pascal traingle row and r --> is the position of the value
'''

def generate(n,full=False):

    if full:
        r=[]
        for i in range(1,n+1):
            r.append(genRow(i))

        return r

    else:
        return genRow(n)



def genRow(n):
        if n==1:
            return [1]

        l=[]
        l=[1]
        num=n-1
        den=1
        val=1
        val1=1
        temp=0
        for _ in range(1,n-1):
            val*= num
            val1*=den
            temp=int(val/val1)
            num-=1
            den+=1
            l.append(temp)
        l.append(1)

        return l

print(generate(4,True))
        

#explanation note: this is only for me ignore this
#refer sde notes problem no.7

