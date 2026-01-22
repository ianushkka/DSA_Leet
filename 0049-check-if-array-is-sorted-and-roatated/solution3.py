from typing import List 
class Solution:
    def check(self, nums: List[int]) -> bool:  
        
        brks=0 
        for i in range(1,len(nums)) :
            if nums[i]<nums[i-1] :
                if brks==0 :
                    brk_point=i 

                brks+=1 

                if brks>1 :
                    return False  

        if brks :
            if nums[0]>=nums[-1] :
                return True 

            else :
                return False 

        else :
            return True 
         