"""
Runtime: 40 ms, faster than 28.24% of Python3 online submissions for Pascal's Triangle II.
Memory Usage: 13.8 MB, less than 69.38% of Python3 online submissions for Pascal's Triangle II.

https://leetcode.com/problems/pascals-triangle-ii/submissions/
"""


def getRow(rowIndex):
    numRows = rowIndex+1
    outputList = [[1]]
    z = 1
    while z < numRows:
        print(z)
        z += 1
        if (outputList[len(outputList) - 1]) == [1]:
            outputList.append([1, 1])
        else:
            lastitem = outputList[len(outputList) - 1]
            nextItem = [1]
            for i in range(len(lastitem)):
                if i < len(lastitem) - 1:
                    nextItem.append(lastitem[i] + lastitem[i + 1])
            nextItem.append(1)
            outputList.append(nextItem)
    return outputList[len(outputList)-1]


rowIndex = 3

print(getRow(rowIndex))