class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for ele in s:
            if not stack:
                stack.append(ele)
            elif ele == stack[-1]:
                stack.pop()
                continue
            else :
                stack.append(ele)
        return "".join(stack)