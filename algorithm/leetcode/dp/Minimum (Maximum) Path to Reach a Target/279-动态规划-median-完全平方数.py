"""

给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。

示例 1:

输入: n = 12
输出: 3 
解释: 12 = 4 + 4 + 4.
示例 2:

输入: n = 13
输出: 2
解释: 13 = 4 + 9.

分析:
dp[i]为组成i的最少完全平方数个数 //状态表示
dp[i]=min(dp[i-1]+1,dp[i-4]+1,...dp[i-n]+1) i-n>0
dp[0]=0

"""

class Solution:
    def numSquares(self, n: int) -> int:
        dp=[float('inf')]*(n+1)
        dp[0]=0
        import math
        # 提前计算好，不然会超时
        square_nums = [i**2 for i in range(0, int(math.sqrt(n))+1)]

        for i in range(1,n+1):
            for square in square_nums:
                if square>i:
                    break
                dp[i]=min(dp[i],dp[i-square]+1)
        return dp[n]

if __name__=="__main__":
    s=Solution()
    print(s.numSquares(13))
