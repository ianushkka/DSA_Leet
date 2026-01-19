from typing import List
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:   
        #in-place-solution   

        start=0 
        for i in range(1,len(nums)) :
            if nums[start]%2!=0 :  
                if nums[i]%2==0 :
                    temp=nums[start] #odd in temp 
                    nums[start]=nums[i] 
                    nums[i]=temp  #odd pushed back  
                    start+=1 

            else : #start already even ,no need just inc 
                start+=1 
        
        return nums




                 


        