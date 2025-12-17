from typing import List 
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        #Shrinking Approach 

        res=strs[0] 
        for i in range(len(res)) :
            ch=res[i] 

            for s in strs :
                if len(s)<=i or s[i]!=ch :
                    return res[:i] 

        return res 

        