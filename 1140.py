class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        hpr = copy.copy(piles)
        for i in range(1, len(hpr)):
            hpr[i] += hpr[i-1]
        hpr.append(0)
        
        @lru_cache(maxsize=None)
        def dp(i, m):
            ans = 0
            if len(piles)-i <= 2 * m:
                return hpr[-2]-hpr[i-1]
            for x in range(2*m):
                j = i+x
                cur = (hpr[j]-hpr[i-1]) + (hpr[-2]-hpr[j]) - dp(j+1, max(x+1, m))
                ans = max(ans, cur)
            return ans
        
        return dp(0, 1)