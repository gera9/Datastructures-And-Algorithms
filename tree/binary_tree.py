class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left: Node | None = None
        self.right: Node | None = None

    def __str__(self) -> str:
        return str(self.data)


class Queue:
    def __init__(self) -> None:
        self.queue: list[Node] = []

    def put(self, data) -> None:
        self.queue.append(data)

    def get(self):
        return self.queue.pop(0)

    def peek(self) -> Node:
        return self.queue[0]

    def empty(self) -> bool:
        return len(self.queue) == 0

    def __str__(self) -> str:
        out = '['
        for e in self.queue:
            out += f'{e},'
        return out[:len(out)-1] + ']'


class BreadthFirstTraversal:
    def levelorder(self, root: Node | None) -> None:
        if not root:
            return

        q = Queue()
        q.put(root)

        while not q.empty():
            node: Node = q.get()
            print(node, end=' -> ')

            if node.left:
                q.put(node.left)

            if node.right:
                q.put(node.right)


class DepthFirstTraversal:
    # Preorder traversal visits the node in the order: Root -> Left -> Right
    def preorder(self, root: Node | None) -> None:
        if root is None:
            return

        print(root, end=' -> ')
        self.preorder(root.left)
        self.preorder(root.right)

    # Postorder traversal visits the node in the order: Left -> Right -> Root
    def postorder(self, root: Node | None) -> None:
        if root is None:
            return

        self.postorder(root.left)
        self.postorder(root.right)
        print(root, end=' -> ')

    # Inorder traversal visits the node in the order: Left -> Root -> Right
    def inorder(self, root: Node | None) -> None:
        if root is None:
            return

        self.inorder(root.left)
        print(root, end=' -> ')
        self.inorder(root.right)


def boundary_traversal(root: Node | None) -> None:
    if root is None:
        return

    print(root, end=' ')
    print_left_boundary(root.left)
    print_leaves(root)
    print_right_boundary(root.right)


def print_left_boundary(root: Node | None) -> None:
    if root is None:
        return

    if root.left is None:
        return

    print(root, end=' ')
    print_left_boundary(root.left)


def print_right_boundary(root: Node | None) -> None:
    if root is None:
        return

    if root.right is None:
        return

    print_right_boundary(root.right)
    print(root, end=' ')


def print_leaves(root: Node | None) -> None:
    if root is None:
        return

    print_leaves(root.left)
    if root.left is None and root.right is None:
        print(root, end=' ')
    print_leaves(root.right)


def insertion_in_level_order(root: Node | None, new_node: Node | None) -> None:
    if not new_node:
        return


def main() -> None:
    # Tree Structure
    #      1
    #    /   \
    #   2     3
    #  / \   / \
    # 4   5 6   7
    root = Node(1)

    root.left = Node(2)
    root.left.left = Node(4)
    root.left.right = Node(5)

    root.right = Node(3)
    root.right.left = Node(6)
    root.right.right = Node(7)

    dfs = DepthFirstTraversal()

    print("Inorder Traversal")
    dfs.inorder(root)

    print("None\nPreorder Traversal")
    dfs.preorder(root)

    print("None\nPostorder Traversal")
    dfs.postorder(root)

    bfs = BreadthFirstTraversal()

    print("None\nLevel Order Traversal")
    bfs.levelorder(root)

    print("None\nBoundary Traversal")
    boundary_traversal(root)


if __name__ == '__main__':
    main()
