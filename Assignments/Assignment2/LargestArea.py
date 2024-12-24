def largestArea(blocks: list[int]) -> int:
    # Append a 0 height at the end to ensure we process all heights in the stack
    blocks.append(0)
    max_area = 0
    stack = []  # Stack will store indices of the blocks

    for i in range(len(blocks)):
        # While the current block is smaller than the block at the top of the stack
        while stack and blocks[i] < blocks[stack[-1]]:
            h = blocks[stack.pop()]  # The height of the rectangle
            # Calculate the width based on the index where we popped
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, h * width)
        stack.append(i)

    return max_area

# Example usage:
# print(largestArea([1, 3, 2, 5, 4]))  # Output: 8
# print(largestArea([3, 4, 5, 3, 5]))  # Output: 15
