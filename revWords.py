def revWords(s):

    i=0
    j=0

    while i<len(s):

        if s[i]==" " or i==len(s)-1:
            
            ptr = i-1
            if i==len(s)-1:
                ptr=i

            while ptr>j:
                s[ptr],s[j] = s[j],s[ptr]
                ptr-=1
                j+=1
            
            j=i+1
        
        i+=1

    print("".join(s))


revWords(list("mario is a legend"))




