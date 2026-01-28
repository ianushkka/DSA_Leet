from typing import List 
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """ 

        cpy=[i[::] for i in matrix]

        for i in range(len(matrix)) :
            for j in range(len(matrix[0])) :
                if cpy[i][j]==0  :  
                    for c in range(len(matrix[0]))  : 
                        matrix[i][c]=0 

                    for q in range(len(matrix)) :
                        matrix[q][j]=0 

        





                   