from typing import List


class Solution:
    
    def longestConsecutive(self, nums: List[int]) -> int:
        setList = set(nums)
        sortedList = sorted(setList)
        lenList =  len(sortedList)
        sliceIndex = 0
        maxListSequence = 0
        
        for c in range(0, lenList):
            if c + 1 < lenList:
                if sortedList[c + 1] - sortedList[c] != 1:
                    newMax = sliceIndex + 1
                    if newMax> maxListSequence:
                        maxListSequence = newMax
                    sliceIndex = 0
                else:
                    sliceIndex += 1
            else:
                newMax = sliceIndex + 1
                if newMax > maxListSequence:
                    maxListSequence = newMax
                sliceIndex = 0
                
                    
        if maxListSequence == 0:
            return lenList
        else:
            return maxListSequence
                    
                    
var = Solution()

print(var.longestConsecutive([9,1,4,7,3,-1,0,5,8,-1,6]))