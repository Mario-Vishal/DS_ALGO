'''
Lexicographical order is often known as alphabetical order when dealing with strings. A string is greater than another string if it comes later in a lexicographically sorted list.

Given a word, create a new word by swapping some or all of its characters. This new word must meet two criteria:

It must be greater than the original word
It must be the smallest word that meets the first condition
For example, given the word , the next largest word is .

Complete the function biggerIsGreater below to create and return the new string meeting the criteria. If it is not possible, return no answer.

Function Description

Complete the biggerIsGreater function in the editor below. It should return the smallest lexicographically higher string possible from the given string or no answer.

biggerIsGreater has the following parameter(s):

w: a string

Output Format

For each test case, output the string meeting the criteria. If no answer exists, print no answer.

####MEDIUM LEVEL####

QUESTION LINK - https://www.hackerrank.com/challenges/bigger-is-greater/problem

'''

def biggerIsGreater(w):
    #making the string into a list
    s=list(w)
    l=len(s)
    
    pos=-1
    pos1=-1
    
    #finding the first lowest in the string
    for i in range(l-1,0,-1):
        if s[i-1]<s[i]:
            pos=i-1
            break
    #if we have not found any just reverse the entire array
    if pos==-1:
        return "".join(reverse(s,0,l-1))
        
    #finding the element which is greater than the first lowest which we
    #found above 
    for i in range(l-1,0,-1):
        if s[pos]<s[i]:
            pos1=i
            break
    
   #swapping the elements at those positions
    s[pos],s[pos1]=s[pos1],s[pos]
        
    #reversing the string starting from the position where we found first
    #lowest + 1 till the end of the string
    s = "".join(reverse(s,pos+1,l-1))

    #as the constraint mentioned that the permuted string should be bigger
    #if statement to check the constraint    
    if s<=w:
        return "no answer"
    else:
        return s

#reverse function which takes list of characters and starting position and 
#ending position
def reverse(s,pos,pos1):
    i=pos
    j=pos1
    while i<j:
        s[j],s[i]=s[i],s[j]
        i+=1
        j-=1
        print(i,j)
    return s


v = biggerIsGreater("dcba")
print(v)