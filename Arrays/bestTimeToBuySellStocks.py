def calculate(arr):

    max_profit=0
    min=999999
    profit=0
    for i in range(len(arr)):

        if arr[i]<min:
            min=arr[i]

        profit = arr[i]-min

        max_profit = max(profit,max_profit)

    return max_profit


prices = [7,1,5,3,6,4]

print(calculate(prices))

#Time coomplexity - O(n)
