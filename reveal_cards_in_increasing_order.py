from typing import List


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        reverse_takeout_order = reversed(sorted(deck))
        results: List[int] = []
        for card in reverse_takeout_order:
            if results:
                last_card = results.pop()
                results.insert(0, last_card)
            results.insert(0, card)
        return results
