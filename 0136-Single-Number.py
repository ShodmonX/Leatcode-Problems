from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        numbers = []
        for i in nums:
            if i in numbers:
                numbers.remove(i)
            else:
                numbers.append(i)

        return numbers[0]