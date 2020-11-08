class Solution:
    def minScoreTriangulation(self, A: List[int]) -> int:
        @lru_cache(maxsize=None)
        def dp(i, j):
            #the min score I can get given nodes from i~j (a sub polygon)
            if i >= j-1:
                return 0
            ans = float(inf)
            for k in range(i+1, j):
                ans = min(ans, A[i]*A[j]*A[k] + dp(i,k) + dp(k,j))
            return ans
        
        return dp(0, len(A)-1)