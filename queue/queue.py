import time


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.nxt: Node | None = None

    def __str__(self) -> str:
        return str(self.data)


class Queue:
    def __init__(self, capacity: int) -> None:
        self.head: Node | None = None
        self.tail: Node | None = None
        self.capacity: int = capacity
        self.length: int = 0

    def __str__(self) -> str:
        if self.head is None:
            return 'empty :('
        out = ''
        curr = self.head
        while curr:
            out += f' <- {curr}'
            curr = curr.nxt
        return 'None' + out

    def enqueue(self, data) -> None:
        if self.length >= self.capacity:
            raise Exception('queue full')

        self.length += 1
        new_node = Node(data)

        if self.tail is None:
            self.tail = new_node
            self.head = new_node
            return

        self.tail.nxt = new_node
        self.tail = self.tail.nxt

    def dequeue(self) -> Node | None:
        if self.head is None:
            return None

        tmp = self.head
        self.head = self.head.nxt
        if self.head is None:
            self.tail = None

        return tmp

    def peek(self) -> Node | None:
        if self.head is None:
            return None

        return self.head

    def is_empty(self) -> bool:
        return self.head is None and self.tail is None

    def size(self) -> int:
        return self.length


def main() -> None:
    q = Queue(1)
    q.enqueue(1)
    print(q.size())
    q.enqueue(1)


if __name__ == '__main__':
    main()
