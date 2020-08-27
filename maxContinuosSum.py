def largeSum(l):

    if len(l)==0:
        return 0

    max_sum = current_sum = l[0]

    for i in range(1,len(l)):

        current_sum = max(l[i],l[i]+current_sum)
        
        
        max_sum = max(current_sum,max_sum)

    print(max_sum)


l=[-1,3,4,-5,2,3,-9]

largeSum(l)