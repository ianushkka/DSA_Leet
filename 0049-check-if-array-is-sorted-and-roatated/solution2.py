from typing import List
class Solution:
    def check(self, nums: List[int]) -> bool: 
        brk=None
        for i in range(1,len(nums))  :
            if nums[i]<nums[i-1] : #breakpoint 
                brk=i   
                break 

        
        if brk!=None : 
            check=nums[brk::]+nums[:brk] 

            for i in range(1,len(check)) :
                if check[i]<check[i-1]  :
                    return False 

            return True 

        else :
            return True
              
         