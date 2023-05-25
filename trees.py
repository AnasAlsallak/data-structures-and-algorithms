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


class BinarySearchTree(BinaryTree):
    def add(self, value):
        new_node = Node(value)
    
        if self.root is None:
            self.root = new_node
        else:
            current = self.root
            
            while True:
                if value < current.value:
                    if current.left is None:
                        current.left = new_node
                        break
                    else:
                        current = current.left
                elif value > current.value:
                    if current.right is None:
                        current.right = new_node
                        break
                    else:
                        current = current.right
                else:
                    raise ValueError("Node with the same value already exists in the Binary Search Tree.")

    def contains(self, value):
        if self.root is None:
            raise ValueError("Binary Search Tree is empty.")

        current = self.root
        
        while current:
            if value == current.value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        
        return False
