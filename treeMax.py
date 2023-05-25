class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def preorder(self, node):
        if node is None:
            return []

        result = [node.value]
        result += self.preorder(node.left)
        result += self.preorder(node.right)
        return result

    def inorder(self, node):
        if node is None:
            return []

        result = self.inorder(node.left)
        result.append(node.value)
        result += self.inorder(node.right)
        return result

    def postorder(self, node):
        if node is None:
            return []

        result = self.postorder(node.left)
        result += self.postorder(node.right)
        result.append(node.value)
        return result
# cc16

    def get_max(self):
        if self.root is None:
            raise Exception("Binary tree is empty")

        return self._get_max_helper(self.root)

    def _get_max_helper(self, node):
        if node is None:
            return float("-inf")

        max_value = node.value
        left_max = self._get_max_helper(node.left)
        right_max = self._get_max_helper(node.right)

        if left_max > max_value:
            max_value = left_max
        if right_max > max_value:
            max_value = right_max

        return max_value

