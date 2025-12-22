import string 
s=string.ascii_uppercase 
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res=""
        while columnNumber>0 :
            columnNumber-=1 

            res+=s[columnNumber%26] 
            columnNumber//=26 

        r=res[-1::-1] 
        return r


            
            

        