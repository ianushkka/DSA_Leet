class Solution:
    def isPalindrome(self, s: str) -> bool:

        another=[] 
        for i in s :
            if i.isalnum() :
                another.append(i.lower()) 

        return another==another[-1::-1]

        
        
        