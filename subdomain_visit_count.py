from typing import Dict, List, Tuple


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domains: Dict[str, int] = {}
        for cpdomain in cpdomains:
            count, domain = self._split(cpdomain)
            for subdomain in _all_subdomains(domain):
                domains[subdomain] = domains.get(subdomain, 0) + count
        result = []
        for subdomain, count in domains.items():
            result.append("{} {}".format(count, subdomain))
        return result

    def _split(self, cpdomain: str) -> Tuple[int, str]:
        parts = cpdomain.split(' ')
        return int(parts[0]), parts[1]


def _all_subdomains(fqdn: str) -> List[str]:
    parts = fqdn.split('.')
    results = []
    for i in range(len(parts)):
        results.append('.'.join(parts[i:]))
    return results
