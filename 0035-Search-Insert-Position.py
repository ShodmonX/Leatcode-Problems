from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        end = len(nums)
        start = 0
        while start < end:
            midd = (start + end)//2
            if nums[midd] == target:
                return midd
            elif nums[midd] > target:
                end = midd
            else:
                start = midd + 1

        return start
    