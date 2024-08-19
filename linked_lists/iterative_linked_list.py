from utils import EmptyLinkedListException, NodeNotFoundException, Node


class LinkedList:
    """Iterative implementation of a singly linked list."""

    def __init__(self, nodes=None) -> None:
        self.head: Node | None = None
        if nodes is not None:
            node = Node(nodes.pop(0))
            self.head: Node | None = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def travserse(self) -> None:
        node = self.head
        while node is not None:
            print(node)
            node = node.next

    def add_first(self, data) -> None:
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        """ aux = self.head
        self.head = new_node
        self.head.next = aux """
        new_node.next = self.head
        self.head = new_node

    def add_last(self, data) -> None:
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        node = self.head
        while node.next is not None:
            node = node.next

        node.next = new_node

    def length(self) -> int:
        n = 0
        node = self.head
        while node is not None:
            n += 1
            node = node.next
        return n

    def add_after(self, target_node_data, data) -> None:
        if self.head is None:
            raise EmptyLinkedListException()

        current_node = self.head
        while current_node is not None:
            if target_node_data == current_node.data:
                new_node = Node(data)
                new_node.next = current_node.next
                current_node.next = new_node
                return

            current_node = current_node.next

        raise NodeNotFoundException(target_node_data)

    def add_before(self, target_node_data, data) -> None:
        if self.head is None:
            raise EmptyLinkedListException()

        if self.head.data == target_node_data:
            return self.add_first(data)

        prev_node = self.head
        current_node = self.head
        while current_node is not None:
            if current_node.data == target_node_data:
                new_node = Node(data)
                new_node.next = current_node
                prev_node.next = new_node
                return

            prev_node = current_node
            current_node = current_node.next

        raise NodeNotFoundException(target_node_data)

    def remove_node(self, target_node_data) -> None:
        if self.head is None:
            raise EmptyLinkedListException()

        if self.head.data == target_node_data:
            self.head = self.head.next
            return

        current_node = self.head
        prev_node = self.head
        while current_node is not Node:
            if current_node.data == target_node_data:
                prev_node.next = current_node.next
                del current_node
                return

            prev_node = current_node
            current_node = current_node.next

        raise NodeNotFoundException(target_node_data)

    def get(self, index) -> None:
        if self.head is None:
            raise EmptyLinkedListException()

        i = 0
        current_node = self.head
        while current_node is not None:
            if i == index:
                return current_node.data

            i += 1
            current_node = current_node.next

        raise NodeNotFoundException()

    def reverse(self) -> None:
        if self.head is None:
            raise EmptyLinkedListException()

        prev_node = None
        curr_node = self.head
        while curr_node is not None:
            new_curr = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = new_curr

        self.head = prev_node

    def add_last_node(self, node: Node) -> None:
        if self.head is None:
            self.head = node
            return

        node = self.head
        while node.next is not None:
            node = node.next

        node.next = node

    def rotate(self, k: int) -> None:
        curr = self.head
        kthNode = None

        i = 1
        while curr:
            if i == k:
                kthNode = curr
                break

            curr = curr.next
            i += 1

        if curr is None:
            return

        while curr.next:
            curr = curr.next

        curr.next = self.head
        self.head = kthNode.next
        kthNode.next = None

    def from_last(self, index: int) -> None:
        length = self.length()
        if length == 0:
            raise EmptyLinkedListException

        if index < 0 or index > length:
            raise IndexError()

        curr = self.head
        i = 0
        while curr:
            if i == length - index:
                print(curr)
                return

            curr = curr.next
            i += 1

    def remove_duplicates(self) -> None:
        if self.head is None or self.head.next is None:
            return

        prev = self.head
        curr = prev.next
        while prev and curr:
            if prev.data == curr.data:
                nxt = curr.next
                prev.next = nxt
                temp = curr
                curr = nxt
                del temp
                continue

            prev = curr
            curr = curr.next

    def pairwise_swap(self) -> None:
        temp = self.head

        # There are no nodes in linked list
        if temp is None:
            return

        # Traverse furthethr only if there are at least two
        # left
        while (temp and temp.next):

            # If both nodes are same,
            # no need to swap data
            if (temp.data != temp.next.data):

                # Swap data of node with its next node's data
                temp.data, temp.next.data = temp.next.data, temp.data

            # Move temp by 2 to the next pair
            temp = temp.next.next


def reverse_linked_lists(ll1: LinkedList, ll2: LinkedList) -> LinkedList:
    if not ll1 and not ll2:
        raise Exception('empty linked both lists')

    if ll1 and not ll2:
        return ll1

    if not ll1 and ll2:
        return ll2

    new = LinkedList()
    curr_ll1 = ll1.head
    curr_ll2 = ll2.head

    while curr_ll1 and curr_ll2:
        nxt_ll1 = curr_ll1.next
        nxt_ll2 = curr_ll2.next
        print(curr_ll1, nxt_ll1)
        print(curr_ll2, nxt_ll2)

        if curr_ll1.data == curr_ll2.data and curr_ll1.data < curr_ll2.data:
            curr_ll1.next = curr_ll2
            new.add_last_node(curr_ll1)

        if curr_ll1.data > curr_ll2.data:
            curr_ll2.next = curr_ll1
            new.add_last_node(curr_ll2)

        ll1.head = nxt_ll1
        ll2.head = nxt_ll2
        curr_ll1 = nxt_ll1
        curr_ll2 = nxt_ll2

    return new


def main() -> None:
    ll = LinkedList([1, 2, 3, 4, 5, 6])

    print(ll)
    ll.pairwise_swap()
    print(ll)


if __name__ == '__main__':
    main()
