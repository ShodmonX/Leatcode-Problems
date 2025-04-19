from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        canditade = nums[0]
        count = 1

        for num in nums[1:]:
            if count == 0:
                canditade = num
                count = 1
            elif canditade == num:
                count += 1
            else:
                count -= 1

        return canditade