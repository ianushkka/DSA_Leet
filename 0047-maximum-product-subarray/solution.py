from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:   

        cur_max=nums[0] 
        cur_min=nums[0]   
        res=nums[0]

        for i in range(1,len(nums)) : 
            temp=cur_max
            cur_max=max(cur_max*nums[i],nums[i],cur_min*nums[i]) 
            cur_min=min(temp*nums[i],nums[i],cur_min*nums[i])   
            res=max(res,cur_max) 

        return res



