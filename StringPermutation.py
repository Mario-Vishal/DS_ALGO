def permutate(s):

    out = []
    #Base Case ----
    if len(s) ==1:
        out = [s]

    else:

        #for every letter in string 

        for i,letter in  enumerate(s):

            #for every permutation resulting fro step 2 and 3

            for p in permutate(s[:i] + s[i+1:]):
                # print("permutation is : ",p)
                # print("current letter is : ",letter)
                
                out += [letter+p]
                # print("output is :",out)

    return out

print(permutate('333'))
