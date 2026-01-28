from typing import List 
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """ 
     
        #SECOND BRUTE FORCE METHOD 

        for row in range(len(matrix)) :
            for col in range(len(matrix[0])) :  
                if matrix[row][col]==0 :

                    # marking cols 
                    for i in range(len(matrix[0])) :
                        if matrix[row][i]!=0 :
                            matrix[row][i]="a"  

                    # marking rows 

                    for i in range(len(matrix)) :
                        if  matrix[i][col]!=0 :
                            matrix[i][col]="a" 


        for i in range(len(matrix)) :
            for j in range(len(matrix[0])) :
                if matrix[i][j]=="a" : 
                    matrix[i][j]=0 




 