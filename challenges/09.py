class Solution:
    
    
    def isPalindrome(self, s: str) -> bool:
    
        filteredText =  "".join(char for char in s if char.isalnum())
        
        filteredText = filteredText.lower()
        
        right = 0
        left = len(filteredText) - 1
        
        while (left > right):
            
            if filteredText[right] != filteredText[left]:
                return False
            
            right += 1
            left -= 1
            
                
        return True
    
    
var = Solution()

print(var.isPalindrome("Was it a car or a cat I saw?"))