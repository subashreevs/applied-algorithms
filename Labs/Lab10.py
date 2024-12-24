import sys
def minimumGreedy(arr: list[int]) -> int:

    arr.sort()
    min = 100000000000

    for i in range(len(arr)-1):
        diff = abs(arr[i]-arr[i+1])
        
        if(diff < min):
            min = diff
    
    return min
    
# print(minimumGreedy([1, -3, 71, 68, 17]))
# print(minimumGreedy(2))
