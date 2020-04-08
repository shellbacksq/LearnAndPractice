"""
数组的每个索引做为一个阶梯，第 i个阶梯对应着一个非负数的体力花费值 cost[i](索引从0开始)。

每当你爬上一个阶梯你都要花费对应的体力花费值，然后你可以选择继续爬一个阶梯或者爬两个阶梯。

您需要找到达到楼层顶部的最低花费。在开始时，你可以选择从索引为 0 或 1 的元素作为初始阶梯。

示例 1:

输入: cost = [10, 15, 20]
输出: 15
解释: 最低花费是从cost[1]开始，然后走两步即可到阶梯顶，一共花费15。
 示例 2:

输入: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
输出: 6
解释: 最低花费方式是从cost[0]开始，逐个经过那些1，跳过cost[3]，一共花费6。

分析:
1. 状态表示:
目标是 "需要找到达到楼层顶部的最低花费". 
dp[i]-->爬到第i个阶梯的最低花费.// 状态表示

dp[i]=min(dp[i-1]+cost[i-1],dp[i-2]+cost[i-2]) // 状态转移

//初始值
dp[0]=0
dp[1]=0
...
dp[i]=0

"""
class Solution:
    def minCostClimbingStairs(self, cost) -> int:
        N=len(cost)
        dp=[0]*(N+1)
        if len(cost)<3:
            return 0
        for i in range(2,N+1):
            dp[i]=min(dp[i-1]+cost[i-1],dp[i-2]+cost[i-2])    
        return dp[N]

if __name__=='__main__':
    s=Solution()
    # cost=[10, 15, 20]
    cost=[1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    print(s.minCostClimbingStairs(cost))
