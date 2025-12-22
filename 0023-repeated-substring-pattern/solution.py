class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        length=1
        sample="" 

        while length<=len(s)//2 :
            while len(sample)<len(s) :
                sample+=s[:length]  

            if sample==s :
                return True

            length+=1 
            sample=""

        return False