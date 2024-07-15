class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.prev: Node = None
        self.next: Node = None

    def __str__(self) -> str:
        return str(self.data)


class DoublyLinkedList:
    def __init__(self, datas=None) -> None:
        self.head: Node = None
        self.tail: Node = None
        self.size: int = 0
        if datas is not None:
            for data in datas:
                self.add_last(data)

    def __str__(self) -> str:
        str_dll = ''
        curr = self.head

        while curr:
            str_dll += f'{curr.data} -> '
            curr = curr.next

        return str_dll + 'None'

    def add_last(self, data) -> None:
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node

            self.size += 1
            return

        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = self.tail.next

        self.size += 1

    def add_first(self, data) -> None:
        new_node = Node(data)

        if self.head is None:
            self.head = new_node

            self.size += 1
            return

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

        self.size += 1

    def traverse_forward(self) -> None:
        curr = self.head

        while curr:
            print(curr.data, end=' -> ')
            curr = curr.next

        print('None')

    def traverse_backward(self) -> None:
        curr = self.tail

        while curr:
            print(curr.data, end=' -> ')
            curr = curr.prev

        print('None')

    def length(self) -> int:
        return self.size

    def insert(self, index: int, data) -> None:
        if self.head is None and index != 0:
            raise Exception('empty doubly linked list')

        if index == 0:
            self.add_first(data)
            return

        curr = self.head
        i = 0
        while curr:
            if i == index:
                prev = curr.prev

                new_node = Node(data)

                prev.next = new_node
                new_node.prev = prev
                new_node.next = curr
                curr.prev = new_node

                self.size += 1
                return

            curr = curr.next
            i += 1

        raise Exception('index out of range')

    def delete_beginning(self) -> None:
        if self.head is None:
            raise Exception('empty doubly linked list')

        if self.head == self.tail:
            temp = self.head
            self.head = None
            self.tail = None
            del temp

            self.size -= 1
            return

        temp = self.head
        self.head = self.head.next
        self.head.prev = None
        del temp

        self.size -= 1

    def delete_end(self) -> None:
        if self.head is None:
            raise Exception('empty doubly linked list')

        if self.head == self.tail:
            temp = self.head
            self.head = None
            self.tail = None
            del temp

            self.size -= 1
            return

        temp = self.tail
        self.tail.prev.next = None
        self.tail = self.tail.prev
        del temp

        self.size -= 1

    def is_empty(self) -> bool:
        return self.head == self.tail

    def delete(self, index: int) -> None:
        if self.head is None:
            raise Exception('empty doubly linked list')

        if index == 0:
            self.delete_beginning()
            return

        if index == self.length()-1:
            self.delete_end()
            return

        curr = self.head
        count = 0
        while curr:
            if count == index:
                prev = curr.prev
                nxt = curr.next
                tmp = curr

                prev.next = nxt
                nxt.prev = prev
                del tmp

                self.size -= 1
                return

            curr = curr.next
            count += 1

        raise Exception('index out of range')


class RecursiveDoublyLinkedList(DoublyLinkedList):
    def __init__(self, datas=None) -> None:
        self.head: Node = None
        self.tail: Node = None
        self.size: int = 0
        if datas is not None:
            def helper(i: int) -> None:
                if i == len(datas):
                    return

                self.add_last(datas[i])

                return helper(i+1)

            helper(0)

    def add_last(self, data) -> None:
        return super().add_last(data)

    def add_first(self, data) -> None:
        return super().add_first(data)

    def __str__(self) -> str:
        def helper(node: Node) -> str:
            if node.next is None:
                return node.data

            return f'{node.data} -> {helper(node.next)}'

        return helper(self.head) + ' -> None'

    def traverse_forward(self) -> None:
        def helper(node: Node) -> None:
            if node is None:
                return

            print(node.data, end=' -> ')
            helper(node.next)

        helper(self.head)
        print('Node')

    def traverse_backward(self) -> None:
        def helper(node: Node) -> None:
            if node is None:
                return

            print(node.data, end=' -> ')
            helper(node.prev)

        helper(self.tail)
        print('Node')

    def length(self) -> int:
        return super().length()

    def insert(self, index: int, data) -> None:
        if index < 0 or index >= self.length():
            raise Exception('index out of range')

        if index == 0:
            self.add_first(data)
            return

        def helper(node: Node, i=0) -> None:
            if node is None:
                return

            if i == index:
                new_node = Node(data)
                prev = node.prev

                new_node.next = node
                node.prev = new_node
                prev.next = new_node
                new_node.prev = prev

            helper(node.next, i+1)

        helper(self.head)

    def delete_beginning(self) -> None:
        return super().delete_beginning()

    def delete_end(self) -> None:
        return super().delete_end()

    def is_empty(self) -> bool:
        return super().is_empty()

    def delete(self, index: int) -> None:
        if index < 0 or index >= self.length():
            raise Exception('index out of range')

        if index == 0:
            self.delete_beginning()
            return

        if index == self.length()-1:
            self.delete_end()
            return

        def helper(node: Node, i: int = 0) -> None:
            if not node:
                return

            if index == i:
                tmp = node
                prev = node.prev
                nxt = node.next

                prev.next = nxt
                nxt.prev = prev
                del tmp

                self.size -= 1
                return
            helper(node.next, i+1)

        helper(self.head, 0)

    def reverse(self) -> None:
        if self.head is None:
            return

        curr = self.head
        while curr:
            nxt = curr.next
            prev = curr.prev
            curr.next = prev
            curr.prev = nxt
            curr = nxt

        self.head, self.tail = self.tail, self.head


def main() -> None:
    rdll = RecursiveDoublyLinkedList(['A', 'B', 'C'])

    print(rdll, rdll.length())
    rdll.reverse()
    print(rdll, rdll.length())


if __name__ == '__main__':
    main()
