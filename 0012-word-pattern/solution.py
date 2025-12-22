class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool: 
        if len(pattern)!=len(list(s.split())) :
            return False 

        map_p={} 
        map_s={} 

        for ss,pp in zip(list(s.split()),pattern) :
            if ss in map_s : 
                if map_s[ss]!=pp  :
                    return False 
            else : #new entry 
                if pp in map_p : 
                    return False 
                map_p[pp]=ss 
                map_s[ss]=pp 

        return True

        