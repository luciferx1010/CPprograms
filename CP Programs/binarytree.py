class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    if not root:
        root = Node(key)
    else:
        queue = []
        queue.append(root)
        while queue:
            node = queue.pop(0)
            if not node.left:
                node.left = Node(key)
                break
            else:
                queue.append(node.left)
            if not node.right:
                node.right = Node(key)
                break
            else:
                queue.append(node.right)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)

# Example usage
if __name__ == "__main__":
    # Create a complete binary tree
    root = Node(1)
    insert(root, 2)
    insert(root, 3)
    insert(root, 4)
    insert(root, 5)
    insert(root, 6)
    insert(root, 7)

    # Perform inorder traversal to print the tree
    inorder(root)
