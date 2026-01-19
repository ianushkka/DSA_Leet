from typing import List
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:  
        current=0
        res=[] 
        for i in nums : 
            res.append(current+i) 
            current+=i
        
        return res


        