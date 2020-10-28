def reverseSentence(s):
    s=list(s)
    
    n = len(s)
    start =0
    end=n-1

    for i in range(n-1,-1,-1):
        # print(s[i])
        if s[i]==" " or i==0:
            if i==0:
                start=0
            else:
                start=i+1

            for j in range(start,end+1):

                print(s[j],end="")
            end=i-1
            print("",end=" ")


def reverse(s,i,j):
  
    while i<j:
        s[i],s[j]=s[j],s[i]
        i+=1
        j-=1

    return s


reverseSentence("mario vishal")
    