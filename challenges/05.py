from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        
        lenStrs = len(strs)
        hash = "None"
        
        if lenStrs > 0:
            hash = ""
        
        for i, v in enumerate(strs):
            
            hash += v.encode().hex() 
            
            if i < lenStrs - 1:
                hash += ";"
            
        return hash
        

    def decode(self, s: str) -> List[str]:
        
        if s == "None":
            return []
        
        hexStrings = s.split(";")
        
        finalString = []
        
        for c in hexStrings:
            finalString.append(bytes.fromhex(c).decode())
            
        return finalString
        
    
    
var = Solution()

encoded = var.encode([])

print(encoded)
print(var.decode(encoded))