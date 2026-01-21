from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int: 

        start=0 
        for i in range(len(nums)) : 
            if nums[i]!=val : 
                temp=nums[start]
                nums[start]=nums[i]  
                nums[i]=temp 
                start+=1 

        return start

        
