from typing import Dict, List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = 0
        char_map = self._word_to_char_map(chars)
        for word in words:
            if self._can_be_formed(word, char_map):
                count += len(word)
        return count

    def _can_be_formed(self, word: str, char_map: Dict[str, int]) -> bool:
        for char, count in self._word_to_char_map(word).items():
            if char_map.get(char, 0) < count:
                return False
        return True

    def _word_to_char_map(self, word: str) -> Dict[str, int]:
        m = {}
        for char in word:
            m[char] = m.get(char, 0) + 1
        return m
