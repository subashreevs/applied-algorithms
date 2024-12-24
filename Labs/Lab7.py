import heapq
def roughNumber(n: int) -> int:
    if n <= 0:
        return 0

    ugly_numbers = []
    heapq.heappush(ugly_numbers,1)

    visited = set([1])

    for i in range(n):
        current_ugly = heapq.heappop(ugly_numbers)

        for prime in [2, 3, 5]:
            next_ugly = current_ugly * prime
            if next_ugly not in visited:
                heapq.heappush(ugly_numbers, next_ugly)
                visited.add(next_ugly)

    # print(visited)

    return current_ugly

print(roughNumber(8))