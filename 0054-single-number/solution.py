from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int: 

        res=0 
        for i in range(len(nums)) :
            res^=nums[i] 

        return res   #every element repeats twice in array so by property of xor , they get cancelled ie result zero ,, and xor with zero is the number itself , hence only one none repeating number would be left, so we return res
        