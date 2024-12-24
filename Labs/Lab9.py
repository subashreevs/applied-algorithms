from typing import List

def sortColors(colors: List[int]) -> List[int]:
    start = 0
    end = len(colors) - 1
    index = 0

    while index <= end:
        if colors[index] == 0:
            colors[start], colors[index] = colors[index], colors[start]
            start += 1
            index += 1
        elif colors[index] == 1:
            index += 1
        else:
            colors[index], colors[end] = colors[end], colors[index]
            end -= 1

    return colors
