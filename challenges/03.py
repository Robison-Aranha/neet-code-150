from typing import List


class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        
        for c in strs:
            sortedArray = sorted(c)
            key = ''.join(sortedArray)
            if key not in anagrams.keys():
                anagrams[key] = []
                    
            anagrams[key].append(c)
        
        finalArray = []
        
        for c in anagrams.keys():
            
            finalArray.append(anagrams[c])
            
        return finalArray
        
        
var = Solution()

print(var.groupAnagrams(["act","pots","tops","cat","stop","hat"]))