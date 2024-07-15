class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

    def __str__(self) -> str:
        return str(self.data)


class Stack:
    def __init__(self) -> None:
        self.head: Node = Node('head')
        self.size = 0

    def __str__(self) -> str:
        str_stack = ''

        curr = self.head
        while curr:
            str_stack += f'{curr.data} -> '
            curr = curr.next

        return str_stack + 'None'

    def push(self, data) -> None:
        node = Node(data)
        node.next = self.head.next  # Make the new node point to the current head
        self.head.next = node  # !!! # Update the head to be the new node
        self.size += 1

    def pop(self) -> Node:
        if self.size <= 0:
            return None

        curr = self.head
        prev = None
        while curr.next:
            prev = curr
            curr = curr.next

        prev.next = None
        self.size -= 1

        return curr

    def peek(self) -> Node:
        if self.size <= 0:
            return None

        curr = self.head
        while curr.next:
            curr = curr.next

        return curr

    def is_empty(self) -> bool:
        return self.size == 0

    def get_size(self) -> int:
        return self.size


def main() -> None:
    s = Stack()
    s.push(1)
    s.push(2)

    print(s.peek())

    print(s.get_size(), s.is_empty())


if __name__ == '__main__':
    main()
