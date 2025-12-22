class Solution:
    def lengthOfLastWord(self, s: str) -> int:
       
        # if len(s.strip())==1 :
        #    return 1

        count=0
        for i in range(-1,-(len(s.strip())+1),-1) :
            if (s.strip())[i]!=" " :
                count+=1 
            else :
                return count

        else :  #for those cases where its only a single word and loop completes cause there is no space 
            return count   


        