from typing import Optional


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next: Optional[Node] = None

    def __str__(self) -> str:
        return str(self.data)


class Stack:
    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.size = 0

    def __str__(self) -> str:
        cur = self.head
        out = ""
        while cur:
            out += str(cur.data) + " -> "
            cur = cur.next
        return out + 'None'

    def push(self, data) -> None:
        node = Node(data)
        if self.head is None:
            self.head = node
            self.size += 1
            return

        node.next = self.head
        self.head = node
        self.size += 1

    def pop(self) -> Node:
        if self.head is None:
            raise Exception("Popping from an empty stack")

        temp = self.head
        self.head = temp.next

        self.size -= 1
        return temp

    def peek(self) -> Node:
        if self.head is None:
            raise Exception("Popping from an empty stack")

        return self.head

    def is_empty(self) -> bool:
        return self.size == 0

    def get_size(self) -> int:
        return self.size

    def push_bottom(self, data) -> None:
        if self.is_empty():
            self.push(data)
            return

        temp = self.pop()
        self.push_bottom(data)
        self.push(temp.data)


def get_higher_precedence(c: str) -> int:
    if c == '^':
        return 3
    elif c == '/' or c == '*':
        return 2
    elif c == '+' or c == '-':
        return 1
    else:
        return -1


def check_balanced_brackets(expr: str) -> bool:
    s = Stack()

    for c in expr:
        if c == '(' or c == '[' or c == '{':
            s.push(c)
            continue

        if c == ')' or c == ']' or c == '}':
            if s.is_empty():
                return False

            curr_char = s.pop().data
            if c == ')' and curr_char != '(':
                return False

            if c == ']' and curr_char != '[':
                return False

            if c == '}' and curr_char != '{':
                return False

    return s.is_empty()


def reverse_individual_words(txt: str) -> str:
    out = ''
    s = Stack()

    for c in txt:
        if c == ' ':
            while not s.is_empty():
                out += s.pop().data

            out += c

            continue

        s.push(c)

    while not s.is_empty():
        out += s.pop().data

    return out


def reverse_string(string: str) -> str:
    s = Stack()

    for c in string:
        s.push(c)

    out = ''
    while not s.is_empty():
        out += s.pop().data
    return out


def reverse_stack_recursion(s: Stack) -> Stack:
    def reverse(s: Stack):
        if s.is_empty():
            return

        temp = s.pop()
        reverse(s)
        s.push_bottom(temp.data)

    reverse(s)

    return s


def from_infix_to_postfix_expression(infix_exp: str) -> str:
    postfix = ''
    s = Stack()

    for char in infix_exp:
        if char == ' ':
            continue

        if ('a' <= char <= 'z') or ('A' <= char <= 'Z') or ('0' <= char <= '9'):
            postfix += char
            continue

        if char == '(':
            s.push(char)
            continue

        if char == ')':
            while not s.is_empty() and s.peek().data != '(':
                postfix += s.pop().data
            s.pop()
            continue

        while not s.is_empty() and (get_higher_precedence(char) <= get_higher_precedence(s.peek().data)) and char != '^':
            postfix += s.pop().data

        s.push(char)

    while not s.is_empty():
        postfix += s.pop().data

    return postfix


def main() -> None:
    # abc*+d+.
    print(from_infix_to_postfix_expression('a+b*(c^d-e)^(f+g*h)-i'))


if __name__ == '__main__':
    main()
