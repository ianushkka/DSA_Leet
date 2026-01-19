from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:  

        start=0
        for i in range(1,len(nums)) : 
            if nums[start]!=nums[i] : 
                nums[start+1]=nums[i]  
                start+=1 

    

        return start+1 #as start is index plus one 
        