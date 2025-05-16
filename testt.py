class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

root = Node('A')
root.left = Node('b')
root.right = Node('c')
root.left.left = Node('d')
root.left.right = Node('e')


def print_tree_priorder(node):
    if node is not None:
        print(node.value)
        print_tree_priorder(node.left)
        print_tree_priorder(node.right)

print_tree_priorder(root)