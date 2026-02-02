from typing import List 
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int: 

        count=0  
        cur_sum=0 


        dct={0:1} 

        for i in range(len(nums)) : 
            cur_sum+=nums[i] 

            if cur_sum-k in dct :   #We check if we can remove a previously calculated part , so that sum results into target ! 
                count+=dct[cur_sum-k]

            if cur_sum in dct :
                dct[cur_sum]+=1 
            else : 
                dct[cur_sum]=1 

        


        return count  


        