from typing import List 
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]: 
        d1={} 
        for i in range(len(list1)) :
            if list1[i] not in d1 :
                d1[list1[i]]=i 
            
        lst=[]
        minimum=len(list1)+len(list2) 
        for i in range(len(list2)) : 
            if list2[i] in d1 :
                if minimum>d1[list2[i]] + i  :
                    minimum=d1[list2[i]] + i   
                    lst.clear() 
                    lst.append(list2[i])
                    
                elif minimum==d1[list2[i]] + i   : 
                    lst.append(list2[i])


        return lst


        