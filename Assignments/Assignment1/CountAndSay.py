def magicalScribe(n: int) -> str:

    prev = "1"  # Base case for the first sequence

    for i in range(1, n):
        j = 0
        count = 1
        temp = ""
        while j < len(prev) - 1:
            if prev[j] == prev[j+1]:
                count += 1
            else:
                temp += str(count) + prev[j]
                count = 1  # Reset count when characters don't match
            j += 1
        # Process the last character in the sequence
        temp += str(count) + prev[j]
        prev = temp  # Update for the next sequence
    
    return prev

# Test case
# print(magicalScribe(4))  # Output: "111221"
