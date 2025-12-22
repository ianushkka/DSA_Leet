from typing import List
class Solution:
    def findWords(self, words: List[str]) -> List[str]: 
        d={} 
        for i in "qwertyuiop" :
            d[i]=1 
        for i in "asdfghjkl" :
            d[i]=2
        for i in "zxcvbnm" :
            d[i]=3  

        ans=[]
        for word in words :
            row=d[word.lower()[0]] 
            flag=True 
            for i in word.lower() : 
                if d[i]!=row : 
                    flag=False
                    break  

            if flag : 
                ans.append(word) 
        return ans

                