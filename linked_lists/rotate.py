from iterative_linked_list import LinkedList, Node


def rotate(head: Node, k: int) -> None:
    if k == 0:
        return

    curr = head
    count = 0
    while curr:
        if count == k:
            tmp = curr.next
            curr.next = None
            tmp.next = curr
            return

        curr = curr.next
        count += 1


def main() -> None:
    ll = LinkedList([30, 40, 50, 60])
    k = 2

    print(ll)
    rotate(ll.head, k)
    print(ll)  # 50->60->30->40


if __name__ == '__main__':
    main()
