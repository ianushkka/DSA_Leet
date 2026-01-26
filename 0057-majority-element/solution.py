from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:   

        freq={} 

        for i in range(len(nums)) :
            if nums[i] not in freq :
                freq[nums[i]]=1 

            else :
                freq[nums[i]]+=1 

        max_freq=float("-inf")

        for i in freq :
            if freq[i]>max_freq : 
                maj=i 
                max_freq=freq[i] 

        return maj
