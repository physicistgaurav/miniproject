
from bt import BinaryTree, _Node


def buildBinaryTree(pre_order, in_order, bt):
    # Definiing Binary tree with arguments preorder, inorder and binary tree
    bt.add_root(pre_order[0])
    # Add root in the binary tree
    root = bt._root
    # take the root element
    root_index = in_order.index(pre_order[0])
    root.left = helper(
        pre_order[1:root_index+1], in_order[:root_index])
    # Place to the left of the root
    root.right = helper(
        pre_order[root_index+1:], in_order[root_index+1:])
    # place to the right of the root
    return root


def helper(pre_order, in_order):
    # use in recursion similar work as buildBinaryTree function
    if not pre_order or not in_order:
        return None
    root = _Node(pre_order[0])
    root_index = in_order.index(pre_order[0])
    root.left = helper(
        pre_order[1:root_index+1], in_order[:root_index])
    root.right = helper(
        pre_order[root_index+1:], in_order[root_index+1:])
    return root


def main():
    pre_order = [1, 2, 4, 8, 9, 10, 11, 5, 3, 6, 7]
    in_order = [8, 4, 10, 9, 11, 2, 5, 1, 6, 3, 7]
    bt = BinaryTree()
    buildBinaryTree(pre_order, in_order, bt)
    print(f"{bt.preorder_walk()=}")
    print(f"{bt.inorder_walk()=}")
    print(bt.printTree())


if __name__ == "__main__":
    main()
