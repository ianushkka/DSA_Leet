from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:  

        total=len(matrix)*len(matrix[0])   
        ans=[]   

        rowstart=0 
        rowend=len(matrix)-1 
        colstart=0 
        colend=len(matrix[0]) -1 

        while len(ans)!=total :  
            
            for i in range(colstart,colend+1) :
                ans.append(matrix[rowstart][i])  
            rowstart+=1

            if len(ans)==total :
                break  

            for i in range(rowstart,rowend+1) :
                ans.append(matrix[i][colend])  
            colend-=1 

            if len(ans)==total :
                break   

            for i in range(colend,colstart-1,-1) :
                ans.append(matrix[rowend][i]) 
            rowend-=1  

            if len(ans)==total :
                break  

            for i in range(rowend,rowstart-1,-1) :
                ans.append(matrix[i][colstart]) 
            colstart+=1 

        return ans



            

            


         