def decrypt(s:str)->int:

    i, j = 0, len(s)-1
    count = 0

    while(i<len(s)//2):
        if(s[i]!=s[j]):
            count += 1
        i += 1
        j -= 1
    
    return(count)


# decrypt("abcfgh")
