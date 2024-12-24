def countSmaller(nums: list[int]) -> list[int]:

    sorted_nums = sorted(nums)

    ranks = {}  
    
    #1,2,2,4,5
    for i in range(len(sorted_nums)):
        if(sorted_nums[i] not in ranks):
            ranks[sorted_nums[i]] = i
    
    result = []
    for num in nums:
        result.append(ranks[num])

    return result

print(countSmaller([4, 5, 1, 2, 2]))
print(countSmaller([3, 6, 4, 2, 0]))