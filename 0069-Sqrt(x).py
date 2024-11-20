class Solution:
    def mySqrt(self, x: int) -> int:
        i = 0
        while i ** 2 < x:
            i += 1
        return i if i ** 2 <= x else i - 1
    
object = Solution()

print(object.mySqrt(4))  # Output: 2
print(object.mySqrt(8))  # Output: 2
