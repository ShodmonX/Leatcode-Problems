class Solution:
    def romanToInt(self, s: str) -> int:
        char = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        res = char[s[-1]]
        for i in range(1, len(s)):
            if char[s[i-1]] < char[s[i]]:
                res -= char[s[i-1]]
            else:
                res += char[s[i-1]]
        
        return res
    
object = Solution()
print(object.romanToInt('III'))
print(object.romanToInt('LVIII'))
print(object.romanToInt('MCMXCIV'))