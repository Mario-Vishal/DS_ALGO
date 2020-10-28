def findCharges(l):
    i=1
    answer=[]
    for i in list(l):
        if answer and answer[-1] == i:
            answer.pop()
        else:
            answer.append(i)

        print(answer)

    print(''.join(answer))

# n=int(input())
# l=list(map(int,input().split()))
l='aaacccbbcccd'
findCharges(l)