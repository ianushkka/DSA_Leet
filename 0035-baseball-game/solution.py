from typing import List 
class Solution:
    def calPoints(self, operations: List[str]) -> int: 
        rec=[] 
        for i in operations : 
            if i=="+" :
                rec.append(rec[-1]+rec[-2])
            elif not i.isalpha() :
                rec.append(int(i)) 
            elif i=="D" :
                rec.append(2*rec[-1]) 
            else :
                rec.pop() 

        return sum(rec)
        