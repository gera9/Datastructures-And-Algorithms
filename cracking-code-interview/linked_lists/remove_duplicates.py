"""
Remove duplicates from an unsorted linked list.

Temporary buffer is NOT allowed.
"""


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next: Node | None = None

    def __str__(self) -> str:
        str_repr = ''

        curr = self
        while curr:
            str_repr += f'{curr.data} -> '
            curr = curr.next

        return str_repr + 'None'

# 10 -> 1 -> 3 -> 1


def remove_duplicates(head: Node) -> None:
    curr = head
    while curr:

        prev = curr
        nxt = curr.next
        while nxt:
            if curr.data == nxt.data:
                prev.next = nxt.next
                return

            prev = nxt
            nxt = nxt.next

        curr = curr.next


def main() -> None:
    root = Node(10)
    root.next = Node(1)
    root.next.next = Node(3)
    root.next.next.next = Node(1)

    print(root)

    remove_duplicates(root)

    print(root)


if __name__ == '__main__':
    main()
