class Coordinate:
    def __init__(self):
        self.x = 0
        self.y = 0

    def apply_move(self, move: str):
        if move == 'U':
            self.y += 1
        elif move == 'D':
            self.y -= 1
        elif move == 'R':
            self.x += 1
        elif move == 'L':
            self.x -= 1

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        coord = Coordinate()
        for move in moves:
            coord.apply_move(move)
        return coord == Coordinate()
