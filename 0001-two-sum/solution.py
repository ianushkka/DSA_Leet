from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        n=len(nums)
        seen={} 
        for i in range(n) :
            if target-nums[i] in seen :
                index1=seen[target-nums[i]]
                index2=i 
                break 
            
            else :
                seen[nums[i]]=i 

        return list((index1,index2))
            