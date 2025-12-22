class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool: 

        if len(s)!=len(t) :
            return False 

        map_st={} 
        map_ts={} 

        for ss,tt in zip(s,t) :
            if ss in map_st :
                if map_st[ss]!=tt :
                    return False

            #if it is a new entry ,we cross check 
            else : #only when ss is a new entry !
                if tt in map_ts : #But before pairing ss with tt , we have to check how honest tt has been ,, if tt has already appeared ,,obv its not withh ss ,, and some other ,, so bang a red flag !! 

                    return False
                    

                map_st[ss]=tt 
                map_ts[tt]=ss 

        return True


        