# Node class that represents each node on the binary search tree
class Node:
    def __init__(self, val=None):
        self.val = val
        self.left_child = None
        self.right_child = None


# Binary search tree class
class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Method to insert a new node in the binary search tree
    def insert(self, val):
        node = Node(val)
        if self.root is None:
            self.root = node
        else:
            current = self.root
            while True:
                if val < current.val:
                    if current.left_child is None:
                        current.left_child = node
                        break
                    else:
                        current = current.left_child
                else:
                    if current.right_child is None:
                        current.right_child = node
                        break
                    else:
                        current = current.right_child

    # Method to traverse the binary search tree in-order (left, root, right)
    def in_order_traversal(self, node, visited):
        if node is None:
            return visited
        visited = self.in_order_traversal(node.left_child, visited)
        visited.append(node.val)
        visited = self.in_order_traversal(node.right_child, visited)
        return visited