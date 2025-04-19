class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumeric_characters = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        s = s.lower()
        rs = ""
        for i in s:
            if i in alphanumeric_characters:
                rs += i
        result = True
        for i in range(len(rs)//2):
            if rs[i] != rs[len(rs)-1-i]:
                result = False
                break

        return result
