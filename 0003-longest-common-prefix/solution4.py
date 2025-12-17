from typing import List
class Solution:  
    def longestCommonPrefix(self, strs: List[str]) -> str:

        #Comparing the most different , using sorting 
        
        strs.sort() 

        first=strs[0] 
        last=strs[-1] 

        i=0
        while i<len(first) and i<len(last) and first[i]==last[i] :
            i+=1
        
        return first[:i]