from typing import List


class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if not self.items:
            return None
        return self.items[-1]

    def __str__(self):
        return ''.join(self.items)


class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = Stack()
        for c in S:
            if stack.peek() == c:
                while stack.peek() == c:
                    stack.pop()
            else:
                stack.push(c)
        return str(stack)
