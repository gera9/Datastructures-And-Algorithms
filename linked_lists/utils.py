# Create own exceptions class for empty linked list
class EmptyLinkedListException(Exception):
    def __init__(self, message="Linked list is empty") -> None:
        self.message = message
        super().__init__(self.message)


class NodeNotFoundException(Exception):
    def __init__(self, data="") -> None:
        self.message = 'Node with data %s not found' % data
        super().__init__(self.message)


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next: Node | None = None

    def __repr__(self):
        return str(self.data)
