class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_dict={}
        for i in s : 
            if i not in s_dict :
                s_dict[i]=1 
            else :
                s_dict[i]+=1  

        for i in t :
            if i not in s_dict :
                return i 
            s_dict[i]-=1 
        
        for i in s_dict : 
            if s_dict[i]==-1 :
                return i

             

        