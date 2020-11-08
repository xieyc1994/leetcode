class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        @lru_cache(maxsize=None)
        def dp(i, j ,l, r):
            if i > j:
                return 0
            if i == j:
                return nums[i]*l*r
            ans = 0
            for k in range(i, j+1):
                ans = max(ans, dp(i,k-1,l,nums[k])+dp(k+1,j,nums[k],r)+l*r*nums[k])
            return ans
        
        return dp(0,len(nums)-1,1,1)