from typing import List
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:  
            numbers=sorted(nums) 
            prod1=numbers[0]*numbers[1]*numbers[-1] 
            prod2=numbers[-1]*numbers[-2]*numbers[-3]  

            return max(prod1,prod2) 