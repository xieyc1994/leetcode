class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 1:
            return 0
        ls = []
        for i in range(len(nums)):
            if i == 0:
                ls.append(nums[0])
            elif i == 1:
                ls.append(max(nums[0], nums[1]))
            else:
                ls.append(max(ls[i-1], ls[i-2]+nums[i]))
        return ls[-1]