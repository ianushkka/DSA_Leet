class Solution:
    def reverseStr(self, s: str, k: int) -> str: 
        if len(s)<=k :
            return s[::-1] 

        new="" 
        start=0 
        c=0 

        for i in range(len(s)) : 
            c+=1 
            if c==k :
                temp=s[start:start+k] 
                temp=temp[::-1]  
                new+=temp 
                c=-k  
                start+=k 

            else : 
                if c==0 :
                    temp=s[start:start+k] 
                     
                    new+=temp  
                    start+=k   

            
        if s[start:] : 
            if c>0 :
                new+=s[start:][::-1] 
            else :
                new+=s[start:] 
                
        return new



        