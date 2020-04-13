"""给定一个方形整数数组 A，我们想要得到通过 A 的下降路径的最小和。

下降路径可以从第一行中的任何元素开始，并从每一行中选择一个元素。在下一行选择的元素和当前行所选元素最多相隔一列。

 

示例：

输入：[[1,2,3],[4,5,6],[7,8,9]]
输出：12
解释：
可能的下降路径有：
[1,4,7], [1,4,8], [1,5,7], [1,5,8], [1,5,9]
[2,4,7], [2,4,8], [2,5,7], [2,5,8], [2,5,9], [2,6,8], [2,6,9]
[3,5,7], [3,5,8], [3,5,9], [3,6,8], [3,6,9]
和最小的下降路径是 [1,4,7]，所以答案是 12。

分析:
dp[i][j]表示i,j位置的最小下降和 //状态表示
dp[i][j]=min(dp[i-1][j-1],dp[i-1][j],dp[i-1][j+1])+A[i][j]// 状态转移
dp[0][j]=A[0][j]

"""
class Solution:
    def minFallingPathSum(self, A) -> int:
        m=len(A)
        n=len(A[0])
        dp=[[float('inf')]*m for _ in range(n)]

        for j in range(n):
            dp[0][j]=A[0][j]

        for i in range(1,m):
            for j in range(n):
                left=dp[i-1][j-1] if j-1>=0 else float('inf')
                right=dp[i-1][j+1] if j+1<=n-1 else float('inf')
                dp[i][j]=min(left,dp[i-1][j],right)+A[i][j]
        
        return min([dp[m-1][item] for item in range(0,n)])
    
if __name__=="__main__":
    s=Solution()
    A=[[1,2,3],[4,5,6],[7,8,9]]
    print(s.minFallingPathSum(A))

                
