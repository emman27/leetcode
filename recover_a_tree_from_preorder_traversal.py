# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __eq__(self, other):
        if bool(self) != bool(other):
            return False
        return self.val == other.val and self.left == other.left and self.right == other.right

    def __repr__(self):
        return "val: " + str(self.val) + " left: " + str(self.left) + " right: " + str(self.right)


class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        end_of_first_number = len(S)
        try:
            end_of_first_number = S.index('-')
        except ValueError:
            pass
        stack = [TreeNode(int(S[:end_of_first_number]))]
        height = 1
        val = ''
        for c in S[end_of_first_number:]:
            if c == "-" and val == '':
                height += 1
            elif c != "-":
                val += c
            elif len(stack) < height:
                node = TreeNode(int(val))
                stack[-1].left = node
                stack.append(node)
                height = 1
                val = ''
            else:
                while len(stack) > height:
                    stack.pop()
                node = TreeNode(int(val))
                if not stack[-1].left:
                    stack[-1].left = node
                else:
                    stack[-1].right = node
                stack.append(node)
                height = 1
                val = ''
        if val:
            while len(stack) > height:
                stack.pop()
            node = TreeNode(int(val))
            if not stack[-1].left:
                stack[-1].left = node
            else:
                stack[-1].right = node
            stack.append(node)
        return stack[0]
