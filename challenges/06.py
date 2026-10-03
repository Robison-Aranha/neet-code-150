from typing import List


class Solution:
    
    
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        product = 1
        finalArray = []
        countZero = 0
        
        for v in nums:
            if v != 0:
                product *= v
            else:
                countZero += 1
                if countZero == 2:
                    break
        
        if countZero == 2:
            product = 0
            
        for c in nums:
            value = 0
            
            if countZero == 1:
                if c == 0:
                    value = product
            else:
                if c != 0:
                    value = int(product / c)
            
            finalArray.append(value)
            
        return finalArray
            

var = Solution()

print(var.productExceptSelf([0,8,0]))
       
                
            