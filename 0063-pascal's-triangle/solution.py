from typing import List 
class Solution:
    def generate(self, numRows: int) -> List[List[int]]: 
        res=[[1]]  
        if numRows==1 : 
            return res  

        #res.append([1,1]) 

        for i in range(2,numRows+1) :  
            lst=[1]  
            for j in range(i-2) :  
                lst.append((res[-1])[j]+(res[-1])[j+1])  
 
            lst.append(1)  
            res.append(lst) 

        return res

 

        