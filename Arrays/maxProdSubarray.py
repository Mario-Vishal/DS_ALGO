'''
QUESTION : https://practice.geeksforgeeks.org/problems/maximum-product-subarray3604/1

Given an array Arr that contains N integers (may be positive, negative or zero).
Find the product of the maximum product subarray.

Example 1:

Input:
N = 5
Arr[] = {6, -3, -10, 0, 2}
Output: 180
Explanation: Subarray with maximum product
is  6, -3, -10 which gives product as 180.
Example 2:

Input:
N = 6
Arr[] = {2, 3, 4, 5, -1, 0}
Output: 120
Explanation: Subarray with maximum product
is 2, 3, 4, 5 which gives product as 120.
Your Task:
You don't need to read input or print anything. Your task is to complete the function maxProduct() which takes the array of integers arr and n as parameters and returns an integer denoting the answer.
Note: Use 64-bit integer data type to avoid overflow.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

Constraints:
1 <= N <= 500
-102 <= Arri <= 102

#MEDIUM

'''

def maxProduct(self,arr,n):
    minVal = arr[0]
    maxVal = arr[0]

    maxProduct = arr[0]

    for i in range(1,n):
        print(minVal,maxVal,maxProduct,arr[i])
        if arr[i]<0:
            maxVal,minVal=minVal,maxVal

        maxVal = max(arr[i],maxVal*arr[i])
        minVal = min(arr[i],minVal*arr[i])

        maxProduct = max(maxProduct,maxVal)
        

    print(maxProduct)


arr = [-1,-3,-10,0,60]
n=len(arr)
maxProduct(arr,n)