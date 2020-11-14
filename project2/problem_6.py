class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next

        return out_string

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

    def contains(self, item):
        cur_head = self.head
        while cur_head:
            if cur_head.value == item:
                return True
            cur_head = cur_head.next

        return False

    def to_list(self):
        out_list = []
        cur_head = self.head
        while cur_head:
            out_list.append(cur_head.value)
            cur_head = cur_head.next

        return out_list


def union(llist_1, llist_2):
    out = LinkedList()
    items = llist_1.to_list() + llist_2.to_list()
    for item in items:
        if not out.contains(item):
            out.append(item)

    return out


def intersection(llist_1, llist_2):
    out = LinkedList()
    list_1 = llist_1.to_list()
    list_2 = llist_2.to_list()

    for item_1 in list_1:
        for item_2 in list_2:
            if item_1 == item_2 and not out.contains(item_1):
                out.append(item_1)

    return out


def test_1():
    print('Test case 1')

    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
    element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    print(union(linked_list_1, linked_list_2))
    # 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 21 -> 32 -> 9 -> 1 -> 11 ->

    print(intersection(linked_list_1, linked_list_2))
    # 4 -> 6 -> 21 ->


def test_2():
    print('Test case 2')

    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
    element_2 = [1, 7, 8, 9, 11, 21, 1]

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)

    print(union(linked_list_3, linked_list_4))
    # 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 23 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 ->

    print(intersection(linked_list_3, linked_list_4))
    #


def test_3():
    print('Test case 3')

    linked_list_5 = LinkedList()
    linked_list_6 = LinkedList()

    element_1 = [3, 2, 4]
    element_2 = []

    for i in element_1:
        linked_list_5.append(i)

    for i in element_2:
        linked_list_6.append(i)

    print(union(linked_list_5, linked_list_6))
    # 3 -> 2 -> 4 ->

    print(intersection(linked_list_5, linked_list_6))
    #


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
