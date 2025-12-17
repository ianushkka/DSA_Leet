from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        start=0 
        i=1 

        while i<len(nums) :
            if nums[start]==nums[i] :
                i+=1  

            else : #fresh-number-found
                nums[start+1]=nums[i] 
                start+=1
                i+=1
                
        return start+1
        
