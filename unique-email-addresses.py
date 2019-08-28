from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        return len(set(map(self._remove_plus, map(self._remove_fullstop, emails))))

    def _remove_fullstop(self, email: str) -> str:
        parts = email.split('@')
        return f"{parts[0].replace('.', '')}@{parts[1]}"

    def _remove_plus(self, email: str)->str:
        parts = email.split('@')
        return f"{parts[0].split('+')[0]}@{parts[1]}"
