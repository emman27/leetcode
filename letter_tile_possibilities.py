import itertools
from typing import List, Set


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        substrings = self._generate_substrings(tiles)
        results = set()
        for substring in substrings:
            for perm in itertools.permutations(substring):
                results.add(perm)
        return len(results) - 1  # The empty string

    def _generate_substrings(self, s: str) -> Set[str]:
        return set(self._generate_substrings_with_prefix(s, ''))

    def _generate_substrings_with_prefix(self, s: str, prefix: str) -> List[str]:
        if not s:
            return [prefix]
        return self._generate_substrings_with_prefix(s[1:], prefix) + self._generate_substrings_with_prefix(s[1:], prefix + s[0])
