from utils import (
    Node,
    EmptyLinkedListException,
    NodeNotFoundException
)
from iterative_linked_list import LinkedList


class RecursiveLinkedList(LinkedList):
    """Recursive implementation of a singly linked list."""

    def __init__(self, nodes=None) -> None:
        self.head: Node | None = None
        if nodes is not None:
            node = Node(nodes.pop(0))
            self.head: Node | None = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def __repr__(self) -> str:
        def helper(node:  Node | None) -> str:
            if node.next is None:
                return node.__repr__()

            return f'{node.__repr__()} -> {helper(node.next)}'

        return helper(self.head) + ' -> None'

    def travserse(self) -> None:
        def helper(node: Node | None) -> None:
            if node is None:
                return
            print(node, end=' -> ')
            return helper(node.next)

        helper(self.head)

    def add_first(self, data) -> None:
        super().add_first(data)

    def add_last(self, data) -> None:
        new = Node(data)

        if self.head is None:
            self.head = new
            return

        def helper(node: Node) -> Node:
            if node.next is None:
                return node

            return helper(node.next)

        last = helper(self.head)
        last.next = new

    def length(self) -> int:
        if self.head is None:
            return 0

        def helper(node: Node, count: int) -> int:
            if node.next is None:
                return count

            return helper(node.next, count+1)

        return helper(self.head, 1)

    def add_after(self, target_node_data, data) -> None:
        if self.head is None:
            raise EmptyLinkedListException

        def helper(node: Node) -> Node:
            if node.next is None:
                return node

            curr = helper(node.next)
            if node.data == target_node_data:
                new = Node(data)
                new.next = curr
                node.next = new
                return new

            return curr

        if helper(self.head).data is not data:
            raise NodeNotFoundException

    def add_before(self, target_node_data, data) -> None:
        if self.head is None:
            raise EmptyLinkedListException

        if self.head.data == data:
            self.add_first(data)

        def helper(node: Node) -> Node:
            if node.next is None:
                return node

            curr = helper(node.next)
            if curr.data == target_node_data:
                new = Node(data)
                new.next = curr
                node.next = new
                return new

            return curr

        if helper(self.head).data is not data:
            raise NodeNotFoundException

    def remove_node(self, target_node_data) -> None:
        if self.head is None:
            raise EmptyLinkedListException

        if self.head.data == target_node_data:
            self.head = self.head.next
            return

        def helper(node: Node) -> Node:
            if node.next is None:
                return node

            nxt = node.next
            if nxt is not None and nxt.data == target_node_data:
                node.next = nxt.next
                return None

            return helper(node.next)

        if helper(self.head) is not None:
            raise NodeNotFoundException

    def get(self, index) -> None:
        if self.head is None:
            raise EmptyLinkedListException

        def helper(node: Node, i: int) -> Node:
            if node is None:
                return None

            if i == index:
                return node

            return helper(node.next, i+1)

        result = helper(self.head, 0)
        if result is None:
            raise NodeNotFoundException

        return result

    def reverse(self) -> None:
        if self.head is None:
            raise EmptyLinkedListException

        if self.head.next is None:
            return

        def helper(node: Node) -> Node:
            if node.next is None:
                self.head = node
                return node

            curr = helper(node.next)

            curr.next = node

            return node

        helper(self.head).next = None


def main() -> None:
    llist = RecursiveLinkedList(['a', 'c'])

    llist.add_before('c', 'b')
    print(llist)
    llist.reverse()
    print(llist)


if __name__ == '__main__':
    main()
