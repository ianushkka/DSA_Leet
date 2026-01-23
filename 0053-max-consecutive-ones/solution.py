from typing import List
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int: 
        cur_ones=0 
        max_ones=0 

        for i in range(len(nums)) : 
            if nums[i]==1 :
                cur_ones+=1  
                if cur_ones>max_ones : 
                    max_ones=cur_ones 

            else :
                cur_ones=0 #re-initialize bcs sequence ended  
            
        return max_ones


         