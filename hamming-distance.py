class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x_str = bin(x).replace('0b', '').rjust(31, '0')
        y_str = bin(y).replace('0b', '').rjust(31, '0')
        count = 0
        for i in range(len(x_str)):
            if x_str[i] != y_str[i]:
                count += 1
        return count
