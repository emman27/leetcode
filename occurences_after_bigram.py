from typing import List


class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        split = text.split(' ')
        first_indexes = []
        second_indexes = []
        third_words = []
        for (i, word) in enumerate(split):
            if word == first:
                first_indexes.append(i)
            if word == second:
                second_indexes.append(i)
        for idx in first_indexes:
            try:
                second_indexes.index(idx + 1)
                third_words.append(split[idx + 2])
            except ValueError:
                pass
            except IndexError:
                pass
        return third_words
