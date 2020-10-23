class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.previous = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.isEmpty = True
        self.size = 0

    def enqueue(self, key, value):
        new_node = Node(key, value)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node

        self.size += 1
        self.isEmpty = False

        return new_node

    def dequeue(self):
        if self.isEmpty:
            return None

        node = self.head

        if self.head == self.tail:
            self.head = None
            self.tail = None

        elif self.head is not None:
            self.head = self.head.next
            self.head.previous = None

        self.size -= 1
        if self.size <= 0:
            self.is_empty = True

        return node

    def remove(self, node):
        if node.previous is None and node.next is None:
            self.head = None
            self.tail = None
        elif node.previous is None:
            self.head = node.next
            self.head.previous = None
        elif node.next is None:
            self.tail = node.previous
            self.tail.next = None
        else:
            node.previous.next = node.next
            node.next.previous = node.previous


class LRU_Cache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.queue = Queue()

    def get(self, key):
        if key in self.cache:
            item = self.cache[key]
            self.queue.remove(item)
            self.queue.enqueue(key, item.value)
            return item.value
        else:
            return -1

    def set(self, key, value):
        if self.capacity <= 0:
            print(f"Operation is not supported with capacity of {self.capacity}")
            return

        if key in self.cache:
            self.queue.remove(self.cache[key])
            node = self.queue.enqueue(key, value)
            self.cache[key] = node
        else:
            if len(self.cache) >= self.capacity:
                node = self.queue.dequeue()
                self.cache.pop(node.key, None)

            self.cache[key] = self.queue.enqueue(key, value)


def test_1():
    print("test 1: Normal case")
    lru = LRU_Cache(5)
    lru.set(1, 1)
    lru.set(2, 2)
    lru.set(3, 3)
    lru.set(4, 4)

    print(lru.get(1))
    # returns 1
    print(lru.get(2))
    # returns 2
    print(lru.get(9))
    # returns -1 since there is no 9 in the cache

    lru.set(5, 5)
    lru.set(6, 6)

    print(lru.get(3))
    # returns -1 since the cache reached it's capacity and 3 was the least recently used entry


def test_2():
    print("test 2: Edge case with zero capacity")
    lru = LRU_Cache(0)
    lru.set(1, 1)
    # prints Operation is not supported with capacity of 0
    print(lru.get(1))
    # returns -1 since there is no such element


def test_3():
    print("test 3: Edge case with one capacity")
    lru = LRU_Cache(1)
    lru.set(3, 3)

    print(lru.get(3))
    # returns 3

    lru.set(2, 2)
    print(lru.get(3))
    # returns -1 since the cache reached it's capacity and 3 was the least recently used (actually the only) entry

    print(lru.get(2))
    # returns 2


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()