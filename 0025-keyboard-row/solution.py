from typing import List
class Solution:
    def findWords(self, words: List[str]) -> List[str]: 

        first=set("qwertyuiop")
        second=set("asdfghjkl") 
        third=set("zxcvbnm") 
        lst=[] 

        for word in words : 
            if set(word.lower()).intersection(first)==set(word.lower()) or set(word.lower()).intersection(second)==set(word.lower()) or set(word.lower()).intersection(third)==set(word.lower()) : 
                lst.append(word)  

        return lst

 
        