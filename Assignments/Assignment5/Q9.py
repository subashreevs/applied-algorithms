def GraphInGokuldham(n: int, s: str) -> int:
    balance = 0
    components = 0

    for char in s:
        if char == '(':
            balance += 1
        elif char == ')':
            balance -= 1
        
        if balance == 0:
            components += 1
    
    return components

# Test cases
print(GraphInGokuldham(1, "()"))          # Expected Output: 1
print(GraphInGokuldham(3, "()(()))"))     # Expected Output: 2
