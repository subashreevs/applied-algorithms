def isVowel(c: str):
    if(c == 'a' or c == 'A'
       or c == 'e' or c == 'E'
       or c == 'i' or c == 'I'
       or c == 'o' or c == 'O'
       or c == 'u' or c == 'U'):
        return True
    else:
        return False

indices = []    
vowels = []

def sortVowels(code: str) -> str:
    for i in range(0, len(code)):
        if(isVowel(code[i])):
            indices.append(i)
            vowels.append(code[i])

    vowels.sort()

    ind = 0
    for i in vowels:
        index = indices[ind] 
        code = code[:index] + i + code[index+1:]
        ind+=1
    # print(code)
    return(code)
        

# sortVowels("bRucEwaYne")        