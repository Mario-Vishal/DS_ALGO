def contains(l,k):

    cache = [[False if j==0 else True if i==0 else None for i in range(k+1)] for j in range(len(l)+1)]

    cache[0][0]=True


    for row in range(1,len(l)+1):
        for column in range(1,k+1):

            if l[row-1]<=column:
                '''
                If the value is less than the sum mentioned in that column then
                we need to check 'OR' of the boolean values which are one row above it
                and also need to check the value at 1 row above current column minus the value of the array
                
                '''
                cache[row][column] = cache[row-1][column-l[row-1]] or cache[row-1][column]

            else:
                cache[row][column] = cache[row-1][column]

    # print(cache)
    return cache[row][column]





l=[3,34,4,12,5,2]
k=25

print(contains(l,k))
cache = [[False if j==0 else True if i==0 else None for i in range(k+1)] for j in range(len(l)+1)]
cache[0][0]=True
# print(cache)