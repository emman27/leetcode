from typing import Dict, List


class Set():
    def __init__(self):
        self.items: List[EquivalenceClass] = []

    def add(self, s: str):
        equiv = EquivalenceClass(s)
        for item in self.items:
            if item == equiv:
                return
        self.items.append(equiv)

    def __len__(self) -> int:
        return len(self.items)


class EquivalenceClass():
    def __init__(self, s: str):
        even = s[::2]
        odd = s[1::2]
        self.odd_dict: Dict[str, int] = {}
        for char in odd:
            self.odd_dict[char] = self.odd_dict.get(char, 0) + 1
        self.even_dict: Dict[str, int] = {}
        for char in even:
            self.even_dict[char] = self.even_dict.get(char, 0) + 1

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, EquivalenceClass):
            return False
        if len(self.odd_dict) != len(other.odd_dict) or len(self.even_dict) != len(other.even_dict):
            return False
        for key, value in self.odd_dict.items():
            if other.odd_dict.get(key) != value:
                return False
        for key, value in self.even_dict.items():
            if other.even_dict.get(key) != value:
                return False
        return True


class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        s = Set()
        for string in A:
            s.add(string)
        return len(s)
