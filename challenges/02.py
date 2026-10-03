from typing import List


class Solution:
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lenNums = len(nums)
        setNums = set(nums)
        for c in range(0, lenNums):
           diff = target - nums[c]
           if diff in setNums:
               nextNumber =  self.findReversed(nums, diff, c)
               if nextNumber == None:
                   continue
               return [c, nextNumber]
           
            
        return None
    
    def findReversed(self, nums: List[int], target: int, numIndex: int):
        for c in range(len(nums) - 1, -1, -1):
            value = nums[c]
            if numIndex != c and value == target:
                return c
                
var = Solution()

print(var.twoSum([5, 5], 10))