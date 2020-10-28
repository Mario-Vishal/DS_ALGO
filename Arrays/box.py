n=int(input())
print()
for i in range(n):
    if i==0 or i==n-1:
        for j in range(n):
            if j==n-1:
                print(1)
            else:
                print(1,end=" ")
    else:
        print(1,end=" ")
        for j in range(n-1):
            if j==n-2:
                print('',end="")
            else:
                print(' ',end=" ")
        print(1)

    


