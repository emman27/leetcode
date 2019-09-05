from subdomain_visit_count import _all_subdomains


def test_all_subdomains():
    assert ['discuss.leetcode.com', 'leetcode.com', 'com'] == _all_subdomains('discuss.leetcode.com')
    assert ['wiki.org', 'org'] == _all_subdomains('wiki.org')
