from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        #What i had thought at first

        min_len=len(min(strs,key=len))
        res="" 
        for i in range(min_len) : 
            temp=set()

            for j in strs :
                temp.add(j[i]) 
            if len(temp)!=1 :
                break 
            
            val=temp.pop() 
            res+=val 

        return res 
            