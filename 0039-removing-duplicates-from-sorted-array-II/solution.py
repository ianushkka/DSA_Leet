from typing import List 
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int: 

        start=0 

        for i in range(1,len(nums)) :  
            if i==1 and nums[i]==nums[0] : 
                start+=1 

            else :    
                if nums[start]==nums[i] :   
                    if nums[start-1]!=nums[start] : 
                        nums[start+1]=nums[i] 
                        start+=1  #allowed 

                else : #differnt 
                    nums[start+1]=nums[i] 
                    start+=1 

        return start+1

                
            

            
                

        