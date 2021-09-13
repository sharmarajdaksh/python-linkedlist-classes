from linked_list import CircularLinkedList, LinkedList, DoublyLinkedList


def main():
    ll = LinkedList()
    dll = DoublyLinkedList()
    cll = CircularLinkedList()

    print()
    print("=============================")
    print("SINGLY LINKED LIST OPERATIONS")
    print("=============================")
    print()

    ll.insert(3)
    ll.insert(9)
    ll.insert(1)
    ll.insert(7)
    ll.insert(9)

    print("FORWARD TRAVERSAL")
    ll.traverse()

    print("REVERSED TRAVERSAL")
    ll.reverse()
    ll.traverse()

    print("TRAVERSAL AFTER DELETION")
    ll.delete_by_index(2)
    ll.delete_by_index(2)
    ll.traverse()

    print()
    print("=============================")
    print("DOUBLY LINKED LIST OPERATIONS")
    print("=============================")
    print()

    cll.insert(3)
    cll.insert(9)
    cll.insert(1)
    cll.insert(7)
    cll.insert(9)

    print("FORWARD TRAVERSAL")
    cll.traverse()

    print("REVERSED TRAVERSAL")
    cll.reverse()
    cll.traverse()

    print("TRAVERSAL AFTER DELETION")
    cll.delete_by_index(2)
    cll.delete_by_index(2)
    cll.traverse()

    print()
    print("==============================")
    print("CIRCULAR LINKED LIST OPERATIONS")
    print("==============================")
    print()

    dll.insert(3)
    dll.insert(9)
    dll.insert(1)
    dll.insert(7)
    dll.insert(9)

    print("FORWARD TRAVERSAL")
    dll.traverse()

    print("REVERSED TRAVERSAL")
    dll.reverse()
    dll.traverse()

    print("TRAVERSAL AFTER DELETION")
    dll.delete_by_index(2)
    dll.delete_by_index(2)
    dll.traverse()


if __name__ == '__main__':
    main()
