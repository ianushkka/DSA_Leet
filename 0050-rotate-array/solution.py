from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None: 
        c=k 
        while c!=0 :
            a=nums.pop() 
            c-=1 
            nums.insert(0,a) 

        
       