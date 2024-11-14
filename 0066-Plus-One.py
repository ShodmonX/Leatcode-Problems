class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        numer = int(''.join(map(str, digits))) + 1
        return [int(i) for i in str(numer)]
    
object = Solution()
print(object.plusOne([1, 2, 3]))
print(object.plusOne([4, 3, 2, 1]))
print(object.plusOne([9]))