'''
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

'''

#time complexity - O(n)
#space complexity - O(n)




def merge(intervals):

    out = []
    
    intervals = sorted(intervals,key=lambda  x: x[0])

    for sub in intervals:

        if out and sub[0] <= out[-1][1]:

            out[-1][1]=max(sub[1],out[-1][1])
        else:
            out.append(sub)

    return out


v = merge([[2,3],[4,5],[6,7],[8,9],[1,10]])
print(v)