from copy import deepcopy
from itertools import combinations
from typing import Dict, List


class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        d = {}
        for i in range(len(letters)):
            if letters[i] not in d:
                d[letters[i]] = 1
            else:
                d[letters[i]] += 1

        print(d)

        max_score = 0
        combis = []
        for i in range(1, len(words)+1):
            combis.extend(combinations(words, i))
        for combi in combis:
            max_score = max(max_score, self._score_word(''.join(combi), d, score))
        return max_score

    def _score_word(self, word: str, d: Dict[str, int], scores: List[int]) -> int:
        d = deepcopy(d)
        score = 0
        for letter in word:
            has_count = d.get(letter, 0)
            if not has_count:
                return 0
            d[letter] -= 1
            score += scores[ord(letter)-97]
        return score
