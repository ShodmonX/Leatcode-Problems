class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = strs[0]
        for i in strs[1:]:
            while not i.startswith(prefix):
                prefix = prefix[:-1]
        return prefix

object = Solution()

print(object.longestCommonPrefix(['flower', 'flow', 'flight']))
print(object.longestCommonPrefix(['dog', 'racecar', 'car']))