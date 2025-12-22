class Solution:
    def reverseVowels(self, s: str) -> str:
         
        left=0 
        right=len(s)-1 
        lst=list(s)
        while left<right :
            if lst[left] not in {"a","e","i","o","u","A","E","I","O","U"} :
                #if right-left>2 :
                    left+=1 
                    continue

            if lst[right] not in {"a","e","i","o","u","A","E","I","O","U"} :
                #if right-left>2 :
                    right-=1  
                    continue 

            temp=lst[left]
            lst[left]=lst[right] 
            lst[right]=temp

            left+=1 
            right-=1 

        return "".join(lst)



            
