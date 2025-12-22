class Solution:
    def isValid(self, s: str) -> bool: 

        #if s.count("(")!=s.count(")") or s.count("[")!=s.count("]") or s.count("{")!=s.count("}") :
            #return False 

        d={ ")" : "(" , "}" : "{" , "]" : "[" }   
        lst=[]

        for i in s :
            if i in "([{" :
                lst.append(i) 

            else : #a closing one 
                if not lst :
                    return False 
                if d[i]!=lst[-1] : #first check if list has something 
                    return False 
                
                lst.pop()   

                
        
        return  not lst


        