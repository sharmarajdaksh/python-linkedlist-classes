class _LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class _DoublyLinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def traverse(self):
        if self.head is None:
            return

        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

    def _get_last_node(self):
        if self.head is None:
            return None

        node = self.head
        while node.next is not None:
            node = node.next
        return node

    def insert(self, value):
        self.size += 1

        if self.head is None:
            self.head = _LinkedListNode(value)
            return

        node = _LinkedListNode(value)
        self._get_last_node().next = node

    def reverse(self):
        if self.head is None:
            return

        node = self.head
        last = None
        nxt = None

        while node is not None:
            nxt = node.next
            node.next = last
            last = node
            node = nxt

        self.head = last

    def _delete_head_node(self):
        head_ref = self.head
        self.head = self.head.next
        del head_ref

    def delete_by_index(self, index):
        if self.head is None:
            raise ValueError(
                'Delete operation not applicable on empty linked list')

        if self.size < index + 1:
            raise ValueError('Index our of range')

        self.size -= 1

        if index == 0:
            self._delete_head_node()
            return

        current_index = 0

        node = self.head
        last = None

        while node is not None:
            if current_index == index:
                node_ref = node
                last.next = node.next
                del node_ref
                return
            last = node
            node = node.next
            current_index += 1


class DoublyLinkedList(LinkedList):
    def insert(self, value):
        self.size += 1

        if self.head is None:
            self.head = _DoublyLinkedListNode(value)
            return

        node = _DoublyLinkedListNode(value)
        last_node = self._get_last_node()
        node.prev = last_node
        last_node.next = node

    def reverse(self):
        if self.head is None:
            return

        node = self.head

        while node is not None:
            t = node.next

            if t is None:
                self.head = node

            node.next = node.prev
            node.prev = t
            node = t

    def _delete_head_node(self):
        head_ref = self.head
        new_head = self.head.next
        if new_head is None:
            self.head = None
            return

        new_head.prev = None
        self.head = new_head
        del head_ref

    def delete_by_index(self, index):
        if self.head is None:
            raise ValueError(
                'Delete operation not applicable on empty linked list')

        if self.size < index + 1:
            raise ValueError('Index our of range')

        self.size -= 1

        if index == 0:
            self._delete_head_node()
            return

        current_index = 0

        node = self.head

        while node is not None:
            if current_index == index:
                node_ref = node
                node.prev.next = node.next
                node.next.prev = node.prev
                del node
                return
            node = node.next
            current_index += 1


class CircularLinkedList(LinkedList):
    def traverse(self):
        if self.head is None:
            return

        node = self.head
        print(node.value)
        node = node.next
        while node != self.head:
            print(node.value)
            node = node.next

    def _get_last_node(self):
        if self.head is None:
            return None

        node = self.head
        while node.next != self.head:
            node = node.next
        return node

    def insert(self, value):
        self.size += 1

        if self.head is None:
            self.head = _LinkedListNode(value)
            self.head.next = self.head
            return

        node = _LinkedListNode(value)
        last_node = self._get_last_node()
        last_node.next = node
        node.next = self.head

    def reverse(self):
        if self.head is None:
            return

        node = self.head
        last = None
        nxt = None

        while node.next != self.head:
            nxt = node.next
            node.next = last
            last = node
            node = nxt

        node.next = last
        self.head.next = node
        self.head = node

    def _delete_head_node(self):
        head_ref = self.head
        last_node = self._get_last_node()
        last_node.next = self.head.next
        self.head = self.head.next
        del head_ref
