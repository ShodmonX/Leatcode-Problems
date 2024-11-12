class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()
        words = s.split(" ")
        lastWord = words[-1]
        length = len(lastWord)
        return length
    
object = Solution()

print(object.lengthOfLastWord("Hello World"))
print(object.lengthOfLastWord("   fly me   to   the moon  "))
print(object.lengthOfLastWord("luffy is still joyboy"))