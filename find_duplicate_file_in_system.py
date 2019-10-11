from typing import List


class File():
    def __init__(self, name: str, content: str, path: str):
        self.name = name
        self.content = content
        self.path = path

    @classmethod
    def from_str(cls, s: str, path: str) -> 'File':
        parts = s.split('(')
        return cls(parts[0], parts[1][:-1], path)

    def full_name(self) -> str:
        return f'{self.path}/{self.name}'


class Directory():
    def __init__(self, path: str, files: List[File]):
        self.path = path
        self.files = files

    @classmethod
    def from_str(cls, s: str) -> 'Directory':
        parts = s.split(' ')
        path = parts[0]
        return cls(path, [File.from_str(f, path) for f in parts[1:]])


class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        files = {}
        for path in paths:
            d = Directory.from_str(path)
            for f in d.files:
                files[f.content] = files.get(f.content, []) + [f]
        result = []
        for file_group in files.values():
            if len(file_group) > 1:
                result.append([f.full_name() for f in file_group])
        return result
