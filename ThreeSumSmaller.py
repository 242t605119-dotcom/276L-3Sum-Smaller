class Solution:
    def threeSumSmaller(self, nums, target):
        nums.sort()
        count = 0
        n = len(nums)

        for i in range(n - 2):
            left = i + 1
            right = n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < target:
                    count += right - left
                    left += 1
                else:
                    right -= 1

        return count
