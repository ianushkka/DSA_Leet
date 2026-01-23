from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None: 
        start=0 
        for i in range(len(nums)) :
            if nums[i]!=0 :
                temp=nums[start] 
                nums[start]=nums[i] 
                nums[i]=temp  
                start+=1

        return nums
        