# def mergeSort(l,low,high):

#     if len(l)>1:
#         mid = low+high//2

#         mergeSort(l,low,mid)
#         mergeSort(l,mid+1,high)

#         merge(l,low,mid,high)


# def merge_sort(l):

#     if len(l)>1:

#         mid = len(l)//2

#         left_list = l[:mid]
#         right_list = l[mid:]

#         merge_sort(left_list)
#         merge_sort(right_list)

#         i,j,k=0,0,0
#         while i<len(left_list) and j<len(right_list):

#             if left_list[i]<right_list[j]:
#                 l[k]=left_list[i]
#                 i+=1
#             else:
#                 l[k]=right_list[j]
#                 j+=1
#             k+1

#         while i<len(left_list):
#             l[k] = left_list[i]
#             i+=1
#             k+=1

#         while j<len(right_list):
#             l[k] = right_list[j]
#             j+=1
#             k+=1

    
    
# l=[23,4,21,12,9,0]

# print(mergeSort(l))

# print(l)


def merge_sort(l):
    
    if len(l)>1:
        mid=len(l)//2
        left_list = l[:mid]
        right_list = l[mid:]
        merge_sort(left_list)
        merge_sort(right_list)
        i,j,k=0,0,0
        
        while i<len(left_list) and j<len(right_list):
            if left_list[i]<right_list[j]:
                l[k]=left_list[i]
                i+=1
                
            else:
                l[k]=right_list[j]
                j+=1
            k+=1
        while i<len(left_list):
            l[k]=left_list[i]
            i+=1
            k+=1
        while j<len(right_list):
            l[k]=right_list[j]
            j+=1
            k+=1
    return l

l=[34,32,12,56,3,78,6]
merge_sort(l)
print(l)
            


