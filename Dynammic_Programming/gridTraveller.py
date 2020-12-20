'''
Given n*m matrix find number of ways to reach bottom-right from top-left

sol:
Use dynamic programming

time complexity - O(n)
space complexity - O(n)
'''

def gridNumber(n,m,memo={}):
    if (n,m) in memo:
        return memo[(n,m)]
    if n==0 or m==0:
        return 0
    if n==1 and m==1:
        return 1

    memo[(n,m)] = gridNumber(n-1,m,memo) + gridNumber(n,m-1,memo)
    return memo[(n,m)]


print(gridNumber(5,5))