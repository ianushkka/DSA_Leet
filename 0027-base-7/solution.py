class Solution:
    def convertToBase7(self, num: int) -> str:
        sign=False 
        if num<0 :
            sign=True 
            num=-(num)

        lst=[]
        if num==0 :
            return "0" 
            
        while num>0 : 
            lst.append(str(num%7)) 
            num//=7 

        lst.reverse() 
        if sign :
            return '-'+"".join(lst)
        
        return "".join(lst)

        