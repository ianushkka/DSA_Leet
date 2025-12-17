from typing import List 
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        #Building one after one (part by part)
        res="" 

        for i in range(len(strs[0])) :
            ch=strs[0][i]

            for s in strs[1:] : 
                if len(s) == i or ch!=s[i] :   #len(s) == i works safely here , as ,as i gets =len(s),,
                    return res                 #,,so it will be True and OR operator will not check the second 
                                               #condition (which was prone to error) ,but we are safe ..
            res+=ch                            #so generally we prefer len(s)<=s .
        
        return res



