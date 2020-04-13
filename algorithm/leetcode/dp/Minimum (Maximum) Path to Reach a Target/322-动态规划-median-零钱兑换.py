"""给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

示例 1:

输入: coins = [1, 2, 5], amount = 11
输出: 3 
解释: 11 = 5 + 5 + 1
示例 2:

输入: coins = [2], amount = 3
输出: -1

分析:
dp[i]表示凑成总金额i时所用的最少硬币个数.//状态定义

dp[i]=min(dp[i-coins[0]]+1,dp[i-coins[1],...,dp[i-coins[n]]+1]//状态转移

dp[coin[0]]=1,..dp[coins[n]]=1,

dp[j]=-1(j<coins[0])
"""

class Solution:
    def coinChange(self, coins, amount: int) -> int:
        n=len(coins)

        dp=[float('inf')]*(amount+1)
        dp[0]=0

        
        for c in coins:
            for i in range(amount+1):
                if i>=c:
                    dp[i]=min(dp[i],dp[i-c]+1)
        
        return dp[amount] if dp[amount]!=float('inf') else -1

if __name__=='__main__':
    s=Solution()
    coins = [1, 2, 5]
    amount = 11
    print(s.coinChange(coins,amount))
