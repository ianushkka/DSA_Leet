from typing import List 
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """ 

        i=-1 
        index1=None 
        while i>=-len(nums)+1 :
            if nums[i]>nums[i-1] :  
                index1=i
                break   
            i-=1 

        if index1==None :
            nums.reverse() 
            return 

        index2=index1-1 #Main point where level change is to be applied   

        for i in range(len(nums)-1,index2,-1) : #index2 not included 
            if nums[i]>nums[index2] :
                index3=i  
                break 
        
        nums[index2],nums[index3]=nums[index3],nums[index2] 

        nums[index2+1:]=reversed(nums[index2+1:]) 


            


        

        