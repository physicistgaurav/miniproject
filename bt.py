
class _Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
# Individual node of binary tree


class BinaryTree:
    def __init__(self):
        self._root = None
# Initialized and makes root none

    def add_root(self, key):
        if self._root is None:
            self._root = _Node(key)
        return False
        # Adds root if no root, and if there return false

# To return inorder traversal using recursion
    def inorder_walk(self):
        walk = list()
        self._inorder_walk(self._root,  walk)
        return walk

    def _inorder_walk(self, node, walk):
        if node is None:
            return
        self._inorder_walk(node.left, walk)
        walk.append(node.key)
        self._inorder_walk(node.right, walk)

        return walk

    # To return preorder traversal using recursion

    def preorder_walk(self):
        walk = list()
        self._preorder_walk(self._root,  walk)
        return walk

    def _preorder_walk(self, node, walk):
        if node is None:
            return
        walk.append(node.key)
        self._preorder_walk(node.left, walk)
        self._preorder_walk(node.right, walk)

        return walk

# To Print tree
    def printTree(self):
        node = self._root
        if node is not None:
            self._printTree(node, level=0)

    def _printTree(self, node, level=0):
        if node is not None:
            self._printTree(node.right, level + 1)
            print(' ' * 4 * level + '-> ' + str(node.key))
            self._printTree(node.left, level + 1)

    def size(self):
        return self._size
