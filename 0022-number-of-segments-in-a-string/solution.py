class Solution:
    def countSegments(self, s: str) -> int: 
        if s=="" :
            return 0
        lst=s.split() 
        #lst=[i for i in lst if i!=""]
        return len(lst)        