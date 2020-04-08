"""给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

示例:

输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。


分析:

状态表示: dp[i][j] --> 在i,j位置的最小和

状态转移: dp[i][j]取决与前面两个阶段,从左边来的dp[i-1][j]和从上面来的dp[i][j-1]
dp[i][j]=min(dp[i-1][j]+cost[i-1][j],dp[i][j-1]+cost[i][j-1])

初始化:
二维dp要对边进行初始化
dp[0][0]=cost[0][0]
dp[0][j]=dp[0][j-1]+cost[0][j-1]
dp[i][0]=dp[i-1][0]+cost[i-1][0]

"""
class Solution:
    def minPathSum(self, grid) -> int:
        m=len(grid)
        n=len(grid[0])

        # dp初始化
        dp=[[0]*n for _ in range(m)]

        dp[0][0]=grid[0][0]
        for i in range(1,m):
            dp[i][0]=dp[i-1][0]+grid[i][0]

        for j in range(1,n):
            dp[0][j]=dp[0][j-1]+grid[0][j]
        
        #状态转移
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]=min(dp[i-1][j],dp[i][j-1])+grid[i][j]
        return dp[m-1][n-1]
        

if __name__=='__main__':
    s=Solution()
    a=[[1,2,3],[4,5,6]]
    print(s.minPathSum(a))