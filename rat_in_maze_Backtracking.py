def findPath(arr,n):

    seen=set()
    x,y=0,0
    seen.add((x,y))
    path=""
    find(arr,n,x,y,seen,path)

global result
result=[]

def find(arr,n,x,y,seen,path):

    if x==n-1 and y==n-1:
        result.append(path)
        return

    if arr[x][y]==0:
        path=path[:-1]
        seen.pop(-1)
        return path

    #down
    if arr[x][y-1]!=0 and (x,y-1) not in seen:
        path+='D'
        seen.append((x,y-1))
        print(path)
        return find(arr,n,x,y-1,seen,path)
        # path=""
        # seen=[]

    if arr[x-1][y]!=0 and (x,y-1) not in seen:
        path+='R'
        seen.append((x-1,y-1))
        print(path)
        return find(arr,n,x-1,y,seen,path)
        # path=""
        # seen=[]
    print(path)
l=[[1,0,0,0],[1,1,0,1],[1,1,0,0],[0,1,1,1]]
n=4

findPath(l,n)

print(result)
