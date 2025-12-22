class Solution:
    def reverseWords(self, s: str) -> str: 
        lst=list(s.split()) 

        for i in range(len(lst)) :
            lst[i]=lst[i][::-1] 

        return " ".join(lst)
        