def maxNumberOfActivities(start,finish):

    #storing the indexes of the finish time before sorting
    index = {}
    for i in range(len(finish)):
        if finish[i] in index:
            index[finish[i]] = min(index[finish[i]],i)
        else:
            index[finish[i]] = i 

    


    T = []

    for i in range(len(finish)):
        T.append([start[i],finish[i]])

    #sorting the pair of (start,finish) according to finish time.
    T.sort(key = lambda x:x[1])
    
    print(index[T[0][1]]+1,end=" ")

    j=0
    for i in range(1,len(finish)):

        '''
        T[i][0] - is the starting time of the next activity
        T[j][1] - is the finishing time of the previous activity
        '''
        if T[i][0] >= T[j][1]:

            print(index[T[i][1]]+1,end=" ")
            # if starting time is greater or equal to the previous finishing time then updating the previous
            # finishing time to the current select activitie's finish time
            j=i


    
    

    
s1 = [75250, 50074, 43659, 8931, 11273, 27545, 50879, 77924]
f1 = [112960, 114515, 81825, 93424, 54316, 35533, 73383, 160252]
s = [1 , 3 , 0 , 5 , 8 , 5] 
f = [2 , 4 , 6 , 7 , 9 , 9] 
maxNumberOfActivities(s , f) 