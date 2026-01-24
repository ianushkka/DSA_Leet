from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None: 
        start=0 
        for i in range(len(nums)) :
            if nums[i]==0 :
                nums[start],nums[i]=nums[i],nums[start]  
                start+=1 

        #start points to the index next to last zero 
        #so count of zeroes is exactly as start basically 

        for i in range(start,len(nums)) : 
            if nums[i]==1 :
                nums[start],nums[i]=nums[i],nums[start]  
                start+=1 
             

        