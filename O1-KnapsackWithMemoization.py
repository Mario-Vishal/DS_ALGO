def knapsack(weight,price,max_weight,size):
    '''
    weight - weight array
    price - price array
    max_weight - the maximum weight of the knapsack
    size - size of the arrays (both weight and price array should be of equal length)
    '''

    #Base Condition - if size is 0 or if the weight is 0, then the max profit would be 0.
    if size==0 or max_weight==0:
        return 0

    #Adding memoization
    if t[size][max_weight] !=-1:
        return t[size][max_weight]

    #Choice Diagram Implementation
    # if the weight of the last item is less than the max_weight
    if weight[size-1] <= max_weight:

        #then we have a choice to include the item or not include it
        #we decide by taking the max profit if we include the item vs if we not include it.
        #In memoization we store the result in the matrix

        t[size][max_weight]= max(price[size-1]+knapsack(weight,price,max_weight - weight[size-1],size-1),
                    knapsack(weight,price,max_weight,size-1))

        return t[size][max_weight]

    #what is the weight is greater than max weight
    elif weight[size-1] > max_weight:

        #we are going to return the same parameters as we did for the above 'not including' condition

        t[size][max_weight] = knapsack(weight,price,max_weight,size-1)

        return t[size][max_weight]



global t
#to implement memoziation we need to have a global variable matrix


weight = [1,3,4,5]
price = [1,4,5,7]
max_weight = 7
size = len(weight)

t = [[-1 for _ in range(size+10)] for _ in range(max_weight+10)]

max_profit = knapsack(weight,price,max_weight,size)


print(max_profit) #output 9 -- price 4 + price 5 is the max profit


