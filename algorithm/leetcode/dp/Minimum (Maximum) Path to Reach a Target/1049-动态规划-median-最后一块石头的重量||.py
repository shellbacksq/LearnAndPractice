"""
有一堆石头，每块石头的重量都是正整数。

每一回合，从中选出任意两块石头，然后将它们一起粉碎。假设石头的重量分别为 x 和 y，且 x <= y。那么粉碎的可能结果如下：

如果 x == y，那么两块石头都会被完全粉碎；
如果 x != y，那么重量为 x 的石头将会完全粉碎，而重量为 y 的石头新重量为 y-x。
最后，最多只会剩下一块石头。返回此石头最小的可能重量。如果没有石头剩下，就返回 0。

 

示例：

输入：[2,7,4,1,8,1]
输出：1
解释：
组合 2 和 4，得到 2，所以数组转化为 [2,7,1,8,1]，
组合 7 和 8，得到 1，所以数组转化为 [2,1,1,1]，
组合 2 和 1，得到 1，所以数组转化为 [1,1,1]，
组合 1 和 1，得到 0，所以数组转化为 [1]，这就是最优值。

分析:
每次选两个碰撞，一直到最后一个,可以表示为:
a_1 : b_1
a_2 : b_2
a_3 : b_3
a_4 : b_4
a_5 : b_5

最后的结果就是 (a_1+a_2+a_3+a_4+a_5)-(b-1+b_2+b_3+b_4+b_5)
所以问题就转化为找出最接近(a_*+b_*)/2的一堆石头，那么另一堆也就天然的十分靠近它.

从一堆石头中找出最接近(a_*+b_*)/2，背包问题.

dp[i]定义为重量上限为i的时候所能装载的最多石头重量.//状态定义
dp[i]=max(dp[i-stones[0]]+stones[0],..,dp[i-stones[n]]+stones[n]) //状态转移
dp[0]=0
"""
class Solution:
    def lastStoneWeightII(self, stones) -> int:
        all_weight=0
        for stone in stones:
            all_weight+=stone
        max_capacity=all_weight//2

        dp=[0]*(max_capacity+1)

        for stone in stones:
            for j in range(max_capacity,stone-1,-1):
                dp[j]=max(dp[j],dp[j-stone]+stone)
        
        return all_weight-dp[max_capacity]*2

if __name__=="__main__":
    s=Solution()
    l=[2,7,4,1,8,1]
    print(s.lastStoneWeightII([2,7,4,1,8,1]))
        
