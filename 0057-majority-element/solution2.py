from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int: 
        elem=None 
        count=0 

        for i in nums :
            if count==0 :
                elem=i 
                count+=1  
                continue 

            if i==elem :
                count+=1 
            else :
                count-=1 

        return elem
        