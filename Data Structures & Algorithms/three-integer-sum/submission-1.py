class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = -nums[i]
            seen = set()
            j = i + 1
            while j < len(nums):
                complement = target - nums[j]
                if complement in seen:
                    ans.append([nums[i], nums[j], complement])
                    while j + 1 < len(nums) and nums[j] == nums[j + 1]:
                        j += 1
                seen.add(nums[j])
                j += 1
        return ans