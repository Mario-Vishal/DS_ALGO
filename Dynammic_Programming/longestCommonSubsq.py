#TOP DOWN APPROACH ---------------------------------------------
def lcs(s1,s2,len1,len2):


    #building the dp matrix
    
    
    if len(s1)==0 or len(s2)==0:
        return 0

    if cache[len2][len1]!=None:
        return cache[len2][len1]

   
    if s1[len1-1] == s2[len2-1]:


        cache[len2][len1]  = 1 + lcs(s1,s2,len1-1,len2-1)
        return cache[len2][len1]

    else:
        cache[len2][len1] = max(lcs(s1,s2,len1-1,len2),lcs(s1,s2,len1,len2-1))
        return cache[len2][len1]

s1 = 'SHINCHAN'

s2 = 'NOHARAAA'

global cache

cache = [[0 if i==0 or j==0 else None for i in range(len(s1)+1)] for j in range(len(s2)+1) ]

# print(lcs(s1,s2,len(s1),len(s2)))


#BOTTOM UP APPROACH (bua) -----------------------------------------

def lcs_bua(s1,s2):

    cache = [[0 if i==0 or j==0 else None  for i in range(len(s1)+1)] for j in range(len(s2)+1) ]

    for s2row in range(1,len(s2)+1):
        for s1row in range(1,len(s1)+1):

            if s1[s1row-1] == s2[s2row-1]:

                cache[s2row][s1row] = cache[s2row-1][s1row-1] + 1
                

            else:

                cache[s2row][s1row] = max(cache[s2row-1][s1row],cache[s2row][s1row-1])

        
    return cache[s2row][s1row]


print(lcs_bua(s1,s2))
