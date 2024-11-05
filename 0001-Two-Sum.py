class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        indexes = {}
        for i, num in enumerate(nums):
            t = target - num
            if t in indexes:
                return [indexes[t], i]
            
            indexes[num] = i


object = Solution()

print(object.twoSum(nums=[2, 7, 11, 15], target=9))
print(object.twoSum(nums=[3, 2, 4], target=6))
print(object.twoSum(nums=[3, 3], target=6))
