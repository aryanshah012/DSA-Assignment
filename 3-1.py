class TreeNode:
    def __init__(self, x):
        self.val = x
        self.height = 0
        self.size = 1
        self.left = None
        self.right = None

class Solution:
    def insertAVL(self, items, threshold):
        if not items:
            return None

        root = TreeNode(items[0])
        for item in items[1:]:
            root = self._insert(root, item, threshold)
        return root

    def _insert(self, node, key, threshold):
        if not node:
            return TreeNode(key)

        if key < node.val:
            node.left = self._insert(node.left, key, threshold)
        elif key > node.val:
            node.right = self._insert(node.right, key, threshold)
        else:
            return node

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        node.size = 1 + self._get_size(node.left) + self._get_size(node.right)

        balance = self._get_balance(node)
        if balance > threshold:
            if self._get_balance(node.left) >= 0:
                return self._right_rotate(node)
            else:
                node.left = self._left_rotate(node.left)
                return self._right_rotate(node)
        if balance < -threshold:
            if self._get_balance(node.right) <= 0:
                return self._left_rotate(node)
            else:
                node.right = self._right_rotate(node.right)
                return self._left_rotate(node)

        return node

    def deleteNode(self, root, key, threshold):
        if not root:
            return root

        if key < root.val:
            root.left = self.deleteNode(root.left, key, threshold)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key, threshold)
        else:
            if not root.left or not root.right:
                temp = root.left if root.left else root.right
                if not temp:
                    temp = root
                    root = None
                else:
                    root = temp
                del temp
            else:
                temp = self._min_value_node(root.right)
                root.val = temp.val
                root.right = self.deleteNode(root.right, temp.val, threshold)

        if not root:
            return root

        root.height = 1 + max(self._get_height(root.left), self._get_height(root.right))
        root.size = 1 + self._get_size(root.left) + self._get_size(root.right)

        balance = self._get_balance(root)
        if balance > threshold:
            if self._get_balance(root.left) >= 0:
                return self._right_rotate(root)
            else:
                root.left = self._left_rotate(root.left)
                return self._right_rotate(root)
        if balance < -threshold:
            if self._get_balance(root.right) <= 0:
                return self._left_rotate(root)
            else:
                root.right = self._right_rotate(root.right)
                return self._left_rotate(root)

        return root

    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def _get_height(self, node):
        return -1 if not node else node.height

    def _get_size(self, node):
        return 0 if not node else node.size

    def _get_balance(self, node):
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def _right_rotate(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        x.height = 1 + max(self._get_height(x.left), self._get_height(x.right))

        return x

    def _left_rotate(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        x.height = 1 + max(self._get_height(x.left), self._get_height(x.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def order_of_key(self, root, key):
        if not root:
            return 0
        if key <= root.val:
            return self.order_of_key(root.left, key)
        else:
            return 1 + self._get_size(root.left) + self.order_of_key(root.right, key)

    def get_by_order(self, root, k):
        if not root:
            return -1
        left_size = self._get_size(root.left)
        if k < left_size:
            return self.get_by_order(root.left, k)
        elif k > left_size:
            return self.get_by_order(root.right, k - left_size - 1)
        else:
            return root.val

    def find(self, root, key):
        if not root:
            return False
        if root.val == key:
            return True
        if key < root.val:
            return self.find(root.left, key)
        return self.find(root.right, key)

    def print_inorder(self, root):
        if not root:
            return
        self.print_inorder(root.left)
        print(root.val, end=' ')
        self.print_inorder(root.right)

if __name__ == "__main__":
    solution = Solution()
    items = [10, 20, 30, 40, 50, 25]
    threshold = 1

    root = solution.insertAVL(items, threshold)

    print("Inorder traversal of the constructed AVL tree:")
    solution.print_inorder(root)
    print()

    print("Height of the constructed AVL tree:", solution._get_height(root))

    root = solution.insertAVL(items, threshold)
    print("Height of the updated AVL tree:", solution._get_height(root))

    print("Inorder traversal of the updated AVL tree:")
    solution.print_inorder(root)
    print()

    root = solution._insert(root, 60, threshold)
    print("Inorder traversal after inserting 60:")
    solution.print_inorder(root)
    print()

    root = solution._insert(root, 70, threshold)
    print("Inorder traversal after inserting 70:")
    solution.print_inorder(root)
    print()

    print("Finding 70 in the AVL tree:", solution.find(root, 70))
    print("Finding 100 in the AVL tree:", solution.find(root, 100))

    print("Height of the updated AVL tree:", solution._get_height(root))

    root = solution.deleteNode(root, 25, threshold)
    print("Inorder traversal after deleting 25:")
    solution.print_inorder(root)
    print()

    root = solution.deleteNode(root, 10, threshold)
    print("Inorder traversal after deleting 10:")
    solution.print_inorder(root)
    print()

    print("Order of key 30:", solution.order_of_key(root, 30))
    print("3rd smallest element (0-based index):", solution.get_by_order(root, 2))
    print("Order of key 60:", solution.order_of_key(root, 60))
