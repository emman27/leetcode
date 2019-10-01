from typing import Dict, List


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        pat = self.str_to_values(pattern)
        results: List[str] = []
        for word in words:
            if pat == self.str_to_values(word):
                results.append(word)
        return results

    def str_to_values(self, pattern: str) -> List[int]:
        d: Dict[str, int] = {}
        i = 0
        values: List[int] = []
        for char in pattern:
            if char not in d:
                d[char] = i
                i += 1
            values.append(d[char])
        return values
