class Stack:
    def __init__(self):
        self._ = []

    def push(self, obj):
        self._.append(obj)

    def pop(self):
        if self._:
            return self._.pop()
        return None

    def size(self):
        return len(self._)


class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        stack = Stack()
        result = ''
        for char in S:
            if char == '(':
                if stack.size() != 0:
                    result += char
                stack.push(char)
            elif char == ')':
                stack.pop()
                if stack.size() != 0:
                    result += char
            else:
                result += char
        return result
