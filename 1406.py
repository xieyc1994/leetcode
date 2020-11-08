class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        L = len(stoneValue)
        dp = [0] * 3
        ans = - 2 ** 23
        
        cum_sum = copy.copy(stoneValue)
        for i in range(1, len(cum_sum)):
            cum_sum[i] += cum_sum[i-1]
        cum_sum.append(0)
        
        for i in range(L-1, -1, -1):
            ans = - 2 ** 23
            for x in range(min(3, L-i)):
                ans = max(cum_sum[i+x]-cum_sum[i-1] + cum_sum[-2]-cum_sum[i+x] - dp[x], ans)
            dp[0], dp[1], dp[2] = ans, dp[0], dp[1] 

        return "Alice" if ans * 2 > cum_sum[-2] else "Tie" if ans*2 == cum_sum[-2] else "Bob"