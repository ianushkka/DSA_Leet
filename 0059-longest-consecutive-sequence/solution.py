from typing import List 
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:  
        if len(nums)==0 :
            return 0

        my_set=set()
        for i in nums :  
            my_set.add(i) 

        
        max_count=float("-inf")
        for i in my_set :  
            if i-1 not in my_set : #makesure we scan from the start of any subsequence we look for 
                c=1
                j=1 
                
                while i+j in my_set :
                    c+=1 
                    j+=1 

                if c>max_count :
                    max_count=c  

        return max_count 


     

            


             

     