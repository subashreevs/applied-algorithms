def treasureHunt(parchment1, parchment2):
    if len(parchment1) < len(parchment2):
        parchment1, parchment2 = parchment2, parchment1
    n, m = len(parchment1), len(parchment2)
    prev = [0] * (m + 1)
    max_length = 0
    
    for i in range(1, n + 1):
        current = [0] * (m + 1)
        for j in range(1, m + 1):
            if parchment1[i - 1] == parchment2[j - 1]:
                current[j] = prev[j - 1] + 1
                max_length = max(max_length, current[j])
            else:
                current[j] = 0
        prev = current  # Update the previous row
    
    return max_length


# Test Case 1
parchment1 = [5, 7, 8, 7, 5, 6]
parchment2 = [8, 7, 5, 3, 9]
print("Test Case 1 Output:", treasureHunt(parchment1, parchment2))  # Expected Output: 3

# Test Case 2
parchment1 = [1, 1, 1, 1, 1]
parchment2 = [1, 1, 1, 1, 1]
print("Test Case 2 Output:", treasureHunt(parchment1, parchment2))  # Expected Output: 5
