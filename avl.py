class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def height_calculation(self, node):
        if not node:
            return 0
        return node.height

    def balancing_factor_calculation(self, node):
        if not node:
            return 0
        return self.height_calculation(node.right) - self.height_calculation(node.left)

    def rotate_left(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node

        node.height = max(self.height_calculation(node.left), self.height_calculation(node.right)) + 1
        new_root.height = max(self.height_calculation(new_root.left), self.height_calculation(new_root.right)) + 1

        return new_root

    def rotate_right(self, node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node

        node.height = max(self.height_calculation(node.left), self.height_calculation(node.right)) + 1
        new_root.height = max(self.height_calculation(new_root.left), self.height_calculation(new_root.right)) + 1

        return new_root

    def rotate_left_right(self, node):
        node.left = self.rotate_left(node.left)
        return self.rotate_right(node)

    def rotate_right_left(self, node):
        node.right = self.rotate_right(node.right)
        return self.rotate_left(node)

    def insertion(self, node, value):
        if not node:
            return Node(value)

        if value < node.value:
            node.left = self.insertion(node.left, value)
        elif value > node.value:
            node.right = self.insertion(node.right, value)
        else:
            return node

        node.height = max(self.height_calculation(node.left), self.height_calculation(node.right)) + 1

        balance_factor = self.balancing_factor_calculation(node)

        if balance_factor > 1:
            if value < node.right.value:
                node = self.rotate_right_left(node)
            else:
                node = self.rotate_left(node)
        elif balance_factor < -1:
            if value > node.left.value:
                node = self.rotate_left_right(node)
            else:
                node = self.rotate_right(node)

        return node

    def deletion(self, node, value):
        if not node:
            return node

        if value < node.value:
            node.left = self.deletion(node.left, value)
        elif value > node.value:
            node.right = self.deletion(node.right, value)
        else:
            if not node.left or not node.right:
                temp = node.left if node.left else node.right

                if not temp:
                    temp = node
                    node = None
                else:
                    node = temp

            else:
                temp = self.find_min(node.right)
                node.value = temp.value
                node.right = self.deletion(node.right, temp.value)

        if not node:
            return node

        node.height = max(self.height_calculation(node.left), self.height_calculation(node.right)) + 1

        balance_factor = self.balancing_factor_calculation(node)

        if balance_factor > 1:
            if self.balancing_factor_calculation(node.right) < 0:
                node = self.rotate_right_left(node)
            else:
                node = self.rotate_left(node)
        elif balance_factor < -1:
            if self.balancing_factor_calculation(node.left) > 0:
                node = self.rotate_left_right(node)
            else:
                node = self.rotate_right(node)

        return node

    def search(self, node, value):
        if not node or node.value == value:
            return node

        if value < node.value:
            return self.search(node.left, value)
        else:
            return self.search(node.right, value)

    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.value, end=" ")
            self.inorder_traversal(node.right)

    def preorder_traversal(self, node):
        if node:
            print(node.value, end=" ")
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)

    def postorder_traversal(self, node):
        if node:
            self.postorder_traversal(node.left)
            self.postorder_traversal(node.right)
            print(node.value, end=" ")

    def calculate_diameter(self, node, height):
        if not node:
            height[0] = 0
            return 0

        left_height = [0]
        right_height = [0]
        left_diameter = self.calculate_diameter(node.left, left_height)
        right_diameter = self.calculate_diameter(node.right, right_height)

        height[0] = max(left_height[0], right_height[0]) + 1

        current_diameter = left_height[0] + right_height[0] + 1
        return max(current_diameter, max(left_diameter, right_diameter))

    def find_min(self, node):
        while node.left:
            node = node.left
        return node

    def find_max(self, node):
        while node.right:
            node = node.right
        return node

    def find_successor(self, node, value):
        current = self.search(node, value)
        if not current:
            return None

        if current.right:
            return self.find_min(current.right)

        successor = None
        ancestor = self.root
        while ancestor != current:
            if current.value < ancestor.value:
                successor = ancestor
                ancestor = ancestor.left
            else:
                ancestor = ancestor.right

        return successor

    def find_predecessor(self, node, value):
        current = self.search(node, value)
        if not current:
            return None

        if current.left:
            return self.find_max(current.left)

        predecessor = None
        ancestor = self.root
        while ancestor != current:
            if current.value > ancestor.value:
                predecessor = ancestor
                ancestor = ancestor.right
            else:
                ancestor = ancestor.left

        return predecessor

    def insert(self, value):
        self.root = self.insertion(self.root, value)

    def delete(self, value):
        self.root = self.deletion(self.root, value)

    def search_value(self, value):
        return self.search(self.root, value) is not None

    def inorder(self):
        self.inorder_traversal(self.root)
        print()

    def preorder(self):
        self.preorder_traversal(self.root)
        print()

    def postorder(self):
        self.postorder_traversal(self.root)
        print()

    def height(self):
        return self.height_calculation(self.root)

    def diameter(self):
        height = [0]
        return self.calculate_diameter(self.root, height)

    def find_min_value(self):
        min_node = self.find_min(self.root)
        return min_node.value if min_node else -1

    def find_max_value(self):
        max_node = self.find_max(self.root)
        return max_node.value if max_node else -1

    def find_successor_value(self, value):
        successor = self.find_successor(self.root, value)
        return successor.value if successor else -1

    def find_predecessor_value(self, value):
        predecessor = self.find_predecessor(self.root, value)
        return predecessor.value if predecessor else -1


if __name__ == "__main__":
    tree = AVLTree()

    tree.insert(5)
    tree.insert(18)
    tree.insert(22)
    tree.insert(31)
    tree.insert(8)
    tree.insert(43)
    tree.insert(55)
    tree.insert(28)
    tree.insert(39)
    tree.insert(11)

    print("Inorder Traversal: ", end="")
    tree.inorder()

    print("----------------------------------------------------")

    print("Preorder Traversal: ", end="")
    tree.preorder()

    print("----------------------------------------------------")

    print("Postorder Traversal: ", end="")
    tree.postorder()

    print("----------------------------------------------------")

    print(f"Height of the tree is {tree.height()}")
    print(f"Diameter of the tree is: {tree.diameter()}")

    print("----------------------------------------------------")

    print(f"Minimum value of the Tree is: {tree.find_min_value()}")
    print(f"Maximum value of the Tree is: {tree.find_max_value()}")

    print("----------------------------------------------------")

    print(f"Successor of 43 is: {tree.find_successor_value(43)}")
    print(f"Predecessor of 43 is: {tree.find_predecessor_value(43)}")

    print("----------------------------------------------------")

    tree.delete(43)
    print("Inorder Traversal after deleting value 43 is: ", end="")
    tree.inorder()
