class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        start=0 
        while len(haystack)-start>=len(needle) :
            if haystack[start:start+len(needle)]==needle :
                return start 
            start+=1

        return -1