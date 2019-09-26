from typing import List


class Range():
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def __len__(self) -> int:
        return self.end - self.start + 1

    def contains(self, other) -> bool:
        if not other:
            return False
        return self.start <= other.end and other.start <= self.end

    def combine(self, other):
        return Range(min(self.start, other.start), max(self.end, other.end))

    def __repr__(self) -> str:
        return f'({self.start}, {self.end})'


class Stack():
    def __init__(self):
        self.items = []

    def peek(self):
        return self.items[-1] if self.items else None

    def pop(self):
        return self.items.pop()

    def push(self, item):
        self.items.append(item)


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        letters = set(S)
        ranges = []
        for letter in letters:
            new_range = Range(S.index(letter), S.rindex(letter))
            ranges.append(new_range)
        ranges.sort(key=lambda r: r.start)
        stack = Stack()
        for r in ranges:
            if r.contains(stack.peek()):
                stack.push(r.combine(stack.pop()))
            else:
                stack.push(r)
        return [len(r) for r in stack.items]
