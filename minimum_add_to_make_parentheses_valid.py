class Stack():

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def peek(self):
        return self.items[-1] if self.items else None

    def match(self, item):
        return self.items and self.items[-1] == '(' and item == ')'

    def pop(self):
        return self.items.pop()

    def __len__(self):
        return len(self.items)


class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        count = 0
        s = Stack()
        for char in S:
            if s.match(char):
                s.pop()
            else:
                s.push(char)
        return count + len(s)
