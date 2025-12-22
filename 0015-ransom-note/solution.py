class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool: 
        d={} 
        for i in magazine :
            if i not in d :
                d[i]=1
            else :
                d[i]+=1 

        for i in ransomNote :
            if i not in d :
                return False 
            
            if d[i]==0 :
                return False 
            
            #kinda else part but we dont need condition as a whole
            d[i]-=1
        return True