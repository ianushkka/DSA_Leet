class Solution:
    def isSubsequence(self, s: str, t: str) -> bool: 
        if len(s)==0 :
            return True
        start=0 

        for i in t :
            if s[start]==i :
                start+=1 

                if start==len(s) :
                    break 
        if start!=len(s) :
            return False 
        else :
            return True
        