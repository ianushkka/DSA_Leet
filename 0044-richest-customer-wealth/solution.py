from typing import List
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int: 

        max_wealth=0 
        

        for i in range(len(accounts)) :
            cur_wealth=0
            for j in range(len(accounts[i])) : 
                cur_wealth+=accounts[i][j] 

            if cur_wealth>max_wealth : 
                max_wealth=cur_wealth 

        return max_wealth
                
