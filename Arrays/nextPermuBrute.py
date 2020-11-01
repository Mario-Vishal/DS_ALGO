'''
Next Permute Brute force 
Time complexity: N!*N
Space Complexity: O(N)
'''

def nextPermute(n):

    r = generate(n)
    flag = False
    for i in range(len(r)):
        if r[i]==n:
            flag = True
            break
    if flag:
        if i==len(r)-1:
            return r[0]
        return r[i+1]
    else:
        return r[0]


def generate(n):

    low=0
    high=len(n)-1
    result=[]
    permute(n,low,high,result)

    return result

def permute(n,low,high,result):

    if low==high:
        g=n.copy()
        result.append(g)
    else:
        # print(n)
        for i in range(low,high+1):

            n[i],n[low] = n[low],n[i]
            permute(n,low+1,high,result)
            n[i],n[low] = n[low],n[i]

v=nextPermute([4,5,1])

print(v)

