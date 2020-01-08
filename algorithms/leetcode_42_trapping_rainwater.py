def trap(height):
    decreasingHeightStack, totalWaterTrapped = [], 0

    for i, v in enumerate(height):
        while len(decreasingHeightStack) > 0 and height[decreasingHeightStack[-1]] <= v:
            bottomHeight = height[decreasingHeightStack.pop()]
            if len(decreasingHeightStack) == 0:
                break
            leftUpperIndex = decreasingHeightStack[-1]
            heightDiff = min(height[leftUpperIndex], v) - bottomHeight
            width = i - leftUpperIndex - 1
            totalWaterTrapped += heightDiff * width

        decreasingHeightStack.append(i)

    return totalWaterTrapped

print(trap([4,3,2,1,1,2,4,4]))
