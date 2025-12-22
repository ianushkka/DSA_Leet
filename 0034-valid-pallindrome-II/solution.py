class Solution:
    def validPalindrome(self, s: str) -> bool:  
        left=0 
        right=len(s)-1 

        while left<right :
            if s[left]!=s[right] :
                lskip,rskip=s[left+1:right+1] , s[left:right] 
                return lskip==lskip[::-1] or rskip==rskip[::-1]  

            left+=1 
            right-=1 
        
        return True

        
        