import string
from typing import List

MAX_LINE_LENGTH = 100


class Lines():
    def __init__(self, char_lengths: List[int]):
        self.lines = 0
        self.length = 0
        self._char_lengths = char_lengths

    def push(self, char: str):
        char_length = self._char_lengths[string.ascii_lowercase.index(char)]
        new_length = self.length + char_length
        if new_length > MAX_LINE_LENGTH:
            self.lines += 1
            self.length = 0
        self.length += char_length


class Solution:
    def numberOfLines(self, widths: List[int], S: str) -> List[int]:
        lines = Lines(widths)
        for c in S:
            lines.push(c)
        return [lines.lines + 1, lines.length]
