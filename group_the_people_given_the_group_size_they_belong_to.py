from typing import Dict, List


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        group_sizes_to_people: Dict[int, List[int]] = {}
        for person, size in enumerate(groupSizes):
            if size not in group_sizes_to_people:
                group_sizes_to_people[size] = []
            group_sizes_to_people[size].append(person)
        answer = []
        for key, value in group_sizes_to_people.items():
            while group_sizes_to_people[key]:
                new_group = []
                for i in range(key):
                    person = group_sizes_to_people[key].pop()
                    new_group.append(person)
                answer.append(new_group)
        return answer
