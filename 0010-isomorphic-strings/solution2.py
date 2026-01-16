class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool: 
        if len(s)!=len(t) :
            return False  
        
        dict1={} 

        for i in range(len(s)) :
            if s[i] not in dict1 :  
                dict1[s[i]]=[i] 

            else : 
                dict1[s[i]].append(i) 

        dict2={} 
        for i in range(len(t)) :
            if t[i] not in dict2 :  
                dict2[t[i]]=[i] 

            else : 
                dict2[t[i]].append(i)  

        return list(dict1.values())==list(dict2.values())



        
        