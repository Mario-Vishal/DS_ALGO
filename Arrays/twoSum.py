def twoSum(l,k):

    seen={}
    for i in range(len(l)):

        if k-l[i] not in seen.keys():

            seen[l[i]]=i

        else:

            print(seen[k-l[i]],i)
        


l=[3,2,4]

k=6

twoSum(l,k)