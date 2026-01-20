from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int: 

        min_price=prices[0] 
        max_profit=0
        cur_profit=0 

        for i in range(1,len(prices)) :
            cur_profit=prices[i]-min_price  

            if cur_profit>max_profit :
                max_profit=cur_profit 

            min_price=min(min_price,prices[i])  

        return max_profit 
    
    
         