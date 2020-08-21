def knapsack(wt,val,w):

    #intialize the matrix to store the values
    size = len(wt)
    t=[[0 for i in range(w+1)] for j in range(size+1)]
    # for i in range(size+1):
    #     for j in range(w+1):

    #         if i==0 or j==0:
    #             t[i][j]=0
    #         else:
    #             t[i][j]=-1
    #         print(t)

    
    #iterate through all the elements in the matrix
    for i in range(1,size+1):
        for j in range(1,w+1):

            if wt[i-1] <= j:

                t[i][j] = max(val[i-1]+t[i-1][j-wt[i-1]],t[i-1][j])

            else:
                t[i][j] = t[i-1][j]

    print(t)
    return t[i][j]


weight = [1,3,4,5]
price = [1,4,5,7]
max_weight = 7
size = len(weight)

val = knapsack(weight,price,max_weight)

print(val)
    