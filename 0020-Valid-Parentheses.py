class Solution:
    def isValid(self, s: str) -> bool:
        br = []
        for i in s:
            if len(br) == 0:
                br.append(i)
            else:
                if br[-1] == '(' and i == ')':
                    br.pop()
                elif br[-1] == '{' and i == '}':
                    br.pop()
                elif br[-1] == '[' and i == ']':
                    br.pop()
                else:
                    br.append(i)
            

        return len(br) == 0             
    
object = Solution()

print(object.isValid('()')) # True
print(object.isValid('()[]{}')) # True
print(object.isValid('(]')) # False
print(object.isValid('([])')) # True
print(object.isValid('([)]')) # False
