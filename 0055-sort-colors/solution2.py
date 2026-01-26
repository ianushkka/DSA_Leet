from typing import List 
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """ 
        left=0 
        r=len(nums)-1 
        i=0 

        while i<=r :
            if nums[i]==0 :
                nums[left],nums[i]=nums[i],nums[left] 
                i+=1 
                left+=1 
            elif nums[i]==2 : 
                nums[r],nums[i]=nums[i],nums[r] 
                r-=1   

            else :
                i+=1

    
                
                
         