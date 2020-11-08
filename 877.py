class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        def p2(i, j):
            return sm[j] - sm[i-1] - helper(i, j)
        
        @lru_cache(maxsize=None)
        def helper(i, j):
            if i == j:
                return piles[i]
            return max((piles[i]+p2(i+1,j)), (piles[j]+p2(i,j-1)))
            pass
        
        sm = copy.copy(piles)
        
        for i in range(1, len(sm)):
            sm[i] += sm[i-1]
        sm.append(0)
        
        return helper(0, len(piles)-1) > sm[-2] / 2