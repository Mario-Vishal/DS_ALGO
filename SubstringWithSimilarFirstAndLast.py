'''
Given a string s, find out the count of all contiguous substrings whose starting and ending are same character.
Note: string contains lowercase English alphabets only.

Input  : S = "aba"
Output : 4
The substrings are a, b, a and aba

AMAZON

'''


def find(s):

    if len(s)<2:
        return len(s)
    left=0
    right = len(s)-1

    dict={}

    count=0

    while left<right:
       
        if s[left] in dict.keys():
            dict[s[left]]+=1
        else:
            dict[s[left]]=1
            
        if s[right] in dict.keys():
            dict[s[right]]+=1
           
        else:
            dict[s[right]]=1

        left+=1
        right-=1

    if len(s)%2!=0:
        if s[right] in dict.keys():
            dict[s[right]]+=1
        else:
            dict[s[right]]=1


    for i in dict.values():
        count+=i*(i+1)//2
    
    print(count)


s='mariovishal'
find(s)

        

        

        
