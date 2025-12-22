class Solution:
    def longestPalindrome(self, s: str) -> int: 
        d={} 
        for i in s :
            if i not in d :
                d[i]=1 
            else :
                d[i]+=1 
        
        res=0 
        flag=True
        for i in d :
            while d[i]>1  : 
                
                res+=2 
                d[i]-=2 
            
        
            if flag==True : 
                if d[i]%2!=0 :
                    res+=1 
                    flag=False 

        return res

        