class Solution:
    def checkRecord(self, s: str) -> bool: 
        if s.count("A")>=2 :
            return False 
        
        late=0
        for i in s :
            if i=="L" : 
                late+=1 
            else :
                late=0  

            if late==3 :
                return False 
            #alternative for above block 
            #if "LLL" in s :
                #return False 
        return True

        