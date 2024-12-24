from typing import List


def coinTask(prices: List[int]) -> int: 
    min = prices[0]
    profit = 0

    for price in prices:
        if price < min:
            min = price
        if(price - min > profit):
            profit = price - min
    return profit

print(coinTask([7,6,4,3,1]))
