class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:  
        st2=s[::-1]
        lst=[]

        check="" 
        c=0

        for i in range(len(st2)) :
            if st2[i]!="-" :
                check+=st2[i] 
                c+=1 
                if c==k :
                    lst.append(check.upper()) 
                    check="" 
                    c=0 
        if check :
            lst.append(check.upper())

        lst="-".join(lst) 
        lst=lst[::-1]
           
        
        return lst

        