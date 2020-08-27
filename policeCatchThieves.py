def findCaught(l,k):

    i=0
    s=0
    r=0
    caught=0
    theif = []
    police = []

    while i<len(l):
        if l[i]=='P':
            police.append(i)
        else:
            theif.append(i)
        i+=1

    while s<len(theif) and r<len(police):

        if abs(theif[s]-police[r])<=k:
            caught+=1
            s+=1
            r+=1
        elif theif[s] < police[r]:
            s+=1
        else:
            r+=1


    print(caught)

l=['P','T','P','T','P','T','T','P']

findCaught(l,1)


            

