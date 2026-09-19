class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class BinaryTree:
    def __init__(self):
        self.root = None
    def print_tree(self):
        if self.root is None:
            return
        queue = []
        queue.append(self.root)
        while len(queue) > 0:
            print(queue[0].data)
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


tree = BinaryTree()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print("Binary Tree Before Mirroring")
tree.print_tree()
def mirror_tree(root):
    if root is None:
        return
    mirror_tree(root.left)
    mirror_tree(root.right)
    root.left, root.right = root.right, root.left

mirror_tree(tree.root)

print("\nBinary Tree After Mirroring")
tree.print_tree()
