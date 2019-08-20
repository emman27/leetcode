from typing import List


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        self_dividing_numbers = []
        for i in range(left, right+1):
            self._append_if_self_dividing(i, self_dividing_numbers)
        return self_dividing_numbers

    def _append_if_self_dividing(self, num: int, arr: List[int]):
        if self._is_self_dividing(num):
            arr.append(num)
        return arr

    def _is_self_dividing(self, num: int):
        for digit in self._digits(num):
            if digit == 0 or num % digit != 0:
                return False
        return True

    def _digits(self, num: int):
        return map(lambda s: int(s), str(num))
