from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:  

        min_price=prices[0]   
        cur_profit=0 
        res=0 

        for i in range(1,len(prices)) :
            cur_profit=prices[i]-min_price 
            if cur_profit>0 :
                res+=cur_profit  
                min_price=prices[i]  #assuming we purchased on same day of sale
                #even if it is a bad purchase , next day cur_prof will be negative hence else code will be run and will set min_price of stock min of both ie prices[i] 

            else:
                min_price=min(min_price,prices[i]) 

        return res
        

        