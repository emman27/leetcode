from typing import Dict, List, Set


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        sets: List[Set] = []
        counts: List[Dict[str, int]] = []
        for word in A:
            sets.append(set(word))
            counts.append(word_to_char_count(word))
        overlapping_characters = sets[0]
        for s in sets:
            overlapping_characters = overlapping_characters & s
        result = []
        for char in overlapping_characters:
            result.extend([char] * min(map(lambda d: d.get(char), counts)))
        return result


def word_to_char_count(word: str) -> Dict[str, int]:
    d: Dict[str, int] = {}
    for char in word:
        d[char] = d.get(char, 0) + 1
    return d
