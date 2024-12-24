def peek(stack):
    if stack:
        return stack[-1]   
    else:
        return None
    
def remove_Duplicates(s:str) -> str:
    stack = []
    for i in range(len(s)):
        if(peek(stack) == s[i] ):
            stack.pop()
        else:
            stack.append(s[i])
        
    return("".join(stack))

