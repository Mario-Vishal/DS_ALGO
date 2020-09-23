#given dictionary of words and the given string find the maximum word that can be formed by the given string 
#by deleting some characters which matches the word in the dictionary

#GOOGLE
#WALMART

def longestWord(dictionary,string):
    
    max_word=-1
    res=None
    for st in dictionary:
        
        count=0
        i,j=0,0
        while i<len(st) and j<len(string):
            
            if st[i] == string[j]:
                
                i+=1
                
                count+=1
            j+=1
        
        if max_word<count:
            max_word=count
            res=st

    print(res)

dict = ["pintu", "geeksfor", "geeksgeeks", "plea"," forgeek"]
str = "geeksforgeeks"
longestWord(dict,str)

        

