class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        map = {}

        for i in range(len(nums)):
            needed = target - nums[i]

            if needed in map:
                return [map[needed], i]

            map[nums[i]] = i

        return []
