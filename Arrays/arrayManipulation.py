'''
Starting with a 1-indexed array of zeros and a list of operations,
for each operation add a value to each of the array element between two given indices, inclusive. Once all operations have been performed, return the maximum value in the array.

Question LINK - https://www.hackerrank.com/challenges/crush/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
'''

#Problem follows prefix sum algorithm
#Time Complexity - 0(n)
#Space Complexity - O(n)

def arrayManipulation(n, queries):
    #creating an empty array with extra index with all 0s.
    arr = [0]*(n+1)
    sum=0
    max=0
    #traversing through each query
    for Q in queries:
        p=Q[0]
        q=Q[1]
        k=Q[2]
        #adding the k value to the element at index p
        arr[p]+=k
        #subtracting the k value at the index q+1
        #because it needs to follow prefix sum algorithm
        #in prefix sum we add previous element's value to current
        #store it in current index position and so on..
        #at the final index we would get the sum
        #similarly
        #here we are not trying to find the sum but we need to find max
        #so we will not add k to all elements in range(a,b)
        #only add to the first index of range(a,b)
        if q+1<=n:
            arr[q+1]-=k
        
    #later performing prefix sum and checking the max after each sum
    for i in range(1,n+1):
        sum+=arr[i]
        
        if sum>max:
            max=sum 
    return max
        

# n=4
# q=[[2,3,603],[1,1,286],[4,4,882]]

# n=10
# q=[[2,6,8],[3,5,7],[1,8,1],[5,9,15]]

# n=10
# q=[[1,5,3],[4,8,7],[6,9,1]]

nm=input().split()
n = int(nm[0])

m = int(nm[1])

q = []

for _ in range(m):
    q.append(list(map(int, input().rstrip().split())))

print(" -------------------------------------------- ")
print()
print()
arrayManipulation(n,q)