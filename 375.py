class Solution:
    def getMoneyAmount(self, n: int) -> int:
        results = {}
        def dp(a, b):
            if (a, b) in results:
                return results[(a, b)]
            if a >= b:
                return 0
            min_value = 40000
            for i in range(a, b+1):
                min_value = min(max(dp(a, i-1), dp(i+1, b)) + i, min_value)
            results[(a, b)] = min_value
            return min_value
        return dp(1, n)