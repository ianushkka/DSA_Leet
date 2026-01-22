from typing import List 
class Solution:
    def check(self, nums: List[int]) -> bool:  

        brk=None
        for i in range(1,len(nums)) :
            if nums[i]<nums[i-1] : #split-point 
                brk=i
                break 

        
        c=0 
        cpy=nums.copy() 

        if brk!=None :
            while c!=brk  : #rotate till brk 
                cpy.pop(0) 
                cpy.append(nums[c]) 
                c+=1  
                print(cpy)

            for i in range(1,len(cpy)) :
                if cpy[i]<cpy[i-1] : 
                    return False 

            return True 

        else :
            return True




        